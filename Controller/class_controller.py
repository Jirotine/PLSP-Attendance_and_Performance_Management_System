from Model.class_model import ClassModel

class ClassController:
    def __init__(self):
        self.model = ClassModel()

    def create_class(self, class_name, teacher_id):
        if not class_name.strip():
            raise ValueError("Class name cannot be empty.")
        return self.model.add_class(class_name, teacher_id)

    def fetch_classes_for_teacher(self, teacher_id):
        return self.model.get_classes_by_teacher(teacher_id)
