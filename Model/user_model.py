from supabase_manager import get_supabase_client

class UserModel:
    def __init__(self):
        self.client = get_supabase_client()

    def insert_student(self, data):
        response = self.client.table("student_table").insert(data).execute()
        return response

    def insert_teacher(self, data):
        response = self.client.table("teachers").insert(data).execute()
        return response

    def check_student(self, data):
        response = self.client.table("student_table").where("email={}".format(data['email'])).execute()