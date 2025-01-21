from supabase_manager import get_supabase_client
import bcrypt
import random
import smtplib
from email.mime.text import MIMEText

class UserModel:
    def __init__(self):
        self.client = get_supabase_client()

    def generate_code(self):
        return str(random.randint(1000, 9999))

    def send_code_to_email(self, email, code):
        sender_email = "jiroluismanalo24@gmail.com"
        sender_password = "onpc xdvm svqx axhb"
        subject = "Password Recovery Code"
        body = f"Your password recovery code is: {code}"

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = email

        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, email, msg.as_string())
            return {"status": "success", "message": "Code sent to email."}
        except Exception as e:
            return {"status": "fail", "message": str(e)}

    def request_password_reset(self, email):
        email_check_result = self.check_email(email)
        if email_check_result["status"] == "found":
            code = self.generate_code()
            self.send_code_to_email(email, code)
            return {"status": "success", "code": code}  # Store this code temporarily
        else:
            return {"status": "fail", "message": "Email not found."}

    def change_password(self, email, new_password):
        hashed_password = self.hash_password(new_password)
        try:
            response = self.client.table("student_table").update({"password": hashed_password}).eq("email", email).execute()
            return response
        except Exception as e:
            return {"error": str(e)}

    def check_student_record(self, student_id, last_name, first_name):
        try:
            response = (
                self.client.table("student_records")
                .select("*")
                .eq("student_id", student_id)
                .eq("last_name", last_name)
                .eq("first_name", first_name)
                .execute()
            )
            return response.data
        except Exception as e:
            return {"error": str(e)}

    def check_teacher_record(self, last_name, teacher_id, first_name):
        try:
            response = (
                self.client.table("teacher_records")
                .select("*")
                .eq("teacher_id", teacher_id)
                .eq("last_name", last_name)
                .eq("first_name", first_name)
                .execute()
            )
            return response.data
        except Exception as e:
            return {"error": str(e)}

    def check_user_id(self, user_id):
        try:
            teacher_response = self.client.table("teacher_table").select("*").eq("teacher_id", user_id).execute()
            student_response = self.client.table("student_table").select("*").eq("student_id", user_id).execute()

            if teacher_response.data:
                return {"status": "found", "role": "teacher", "data": teacher_response.data}
            elif student_response.data:
                return {"status": "found", "role": "student", "data": student_response.data}
            else:
                return {"status": "not_found", "message": "ID not found in records."}
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def check_email(self, email):
        try:
            teacher_response = self.client.table("teacher_table").select("*").eq("email", email).execute()
            student_response = self.client.table("student_table").select("*").eq("email", email).execute()

            if teacher_response.data:
                return {"status": "found", "role": "teacher", "data": teacher_response.data}
            elif student_response.data:
                return {"status": "found", "role": "student", "data": student_response.data}
            else:
                return {"status": "not_found", "message": "Email not found in records."}
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def login_checker(self, email, password):
        try:
            for role, table in [("teacher", "teacher_table"), ("student", "student_table")]:
                response = self.client.table(table).select("*").eq("email", email).execute()
                if response.data:
                    user = response.data[0]
                    if self.verify_password(password, user.get("password")):
                        full_name = f"{user.get('first_name')} {user.get('last_name')}"

                        # Check the role and fetch either student_id or teacher_id
                        if role == "teacher":
                            teacher_id = user.get("teacher_id", None)
                            return {
                                "status": "found",
                                "role": role,
                                "teacher_id": teacher_id,  # Return teacher_id for teachers
                                "full_name": full_name,
                                "message": f"Welcome, {user.get('last_name')}",
                                "data": user,
                            }
                        else:
                            student_id = user.get("student_id", None)
                            return {
                                "status": "found",
                                "role": role,
                                "student_id": student_id,  # Return student_id for students
                                "full_name": full_name,
                                "message": f"Welcome, {user.get('last_name')}",
                                "data": user,
                            }
                    return {"status": "not_found", "message": "Incorrect email or password."}
            return {"status": "not_found", "message": "Incorrect email or password."}
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def insert_student(self, data):
        try:
            response = self.client.table("student_table").insert(data).execute()
            return response
        except Exception as e:
            return {"error": str(e)}

    def insert_teacher(self, data):
        try:
            response = self.client.table("teacher_table").insert(data).execute()
            return response
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def hash_password(password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    @staticmethod
    def verify_password(password, hashed_password):
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))