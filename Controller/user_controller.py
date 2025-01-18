from Model.user_model import UserModel

class UserController:
    def __init__(self):
        self.model = UserModel()

    def validate_student(self, last_name, student_id):
        try:
            student = self.model.check_student_record(student_id, last_name)
            if not student:
                return {"status": "fail", "message": "Student not found in records. Registration denied."}
            return {"status": "success"}  # Successful validation
        except Exception as e:
            return {"status": "fail", "message": f"An error occurred: {str(e)}"}

    def validate_email(self, email):
        try:
            email_check_result = self.model.check_email(email)

            if email_check_result["status"] == "found":
                return {"status": "fail", "message": "Email already registered."}
            elif email_check_result["status"] == "not_found":
                return {"status": "success"}  # Email is not registered
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

    def validate_teacher(self, last_name, teacher_id):
        try:
            student = self.model.check_teacher_record(last_name, teacher_id)
            if not student:
                return {"status": "fail", "message": "Teacher not found in records."}
            return {"status": "success"}  # Successful validation
        except Exception as e:
            return {"status": "fail", "message": f"An error occurred: {str(e)}"}

    def register_student(self, first_name, last_name, student_id, email, password):
        hashed_password = self.model.hash_password(password)
        data = {
            "first_name": first_name,
            "last_name": last_name,
            "student_id": student_id,
            "email": email,
            "password": hashed_password,
        }
        result = self.model.insert_student(data)
        if "error" in result:
            return {"status": "fail", "message": result["error"]}
        return {"status": "success", "message": "Student registered successfully!"}

    def register_teacher(self, first_name, last_name, teacher_id, email, password):

        hashed_password = self.model.hash_password(password)
        data = {
            "first_name": first_name,
            "last_name": last_name,
            "teacher_id": teacher_id,
            "email": email,
            "password": hashed_password,
        }
        result = self.model.insert_teacher(data)
        if "error" in result:
            return {"status": "fail", "message": result["error"]}
        return {"status": "success", "message": "Teacher registered successfully!"}

    def login_account(self, email, password):
        user = self.model.login_checker(email, password)

        if user.get("status") != "found":
            return {"status": "fail", "message": user.get("message", "User not found")}

        hashed_password = user["data"][0].get("password")
        if self.model.verify_password(password, hashed_password):
            # Use the message from `login_checker` directly
            return {"status": "success", "message": user["message"], "role": user["role"]}

        return {"status": "fail", "message": "Invalid email or password"}

