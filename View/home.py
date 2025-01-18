from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDIconButton, MDFlatButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField

class Home_Student(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout(size_hint=(1, 1))

        background = Image(
            source="assets/background.png",
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(1, 1),
            pos_hint={"x": 0, "y": 0},
        )
        layout.add_widget(background)

        card_user_profile = MDCard(
            orientation="vertical",
            size_hint=(0.9, None),
            height="230dp",
            pos_hint={"center_x": 0.5, "center_y": 0.75},
            radius=[15, 15, 15, 15],
            padding=[20, 20, 20, 20],
            spacing="15dp"
        )

        profile_icon = MDIconButton(
            icon="account-circle",
            pos_hint={"center_x": 0.5},
            theme_text_color="Custom",
            text_color=(0, 0.6, 0, 1),
            icon_size="70dp",
        )
        card_user_profile.add_widget(profile_icon)

        card_user_profile.add_widget(
            MDLabel(
                text="JIRO LUIS MANALO",
                halign="center",
                theme_text_color="Primary",
                font_style="H6",
                bold=True,
            )
        )

        icons_layout = BoxLayout(
            orientation="horizontal",
            size_hint=(None, None),
            width="120dp",
            height="50dp",
            spacing="20dp",
            pos_hint={"center_x": 0.5},
        )

        qr_code_icon = MDIconButton(
            icon="qrcode",
            theme_text_color="Custom",
            text_color=(0, 0.6, 0, 1),
            icon_size="30dp",
        )

        def switch_to_login_screen(instance):
            self.manager.current = "Login"

        logout_icon = MDIconButton(
            icon="logout",
            theme_text_color="Custom",
            text_color=(0, 0.6, 0, 1),
            icon_size="30dp",
        )
        logout_icon.bind(on_release=switch_to_login_screen)

        icons_layout.add_widget(qr_code_icon)
        icons_layout.add_widget(logout_icon)

        card_user_profile.add_widget(icons_layout)

        layout.add_widget(card_user_profile)

        card_user_class = MDCard(
            orientation="vertical",
            size_hint=(0.9, 0.5),
            pos_hint={"center_x": 0.5, "center_y": 0.28},
            radius=[15, 15, 15, 15],
            padding=[10, 10, 10, 10],
        )

        # ScrollView for the grid of icons
        scroll_view = ScrollView(size_hint=(1, 1))

        # GridLayout to hold folders/icons
        self.grid_layout = GridLayout(
            cols=3,
            spacing=10,
            size_hint_y=None,
        )
        self.grid_layout.bind(minimum_height=self.grid_layout.setter("height"))

        scroll_view.add_widget(self.grid_layout)
        card_user_class.add_widget(scroll_view)

        self.dialog = None

        def open_add_class_dialog(instance):
            if not self.dialog:
                self.dialog = MDDialog(
                    title="ADD CLASS",
                    type="custom",
                    content_cls=MDTextField(
                        hint_text="Enter Class Name",
                        font_name="assets/fonts/Uni Sans Heavy.otf",
                        mode="rectangle",
                    ),
                    buttons=[
                        MDFlatButton(
                            text="CANCEL",
                            font_name="assets/fonts/Uni Sans Heavy.otf",
                            theme_text_color="Custom",
                            text_color=(0, 0.6, 0, 1),
                            on_release=lambda x: self.dialog.dismiss()
                        ),
                        MDFlatButton(
                            text="ADD",
                            theme_text_color="Custom",
                            text_color=(0, 0.6, 0, 1),
                            font_name="assets/fonts/Uni Sans Heavy.otf",
                            on_release=lambda x: add_class(self.dialog.content_cls.text)
                        ),
                    ],
                )
            self.dialog.open()

        def add_class(class_name):
            if class_name.strip():
                new_button_layout = FloatLayout(size_hint=(None, None), size=(125, 100))

                new_icon = MDIconButton(
                    icon="notebook",
                    theme_text_color="Custom",
                    text_color=(0, 0.6, 0, 1),
                    icon_size="50dp",
                    pos_hint={"center_x": 0.5, "top": 1},
                )
                new_label = MDLabel(
                    text=class_name,
                    halign="center",
                    size_hint=(1, None),
                    height="20dp",
                    bold=True,
                    font_style="Caption",
                    pos_hint={"center_x": 0.5, "y": 0},
                )

                new_button_layout.add_widget(new_icon)
                new_button_layout.add_widget(new_label)

                self.grid_layout.add_widget(new_button_layout)

            self.dialog.dismiss()

        add_class_button = MDIconButton(
            icon="plus-box",
            pos_hint={"center_x": 0.5},
            icon_size="60dp",
            theme_text_color="Custom",
            text_color=(0, 0.6, 0, 1),
        )
        add_class_button.bind(on_release=open_add_class_dialog)
        self.grid_layout.add_widget(add_class_button)

        layout.add_widget(card_user_class)

        # Add the main layout to the screen
        self.add_widget(layout)
