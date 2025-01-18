from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.toast import toast
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton, MDRectangleFlatButton, MDIconButton
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.boxlayout import BoxLayout
from Controller.user_controller import UserController

class BaseRegistrationScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_controller = UserController()
        self.registration_data = {
        }

class Registration_Type(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout(size_hint=(1, 1))

        background = Image(
            source="assets/background.png",
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(2, 1),
            pos_hint={"x": 0, "y": 0},
        )
        layout.add_widget(background)

        card = MDCard(
            orientation="vertical",
            size_hint=(0.9, None),
            height="220dp",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            radius=[15, 15, 15, 15],
            padding=[20, -20, 20, 20],
            spacing="25dp"
        )

        self.user_type = MDRectangleFlatButton(
            text="Select User Type",
            size_hint=(1, None),
            height="50dp",
            pos_hint={"center_x": 0.5},
            font_name="Roboto-Bold"
        )
        user_type_menu = [
            {"text": "Student", "on_release": lambda x="Student": self.set_program(x)},
            {"text": "Teacher", "on_release": lambda x="Teacher": self.set_program(x)},
        ]
        self.user_menu = MDDropdownMenu(
            caller=self.user_type,
            items=user_type_menu,
            width_mult=4
        )
        self.user_type.bind(on_release=lambda instance: self.user_menu.open())
        card.add_widget(self.user_type)

        register_button = MDRaisedButton(
            text=">",
            text_color=[1, 1, 1, 1],
            size_hint=(1, None),
            height="50dp",
            pos_hint={"center_x": 0.5},
            font_name="assets/fonts/Uni Sans Heavy.otf",
        )
        register_button.bind(on_release=self.go_to_next_screen)
        card.add_widget(register_button)

        def switch_to_login_screen(instance):
            self.manager.current = "Login"

        login_button = MDIconButton(
            icon="close-circle",
            size_hint=(1, None),
            theme_text_color="Custom",
            text_color=(0, 0.6, 0, 1),
            height="50dp",
            pos_hint={"center_x": 0.5},
        )
        login_button.bind(on_release=switch_to_login_screen)
        card.add_widget(login_button)

        layout.add_widget(card)
        self.add_widget(layout)

    def set_program(self, text):
        self.user_type.text = text
        self.user_menu.dismiss()

    def go_to_next_screen(self, instance):
        if self.user_type.text == "Student":
            self.manager.current = "Register_Student1"
        elif self.user_type.text == "Teacher":
            self.manager.current = "Register_Teacher1"
        else:
            toast("Please select a user type!")

class Register_Student1(BaseRegistrationScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout(size_hint=(1, 1))

        background = Image(
            source="assets/background.png",
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(2, 1),
            pos_hint={"x": 0, "y": 0},
        )
        layout.add_widget(background)

        card = MDCard(
            orientation="vertical",
            size_hint=(0.9, None),
            height="380dp",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            radius=[15, 15, 15, 15],
            padding=[20, 20, 20, 20],
            spacing="25dp"
        )

        text_fields_box = BoxLayout(
            orientation="vertical",
            spacing="15dp",
            size_hint=(1, None),
        )

        self.first_name_field = MDTextField(
            hint_text="First Name",
            size_hint_x=1,
            mode="rectangle",
            font_name="Roboto-Bold"
        )
        text_fields_box.add_widget(self.first_name_field)

        self.last_name_field = MDTextField(
            hint_text="Last Name",
            size_hint_x=1,
            mode="rectangle",
            font_name="Roboto-Bold"
        )
        text_fields_box.add_widget(self.last_name_field)

        self.student_id_field = MDTextField(
            hint_text="Student ID",
            size_hint_x=1,
            mode="rectangle",
            font_name="Roboto-Bold"
        )
        text_fields_box.add_widget(self.student_id_field)

        card.add_widget(text_fields_box)

        def submit_info(instance):
            first_name = self.first_name_field.text
            last_name = self.last_name_field.text
            student_id = self.student_id_field.text

            self.registration_data.update({"first_name": first_name})
            self.registration_data.update({"last_name": last_name})
            self.registration_data.update({"student_id": student_id})

            if not (first_name and last_name and student_id):
                toast("Please fill up the missing fields")
            else:
                print("Registration Data:", self.registration_data)
                self.manager.current = "Register_Student2"
                self.manager.get_screen("Register_Student2").registration_data = self.registration_data

        register_button = MDRaisedButton(
            text=">",
            size_hint=(1, None),
            height="50dp",
            pos_hint={"center_x": 0.5},
            font_name="assets/fonts/Uni Sans Heavy.otf",
            text_color=[1, 1, 1, 1],
        )
        register_button.bind(on_release=submit_info)
        card.add_widget(register_button)

        def switch_to_login_screen(instance):
            self.manager.current = "Login"

        login_button = MDIconButton(
            icon="close-circle",
            size_hint=(1, None),
            theme_text_color="Custom",
            text_color=(0, 0.6, 0, 1),
            height="50dp",
            pos_hint={"center_x": 0.5},
        )
        login_button.bind(on_release=switch_to_login_screen)
        card.add_widget(login_button)

        layout.add_widget(card)
        self.add_widget(layout)

class Register_Student2(BaseRegistrationScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout(size_hint=(1, 1))

        background = Image(
            source="assets/background.png",
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(2, 1),
            pos_hint={"x": 0, "y": 0},
        )
        layout.add_widget(background)

        card = MDCard(
            orientation="vertical",
            size_hint=(0.9, None),
            height="280dp",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            radius=[15, 15, 15, 15],
            padding=[20, -20, 20, 20],
            spacing="25dp"
        )

        self.program_type = MDRectangleFlatButton(
            text="Select Program",
            size_hint=(1, None),
            height="50dp",
            pos_hint={"center_x": 0.5},
            font_name="Roboto-Bold"
        )
        program_type_menu = [
            {"text": "BA in Communication", "on_release": lambda x="BA in Communication": self.set_program_name(x)},
        ]
        self.program_menu = MDDropdownMenu(
            caller=self.program_type,
            items=program_type_menu,
            width_mult=1,
            position="center"
        )
        self.program_type.bind(on_release=lambda instance: self.program_menu.open())
        card.add_widget(self.program_type)

        self.major_field = MDRectangleFlatButton(
            text="Select Major",
            size_hint=(1, None),
            height="50dp",
            pos_hint={"center_x": 0.5},
            font_name="Roboto-Bold"
        )
        major_menu_items = [
            {"text": "Computer Science", "on_release": lambda x="Computer Science": self.set_major(x)},
        ]
        self.major_menu = MDDropdownMenu(
            caller=self.major_field,
            items=major_menu_items,
            width_mult=4
        )
        self.major_field.bind(on_release=lambda instance: self.major_menu.open())
        card.add_widget(self.major_field)

        def submit_info2(instance):
            program = self.program_type.text
            major = self.major_field.text

            self.registration_data.update({"program": program})
            self.registration_data.update({"major": major})

            if not (major and program):
                toast("Please fill up the missing fields")
            else:
                print("Registration Data:", self.registration_data)
                self.manager.current = "Register_Student3"
                self.manager.get_screen("Register_Student3").registration_data = self.registration_data

        register_button = MDRaisedButton(
            text=">",
            text_color=[1, 1, 1, 1],
            size_hint=(1, None),
            height="50dp",
            pos_hint={"center_x": 0.5},
            font_name="assets/fonts/Uni Sans Heavy.otf",
        )
        register_button.bind(on_release=submit_info2)
        card.add_widget(register_button)

        def switch_to_login_screen(instance):
            self.manager.current = "Login"

        login_button = MDIconButton(
            icon="close-circle",
            size_hint=(1, None),
            theme_text_color="Custom",
            text_color=(0, 0.6, 0, 1),
            height="50dp",
            pos_hint={"center_x": 0.5},
        )
        login_button.bind(on_release=switch_to_login_screen)
        card.add_widget(login_button)

        layout.add_widget(card)
        self.add_widget(layout)

    def set_program_name(self, text):
        self.program_type.text = text
        self.program_menu.dismiss()

    def set_major(self, text):
        self.major_field.text = text
        self.major_menu.dismiss()

class Register_Student3(BaseRegistrationScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout(size_hint=(1, 1))

        background = Image(
            source="assets/background.png",
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(2, 1),
            pos_hint={"x": 0, "y": 0},
        )
        layout.add_widget(background)

        card = MDCard(
            orientation="vertical",
            size_hint=(0.9, None),
            height="380dp",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            radius=[15, 15, 15, 15],
            padding=[20, 20, 20, 20],
            spacing="25dp"
        )

        text_fields_box = BoxLayout(
            orientation="vertical",
            spacing="15dp",
            size_hint=(1, None),
        )

        self.email_field = MDTextField(
            hint_text="Email",
            size_hint_x=1,
            mode="rectangle",
            font_name="Roboto-Bold"
        )
        text_fields_box.add_widget(self.email_field)

        self.password_field = MDTextField(
            hint_text="Password",
            password=True,
            size_hint_x=1,
            mode="rectangle",
            font_name="Roboto-Bold"
        )
        text_fields_box.add_widget(self.password_field)

        self.confirm_password_field = MDTextField(
            hint_text="Confirm Password",
            password=True,
            size_hint_x=1,
            mode="rectangle",
            font_name="Roboto-Bold"
        )
        text_fields_box.add_widget(self.confirm_password_field)

        card.add_widget(text_fields_box)

        first_name = self.registration_data.get("first_name", "")
        last_name = self.registration_data.get("last_name", "")
        student_id = self.registration_data.get("student_id", "")
        program = self.registration_data.get("program", "")
        major = self.registration_data.get("major", "")

        def submit_info3(instance):
            password = self.password_field.text
            email = self.email_field.text
            confirm_password = self.confirm_password_field.text

            self.registration_data["password"] = password
            self.registration_data["email"] = email

            if not (password and email and confirm_password):
                toast("Please fill up the missing fields")
            elif password != confirm_password:
                toast("Passwords do not match")
            else:
                self.user_controller.register_student(
                    first_name=self.registration_data.get("first_name"),
                    last_name=self.registration_data.get("last_name"),
                    student_id=self.registration_data.get("student_id"),
                    email=email,
                    password=password,
                    program=self.registration_data.get("program"),
                    major=self.registration_data.get("major")
                )
                toast("Registration Successful")
                self.manager.current = "Login"

        def switch_to_login_screen(instance):
            self.manager.current = "Login"

        register_button = MDRaisedButton(
            text="Register",
            size_hint=(1, None),
            text_color=[1, 1, 1, 1],
            height="50dp",
            pos_hint={"center_x": 0.5},
            font_name="assets/fonts/Uni Sans Heavy.otf",
        )
        register_button.bind(on_release=submit_info3)
        card.add_widget(register_button)

        login_button = MDIconButton(
            icon="close-circle",
            size_hint=(1, None),
            theme_text_color="Custom",
            text_color=(0, 0.6, 0, 1),
            height="50dp",
            pos_hint={"center_x": 0.5},
        )
        login_button.bind(on_release=switch_to_login_screen)
        card.add_widget(login_button)

        layout.add_widget(card)
        self.add_widget(layout)

class Register_Teacher1(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout(size_hint=(1, 1))

        background = Image(
            source="assets/background.png",
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(2, 1),
            pos_hint={"x": 0, "y": 0},
        )
        layout.add_widget(background)

        card = MDCard(
            orientation="vertical",
            size_hint=(0.9, None),
            height="380dp",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            radius=[15, 15, 15, 15],
            padding=[20, 20, 20, 20],
            spacing="25dp"
        )

        text_fields_box = BoxLayout(
            orientation="vertical",
            spacing="15dp",
            size_hint=(1, None),
        )

        first_name_field = MDTextField(
            hint_text="First Name",
            size_hint_x=1,
            mode="rectangle",
            font_name="Roboto-Bold"
        )
        text_fields_box.add_widget(first_name_field)

        last_name_field = MDTextField(
            hint_text="Last Name",
            size_hint_x=1,
            mode="rectangle",
            font_name="Roboto-Bold"
        )
        text_fields_box.add_widget(last_name_field)

        student_id_field = MDTextField(
            hint_text="Teacher ID",
            size_hint_x=1,
            mode="rectangle",
            font_name="Roboto-Bold"
        )
        text_fields_box.add_widget(student_id_field)

        card.add_widget(text_fields_box)

        def switch_to_register_student2_screen(instance):
            self.manager.current = "Register_Teacher2"

        register_button = MDRaisedButton(
            text=">",
            size_hint=(1, None),
            height="50dp",
            pos_hint={"center_x": 0.5},
            font_name="assets/fonts/Uni Sans Heavy.otf",
            text_color=[1, 1, 1, 1],
        )
        register_button.bind(on_release=switch_to_register_student2_screen)
        card.add_widget(register_button)

        def switch_to_login_screen(instance):
            self.manager.current = "Login"

        login_button = MDIconButton(
            icon="close-circle",
            size_hint=(1, None),
            theme_text_color="Custom",
            text_color=(0, 0.6, 0, 1),
            height="50dp",
            pos_hint={"center_x": 0.5},
        )
        login_button.bind(on_release=switch_to_login_screen)
        card.add_widget(login_button)

        layout.add_widget(card)
        self.add_widget(layout)

class Register_Teacher2(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout(size_hint=(1, 1))

        background = Image(
            source="assets/background.png",
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(2, 1),
            pos_hint={"x": 0, "y": 0},
        )
        layout.add_widget(background)

        card = MDCard(
            orientation="vertical",
            size_hint=(0.9, None),
            height="380dp",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            radius=[15, 15, 15, 15],
            padding=[20, 20, 20, 20],
            spacing="25dp"
        )

        text_fields_box = BoxLayout(
            orientation="vertical",
            spacing="15dp",
            size_hint=(1, None),
        )

        email_field = MDTextField(
            hint_text="Email",
            size_hint_x=1,
            mode="rectangle",
            font_name="Roboto-Bold"
        )
        text_fields_box.add_widget(email_field)

        password_field = MDTextField(
            hint_text="Password",
            password=True,
            size_hint_x=1,
            mode="rectangle",
            font_name="Roboto-Bold"
        )
        text_fields_box.add_widget(password_field)

        confirm_password_field = MDTextField(
            hint_text="Confirm Password",
            password=True,
            size_hint_x=1,
            mode="rectangle",
            font_name="Roboto-Bold"
        )
        text_fields_box.add_widget(confirm_password_field)

        card.add_widget(text_fields_box)

        def switch_to_login_screen(instance):
            self.manager.current = "Login"

        register_button = MDRaisedButton(
            text="Register",
            size_hint=(1, None),
            text_color=[1, 1, 1, 1],
            height="50dp",
            pos_hint={"center_x": 0.5},
            font_name="assets/fonts/Uni Sans Heavy.otf",
        )
        register_button.bind(on_release=switch_to_login_screen)
        card.add_widget(register_button)

        login_button = MDIconButton(
            icon="close-circle",
            size_hint=(1, None),
            theme_text_color="Custom",
            text_color=(0, 0.6, 0, 1),
            height="50dp",
            pos_hint={"center_x": 0.5},
        )
        login_button.bind(on_release=switch_to_login_screen)
        card.add_widget(login_button)

        layout.add_widget(card)
        self.add_widget(layout)