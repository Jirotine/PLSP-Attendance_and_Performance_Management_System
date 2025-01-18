from Model.user_model import UserModel

class UserController:
    def __init__(self):
        self.model = UserModel()

    def register_student(self, first_name, last_name, student_id, email, password, program, major):
        hashed_password = self.model.hash_password(password)
        data = {
            "first_name": first_name,
            "last_name": last_name,
            "student_id": student_id,
            "email": email,
            "password": hashed_password,
            "program": program,
            "major": major,
        }
        result = self.model.insert_student(data)
        if "error" in result:
            return {"status": "fail", "message": result["error"]}
        return {"status": "success", "message": "Student registered successfully!"}

    def register_teacher(self, first_name, last_name, teacher_id, email, password):
        data = {
            "first_name": first_name,
            "last_name": last_name,
            "teacher_id": teacher_id,
            "email": email,
            "passowrd": password
        }
        result = self.model.insert_teacher(data)
        if "error" in result:
            return {"status": "fail", "message": result["error"]}
        return {"status": "success", "message": "Teacher registered successfully!"}

    def login_account(self, email, password):
        user = self.model.check_student(email)
        if not user:
            return {"status": "fail", "message": "User not found"}

        hashed_password = user[0].get("password")
        if self.model.verify_password(password, hashed_password):
            return {"status": "success", "message": "Login successful!"}
        return {"status": "fail", "message": "Invalid email or password"}
