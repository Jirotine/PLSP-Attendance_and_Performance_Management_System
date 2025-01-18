from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screenmanager import ScreenManager
from View.login import Login
from View.register import Register_Student1, Register_Student2, Registration_Type, Register_Teacher1, Register_Teacher2
from View.home_page import Home_Student, Home_Teacher
from View.forgot_password import Forgot_Password, Forgot_Password2, Forgot_Password3

class MainApp(MDApp):
    def build(self):
        Window.size = (360, 640)
        self.theme_cls.primary_palette = "Green"

        screen_manager = ScreenManager()

        screen_manager.add_widget(Login(name="Login"))

        screen_manager.add_widget(Registration_Type(name="Registration_Type"))

        screen_manager.add_widget(Register_Student1(name="Register_Student1"))

        screen_manager.add_widget(Register_Student2(name="Register_Student2"))

        screen_manager.add_widget(Register_Teacher1(name="Register_Teacher1"))

        screen_manager.add_widget(Register_Teacher2(name="Register_Teacher2"))

        screen_manager.add_widget(Home_Student(name="Home_Student"))

        screen_manager.add_widget(Home_Teacher(name="Home_Teacher"))

        screen_manager.add_widget(Forgot_Password(name="forgot_password"))

        screen_manager.add_widget(Forgot_Password2(name="forgot_password2"))

        screen_manager.add_widget(Forgot_Password3(name="forgot_password3"))

        return screen_manager

if __name__ == "__main__":
    MainApp().run()