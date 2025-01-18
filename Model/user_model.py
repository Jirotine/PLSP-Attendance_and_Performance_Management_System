from supabase_manager import get_supabase_client
import bcrypt  # For password hashing

class UserModel:
    def __init__(self):
        self.client = get_supabase_client()

    # Registration Model
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

    def check_student(self, email):
        try:
            response = self.client.table("student_table").select("*").eq("email", email).execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def hash_password(password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    @staticmethod
    def verify_password(password, hashed_password):
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
