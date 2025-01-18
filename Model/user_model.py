from supabase_manager import get_supabase_client
import bcrypt

class UserModel:
    def __init__(self):
        self.client = get_supabase_client()

    def check_student_record(self, student_id, last_name):
        try:
            response = (
                self.client.table("student_records")
                .select("*")
                .eq("student_id", student_id)
                .eq("last_name", last_name)
                .execute()
            )
            return response.data
        except Exception as e:
            return {"error": str(e)}

    # Check if a teacher is in the teacher_records table
    def check_teacher_record(self, last_name, teacher_id):
        try:
            response = (
                self.client.table("teacher_records")
                .select("*")
                .eq("teacher_id", teacher_id)
                .eq("last_name", last_name)
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
            # Check in the teacher table
            teacher_login_response = self.client.table("teacher_table").select("*").eq("email", email).execute()

            if teacher_login_response.data:
                # If a teacher is found, verify the password
                hashed_password = teacher_login_response.data[0].get("password")
                if self.verify_password(password, hashed_password):
                    last_name = teacher_login_response.data[0].get("last_name")
                    return {
                        "status": "found",
                        "role": "teacher",
                        "message": f"Welcome, {last_name}",
                        "data": teacher_login_response.data
                    }
                else:
                    return {"status": "not_found", "message": "Incorrect Email or Password."}

            # Check in the student table
            student_login_response = self.client.table("student_table").select("*").eq("email", email).execute()

            if student_login_response.data:
                # If a student is found, verify the password
                hashed_password = student_login_response.data[0].get("password")
                if self.verify_password(password, hashed_password):
                    last_name = student_login_response.data[0].get("last_name")
                    return {
                        "status": "found",
                        "role": "student",
                        "message": f"Welcome, {last_name}",
                        "data": student_login_response.data
                    }
                else:
                    return {"status": "not_found", "message": "Incorrect Email or Password."}

            # If no user is found in both tables
            return {"status": "not_found", "message": "Incorrect Email or Password."}

        except Exception as e:
            # Log the exception here
            return {"status": "error", "message": str(e)}

    def check_teacher(self, field, value):
        try:
            response = self.client.table("teacher_table").select("*").eq(field, value).execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}

    def insert_student(self, data):
        try:
            print("Inserting student data:", data)
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
