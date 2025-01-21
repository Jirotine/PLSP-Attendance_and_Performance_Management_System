from Model.user_model import UserModel

class UserController:
    def __init__(self):
        self.model = UserModel()

    def validate_student(self, last_name, student_id):
        try:
            student = self.model.check_student_record(student_id, last_name)
            if not student:
                return {"status": "fail", "message": "Student not found in records. Registration denied."}
            return {"status": "success"}
        except Exception as e:
            return {"status": "fail", "message": f"An error occurred: {str(e)}"}

    def validate_email(self, email):
        if not email or "@" not in email:
            return {"status": "fail", "message": "Invalid email format."}
        try:
            email_check_result = self.model.check_email(email)

            if email_check_result["status"] == "found":
                return {"status": "fail", "message": "Email already registered."}
            elif email_check_result["status"] == "not_found":
                return {"status": "success"}
            else:
                return {"status": "error", "message": email_check_result.get("message", "Unknown error occurred.")}
        except Exception as e:
            return {"status": "fail", "message": f"An error occurred: {str(e)}"}

    def validate_user_id(self, user_id):
        try:
            id_check_result = self.model.check_user_id(user_id)

            if id_check_result["status"] == "found":
                return {"status": "fail", "message": "ID already registered."}
            elif id_check_result["status"] == "not_found":
                return {"status": "success"}
            else:
                return {"status": "error", "message": id_check_result.get("message", "Unknown error occurred.")}
        except Exception as e:
            return {"status": "fail", "message": f"An error occurred: {str(e)}"}

    def register_student(self, first_name, last_name, student_id, email, password, password_code):
        email_check = self.validate_email(email)
        if email_check["status"] == "fail":
            return email_check

        id_check = self.validate_user_id(student_id)
        if id_check["status"] == "fail":
            return id_check

        hashed_password = self.model.hash_password(password)
        data = {
            "first_name": first_name,
            "last_name": last_name,
            "student_id": student_id,
            "email": email,
            "password": hashed_password,
            "password_code": password_code,
        }
        result = self.model.insert_student(data)
        if "error" in result:
            return {"status": "fail", "message": result["error"]}
        return {"status": "success", "message": "Student registered successfully!"}

    def register_teacher(self, first_name, last_name, teacher_id, email, password, password_code):
        email_check = self.validate_email(email)
        if email_check["status"] == "fail":
            return email_check

        id_check = self.validate_user_id(teacher_id)
        if id_check["status"] == "fail":
            return id_check

        hashed_password = self.model.hash_password(password)
        data = {
            "first_name": first_name,
            "last_name": last_name,
            "teacher_id": teacher_id,
            "email": email,
            "password": hashed_password,
            "password_code": password_code,
        }
        result = self.model.insert_teacher(data)
        if "error" in result:
            return {"status": "fail", "message": result["error"]}
        return {"status": "success", "message": "Teacher registered successfully!"}

    def request_password_reset(self, email):
        return self.model.request_password_reset(email)

    def login_account(self, email, password):
        user = self.model.login_checker(email, password)

        if user.get("status") != "found":
            return {"status": "fail", "message": user.get("message", "User not found")}

        teacher_id = user.get("teacher_id") if user["role"] == "teacher" else None

        return {
            "status": "success",
            "message": user["message"],
            "full_name": user["full_name"],
            "student_id": user.get("student_id"),
            "teacher_id": teacher_id,  # Include teacher_id for teachers
            "role": user["role"],
        }
