from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout

class Forgot_Password(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

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
            height="200dp",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            radius=[15, 15, 15, 15],
            padding=[20, 20, 20, 20],
            spacing="20dp"
        )

        enter_email = MDLabel(
            text="ENTER YOUR EMAIL HERE",
            font_name="assets/fonts/Uni Sans Heavy.otf",
            font_style="Body1",
            bold=True,
            halign="center",
        )
        card.add_widget(enter_email)

        email_field = MDTextField(
            hint_text="Email",
            size_hint_x=1,
            mode="rectangle",
            font_name="Roboto-Bold",
        )
        card.add_widget(email_field)

        button_layout = BoxLayout(
            orientation="horizontal",
            size_hint=(1, None),
            height="50dp",
            spacing="20dp",
            pos_hint={"center_x": 0.5}
        )

        def switch_to_login_screen(instance):
            self.manager.current = "Login"

        login_button = MDRectangleFlatButton(
            text="< Back to Login",
            size_hint=(1, None),
            height="50dp",
            pos_hint={"center_x": 0.5},
            font_name="assets/fonts/Uni Sans Heavy.otf",
        )
        login_button.bind(on_release=switch_to_login_screen)
        button_layout.add_widget(login_button)

        def switch_to_forgot_password2_screen(instance):
            self.manager.current = "forgot_password2"

        submit_button = MDRectangleFlatButton(
            text="Send Code",
            size_hint=(1, None),
            height="50dp",
            pos_hint={"center_x": 0.5},
            font_name="assets/fonts/Uni Sans Heavy.otf",
        )
        submit_button.bind(on_release=switch_to_forgot_password2_screen)
        button_layout.add_widget(submit_button)

        card.add_widget(button_layout)

        layout.add_widget(card)

        self.add_widget(layout)


class Forgot_Password2(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

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
            height="200dp",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            radius=[15, 15, 15, 15],
            padding=[20, 20, 20, 20],
            spacing="20dp"
        )

        enter_code = MDLabel(
            text="ENTER YOUR CODE HERE",
            font_name="assets/fonts/Uni Sans Heavy.otf",
            font_style="Body1",
            bold=True,
            halign="center",
        )
        card.add_widget(enter_code)

        code_field = MDTextField(
            hint_text="Code",
            size_hint_x=1,
            mode="rectangle",
            font_name="Roboto-Bold",
        )
        card.add_widget(code_field)

        button_layout = BoxLayout(
            orientation="horizontal",
            size_hint=(1, None),
            height="50dp",
            spacing="20dp",
            pos_hint={"center_x": 0.5}
        )

        def switch_to_login_screen(instance):
            self.manager.current = "Login"

        login_button = MDRectangleFlatButton(
            text="< Back to Login",
            size_hint=(1, None),
            height="50dp",
            pos_hint={"center_x": 0.5},
            font_name="assets/fonts/Uni Sans Heavy.otf",
        )
        login_button.bind(on_release=switch_to_login_screen)
        button_layout.add_widget(login_button)

        def switch_to_forgot_password3_screen(instance):
            self.manager.current = "forgot_password3"

        submit_button = MDRectangleFlatButton(
            text="Submit Code",
            size_hint=(1, None),
            height="50dp",
            pos_hint={"center_x": 0.5},
            font_name="assets/fonts/Uni Sans Heavy.otf",
        )
        submit_button.bind(on_release=switch_to_forgot_password3_screen)
        button_layout.add_widget(submit_button)

        card.add_widget(button_layout)

        layout.add_widget(card)

        self.add_widget(layout)

class Forgot_Password3(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

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
            height="300dp",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            radius=[15, 15, 15, 15],
            padding=[20, 20, 20, 20],
            spacing="25dp"
        )

        change_password = MDLabel(
            text="SET YOUR NEW PASSWORD",
            font_name="assets/fonts/Uni Sans Heavy.otf",
            font_style="Body1",
            bold=True,
            halign="center",
        )
        card.add_widget(change_password)


        password_field = MDTextField(
            hint_text="New Password",
            password=True,
            size_hint_x=1,
            mode="rectangle",
            font_name="Roboto-Bold",
        )
        card.add_widget(password_field)

        confirm_password_field = MDTextField(
            hint_text="Confirm Password",
            password=True,
            size_hint_x=1,
            mode="rectangle",
            font_name="Roboto-Bold",
        )
        card.add_widget(confirm_password_field)

        def switch_to_login_screen(instance):
            self.manager.current = "Login"

        submit_button = MDRectangleFlatButton(
            text="Submit",
            size_hint=(1, None),
            height="50dp",
            pos_hint={"center_x": 0.5},
            font_name="assets/fonts/Uni Sans Heavy.otf",
        )
        submit_button.bind(on_release=switch_to_login_screen)
        card.add_widget(submit_button)

        layout.add_widget(card)

        self.add_widget(layout)