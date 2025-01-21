from kivy.uix.scrollview import ScrollView
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivy.uix.boxlayout import BoxLayout
from Controller.class_controller import ClassController
from session_manager import SessionManager
# import matplotlib.pyplot as plt

class ClassPage_Teacher(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Create a layout for the screen
        layout = FloatLayout(size_hint=(1, 1))

        # Initialize class controller and session manager
        self.class_controller = ClassController()
        self.session = SessionManager()

        # Get the class information from the session
        class_name = self.session.get("class_name", "Class")
        class_code = self.session.get("class_code", "Code")

        # Background image setup
        background = Image(
            source="assets/background.png",
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(1, 1),
            pos_hint={"x": 0, "y": 0},
        )
        layout.add_widget(background)

        # Card layout for content
        card_class = MDCard(
            orientation="vertical",
            size_hint=(0.9, 0.7),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            radius=[15, 15, 15, 15],
            padding="20dp",
            spacing="30dp",
        )
        layout.add_widget(card_class)

        # Course label layout
        course_label_layout = BoxLayout(
            orientation="vertical",
            size_hint=(1, 1),
            height="50dp",
            spacing="5dp",
        )
        card_class.add_widget(course_label_layout)

        course_code_label = MDLabel(
            text="Course Code",
            halign="center",
            font_style="Subtitle1",
            theme_text_color="Custom",
            text_color=[0, 0.6, 0, 1],
            font_name="Roboto-Bold",
            bold=True,
        )
        course_label_layout.add_widget(course_code_label)

        course_class_label = MDRaisedButton(
            text=class_code,  # Use the class code from the session
            elevation=0,
            size_hint=(0.5, 1),
            pos_hint={"center_x": 0.5},
            theme_text_color="Custom",
            text_color=[1, 1, 1, 1],
            font_name="assets/fonts/Uni Sans Heavy.otf",
        )
        course_label_layout.add_widget(course_class_label)

        # Course class layout
        course_label_class_layout = BoxLayout(
            orientation="vertical",
            size_hint=(1, 1),
            height="50dp",
            spacing="5dp",
        )
        card_class.add_widget(course_label_class_layout)

        course_code_class_label = MDLabel(
            text="Course Name",
            halign="center",
            font_style="Subtitle1",
            theme_text_color="Custom",
            text_color=[0, 0.6, 0, 1],
            font_name="Roboto-Bold",
            bold=True,
        )
        course_label_class_layout.add_widget(course_code_class_label)

        course_name_class_label = MDRaisedButton(
            text=class_name,  # Use the class name from the session
            elevation=0,
            size_hint=(0.5, 1),
            pos_hint={"center_x": 0.5},
            theme_text_color="Custom",
            text_color=[1, 1, 1, 1],
            font_name="assets/fonts/Uni Sans Heavy.otf",
        )
        course_label_class_layout.add_widget(course_name_class_label)

        # Add the layout to the screen
        self.add_widget(layout)

class ClassPage_Student(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout(size_hint=(1, 1))

        # Background image
        background = Image(
            source="assets/background.png",
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(1, 1),
            pos_hint={"x": 0, "y": 0},
        )
        layout.add_widget(background)

        # Profile card
        card_user_profile = MDCard(
            orientation="vertical",
            size_hint=(0.9, None),
            height="250dp",  # Adjusted height for the graph
            pos_hint={"center_x": 0.5, "center_y": 0.75},
            radius=[15, 15, 15, 15],
            padding=[20, 20, 20, 20],
            spacing="15dp"
        )

        # Icon layout
        icon_layout = BoxLayout(
            orientation="horizontal",
            size_hint=(None, None),
            width="120dp",
            height="50dp",
            spacing="20dp",
            pos_hint={"center_x": 0.5},
        )
        card_user_profile.add_widget(icon_layout)

        # Add Class button
        add_class_button = MDIconButton(
            icon="plus-box",
            theme_text_color="Custom",
            text_color=(0, 0.6, 0, 1),
            icon_size="30dp",
            pos_hint={"center_x": 0.5},
        )
        icon_layout.add_widget(add_class_button)

        # Logout button
        logout_icon = MDIconButton(
            icon="logout-variant",
            theme_text_color="Custom",
            text_color=(0, 0.6, 0, 1),
            icon_size="30dp",
            pos_hint={"center_x": 0.5},
        )
        icon_layout.add_widget(logout_icon)

        layout.add_widget(card_user_profile)

        # Class card
        card_user_class = MDCard(
            orientation="vertical",
            size_hint=(0.9, 0.5),
            pos_hint={"center_x": 0.5, "center_y": 0.28},
            radius=[15, 15, 15, 15],
            padding=[10, 10, 10, 10],
        )

        # ScrollView for classes
        scroll_view = ScrollView(size_hint=(1, 1))
        card_user_class.add_widget(scroll_view)

        self.dialog = None

        layout.add_widget(card_user_class)

        # Add the main layout to the screen
        self.add_widget(layout)
<<<<<<< Updated upstream

    # def create_graph(self):
    #     # Example data for the graph
    #     x = [1, 2, 3, 4, 5]
    #     y = [5, 3, 7, 10, 2]
    #
    #     # Create a Matplotlib figure and axis
    #     fig, ax = plt.subplots()
    #     ax.plot(x, y, label="Sample Data", marker="o")
    #     ax.set_title("Performance Graph")
    #     ax.set_xlabel("Time")
    #     ax.set_ylabel("Score")
    #     ax.legend()
    #
    #     # Return the Kivy widget for the graph
    #     return FigureCanvasKivyAgg(fig)
=======
>>>>>>> Stashed changes
