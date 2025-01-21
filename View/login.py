from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.toast import toast
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton, MDFlatButton, MDTextButton
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from Controller.user_controller import UserController
from session_manager import SessionManager
from View.home_page import Home_Student, Home_Teacher
from View.forgot_password import Forgot_Password
from View.register import Registration_Type

class Login(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.session = SessionManager()

        self.UserController = UserController()

        layout = FloatLayout(size_hint=(1, 1))

        # Background Image
        background = Image(
            source="assets/background.png",
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(2, 1),
            pos_hint={"x": 0, "y": 0},
        )
        layout.add_widget(background)

        # Card
        card = MDCard(
            orientation="vertical",
            size_hint=(0.9, None),
            height="370dp",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            radius=[15, 15, 15, 15],
            padding=[20, 20, 20, 20],
            spacing="25dp"
        )

        spacer = BoxLayout(size_hint_y=None, height="20dp")
        card.add_widget(spacer)

        logo = Image(
            source="assets/logo.png",
            size_hint=(0.6, None),
            height="150dp",
            pos_hint={"center_x": 0.5, "center_y": 0.2},
        )
        card.add_widget(logo)

        text_fields_box = BoxLayout(
            orientation="vertical",
            spacing="15dp",
            size_hint=(1, None),
        )

        # Email Field
        self.email_field = MDTextField(
            hint_text="Email",
            size_hint_x=1,
            mode="rectangle",
            font_name="Roboto-Bold",
        )
        text_fields_box.add_widget(self.email_field)

        # Password Field
        self.password_field = MDTextField(
            hint_text="Password",
            size_hint_x=1,
            mode="rectangle",
            password=True,
            font_name="Roboto-Bold",
        )
        text_fields_box.add_widget(self.password_field)

        card.add_widget(text_fields_box)

        def switch_to_forgot_password_screen(instance):
            self.manager.add_widget(Forgot_Password(name="forgot_password"))
            self.manager.current = "forgot_password"

        forgot_password_button = MDTextButton(
            text="Forgot Password?",
            size_hint=(1, None),
            pos_hint={"center_x": 0.8},
            font_style="Body2",
            font_name="assets/fonts/Uni Sans Heavy.otf",
            bold=True,
        )
        forgot_password_button.bind(on_release=switch_to_forgot_password_screen)
        card.add_widget(forgot_password_button)

        # Login Functionality
        def login_checker_ui(instance):
            email = self.email_field.text
            password = self.password_field.text

            if not email or not password:
                toast("Please enter both email and password.")
            else:
                result = self.UserController.login_account(email, password)
                if result["status"] == "success":
                    toast(result.get("message"))
                    full_name = result.get("full_name")
                    role = result.get("role")
                    student_id = result.get("student_id")
                    teacher_id = result.get("teacher_id")  # Get teacher_id for teachers

                    if full_name:
                        self.session.set("full_name", full_name)
                    if role:
                        self.session.set("role", role)
                    if student_id:
                        self.session.set("student_id", student_id)
                    if teacher_id:
                        self.session.set("teacher_id", teacher_id)  # Store teacher_id in session

                    if role == "student":
                        self.manager.add_widget(Home_Student(name="Home_Student"))
                        self.manager.current = "Home_Student"
                    else:
                        self.manager.add_widget(Home_Teacher(name="Home_Teacher"))
                        self.manager.current = "Home_Teacher"

                    # Clear the fields after successful login
                    self.email_field.text = ""
                    self.password_field.text = ""
                else:
                    toast(result.get("message"))

        login_button = MDRaisedButton(
            text="Login",
            size_hint=(1, None),
            height="50dp",
            pos_hint={"center_x": 0.5},
            text_color=[1, 1, 1, 1],
            font_name="assets/fonts/Uni Sans Heavy.otf",
        )
        login_button.bind(on_release=login_checker_ui)
        card.add_widget(login_button)

        def switch_to_register_screen(instance):
            self.manager.add_widget(Registration_Type(name="Registration_Type"))
            self.manager.current = "Registration_Type"

        register_button = MDFlatButton(
            text="Register",
            size_hint=(1, None),
            height="50dp",
            pos_hint={"center_x": 0.5},
            font_name="assets/fonts/Uni Sans Heavy.otf",
        )
        register_button.bind(on_release=switch_to_register_screen)
        card.add_widget(register_button)

        layout.add_widget(card)

        self.add_widget(layout)
