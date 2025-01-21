from supabase_manager import get_supabase_client
import random
import string

class ClassModel:
    def __init__(self):
        self.client = get_supabase_client()

    def generate_class_code(self):
        # Generate a unique 6-character alphanumeric code
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    def add_class(self, class_name, teacher_id):
        try:
            if not class_name.strip():
                raise ValueError("Class name cannot be empty.")

            # Check if a class with the same name already exists
            response = self.client.table("classes").select("*").eq("class_name", class_name).execute()

            if response.data:  # If data exists, the class name already exists
                raise ValueError("Class name already exists.")

            # Ensure class code is unique
            while True:
                class_code = self.generate_class_code()
                response = self.client.table("classes").select("*").eq("class_code", class_code).execute()

                if not response.data:  # Check if no data is returned
                    break

            # Insert class into the classes table
            response = self.client.table("classes").insert({
                "class_name": class_name,
                "class_code": class_code,
                "teacher_id": teacher_id
            }).execute()

            # Instead of response.error, inspect response structure
            if hasattr(response, "data") and response.data:
                return class_code  # Return the class code if insertion was successful
            else:
                raise Exception(f"Unexpected response structure: {response}")

        except Exception as e:
            return {"error": str(e)}

    def get_classes_by_teacher(self, teacher_id):
        try:
            response = self.client.table("classes").select("*").eq("teacher_id", teacher_id).execute()

            if response.data is None or isinstance(response.data, list) and not response.data:
                raise Exception(f"Failed to fetch classes: {response.error or 'No classes found.'}")

            return response.data
        except Exception as e:
            return {"error": str(e)}

