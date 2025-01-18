from Model.user_model import UserModel

class UserController:
    def __init__(self):
        self.model = UserModel()

    def register_student(self, first_name, last_name, student_id, email, password, program, major):
        data = {
            "first_name": first_name,
            "last_name": last_name,
            "student_id": student_id,
            "email": email,
            "password": password,
            "program": program,
            "major": major,
        }
        return self.model.insert_student(data)

    def register_teacher(self, first_name, last_name, teacher_id, email):
        data = {
            "first_name": first_name,
            "last_name": last_name,
            "teacher_id": teacher_id,
            "email": email,
        }
        return self.model.insert_teacher(data)

    def login_Account(self, email, password):
        data= {
            "email": email,
            "password": password,
        }
        return self.model.check_student(data)