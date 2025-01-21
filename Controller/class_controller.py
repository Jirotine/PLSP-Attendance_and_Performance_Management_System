from Model.class_model import ClassModel
from session_manager import SessionManager

class ClassController:
    def __init__(self):
        self.model = ClassModel()
        self.session = SessionManager()

    def fetch_class_by_code(self, class_code):
        class_data = self.model.get_class_by_code(class_code)
        if class_data:
            return class_data
        else:
            return {"error": "Class not found."}

    def enroll_student_in_class(self, student_id, class_id):
        response = self.model.add_student_to_class(student_id, class_id)
        if response is None:
            return {"error": "Failed to add student to class."}
        return {"success": f"Student {student_id} added to class {class_id}."}

    def create_class(self, class_name, teacher_id):
        if not class_name.strip():
            raise ValueError("Class name cannot be empty.")
        return self.model.add_class(class_name, teacher_id)

    def fetch_classes_for_teacher(self, teacher_id):
        return self.model.get_classes_by_teacher(teacher_id)

    def fetch_classes_for_student(self, student_id):
        return self.model.get_classes_by_student(student_id)

    def get_student_id(self):
        # Get the student_id from the session
        student_id = self.session.get("student_id", "Unknown ID")
        if student_id == "Unknown ID":
            print("Warning: student_id not set in session, defaulting to 'Unknown ID'")
        return student_id

    def add_class(self, class_code, student_id):
        try:
            # Check if the class_code exists in the database
            response = self.model.client.table("classes").select("*").eq("class_code", class_code).execute()

            if not response.data:  # If no class is found with the given code
                raise ValueError("Invalid class code.")

            # Fetch class_name and class_id
            class_data = response.data[0]
            class_name = class_data["class_name"]
            class_id = class_data["id"]

            # Insert student and class relationship into the student_classes table
            insert_response = self.model.client.table("student_classes").insert({
                "student_id": student_id,
                "class_id": class_id
            }).execute()

            if insert_response.data:
                return f"Student successfully added to the class '{class_name}'."
            else:
                raise Exception("Failed to enroll the student in the class.")

        except Exception as e:
            return {"error": str(e)}

