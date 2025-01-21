from kivymd.uix.screen import MDScreen
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.uix.widget import Widget
from math import pi 

class PieChart(Widget):
    def __init__(self, data=None, **kwargs):
        super().__init__(**kwargs)
        self.data = data or {"Complete": 30, "Incomplete": 70}  # Default data
        self.colors = [(0, 0.6, 0, 1), (0.8, 0.8, 0.8, 1)]  # Green and Gray
        
        with self.canvas:
            self.bind(pos=self.update_pie, size=self.update_pie)
            
    def update_pie(self, *args):
        self.canvas.clear()
        center_x = self.center_x
        center_y = self.center_y
        radius = min(self.width, self.height) * 0.4
        
        total = sum(self.data.values())
        start_angle = 0
        
        for i, (key, value) in enumerate(self.data.items()):
            with self.canvas:
                Color(*self.colors[i])
                angle = 2 * pi * (value / total)
                Ellipse(
                    pos=(center_x - radius, center_y - radius),
                    size=(radius * 2, radius * 2),
                    angle_start=start_angle * 360 / (2 * pi),
                    angle_end=(start_angle + angle) * 360 / (2 * pi)
                )
            start_angle += angle

class CourseDetail(MDScreen):
    def __init__(self, course_code="", course_name="", **kwargs):
        super().__init__(**kwargs)
        
        layout = FloatLayout(size_hint=(1, 1))
        
        # Background
        background = Image(
            source="assets/background.png",
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(1, 1),
            pos_hint={"x": 0, "y": 0},
        )
        layout.add_widget(background)
        
        # Header Card with white background
        header_card = MDCard(
            orientation="vertical",
            size_hint=(1, None),
            height="70dp",
            pos_hint={"top": 1},
            radius=[0, 0, 0, 0],
            padding=0,
            elevation=2,
        )
        
        # Header with back button and course title
        header = BoxLayout(
            orientation='horizontal',
            size_hint=(1, 1),
            padding=[10, 10, 10, 10],
        )
        
        back_button = MDIconButton(
            icon="arrow-left",
            theme_text_color="Custom",
            text_color=(0, 0.6, 0, 1),
            on_release=self.go_back
        )
        
        title = MDLabel(
            text=f"{course_code} - {course_name}",
            theme_text_color="Custom",
            text_color=(0, 0.6, 0, 1),
            font_style="H6",
            bold=True
        )
        
        header.add_widget(back_button)
        header.add_widget(title)
        header_card.add_widget(header)
        
        # Graph Card
        graph_card = MDCard(
            orientation="vertical",
            size_hint=(0.9, 0.3),
            pos_hint={"center_x": 0.5, "center_y": 0.7},
            radius=[15, 15, 15, 15],
            padding=[20, 20, 20, 20],
        )
        
        graph_label = MDLabel(
            text="Progress Graph",
            theme_text_color="Custom",
            text_color=(0, 0.6, 0, 1),
            font_style="H6",
            bold=True,
            size_hint_y=None,
            height="30dp"
        )
        
        # Create pie chart container
        chart_container = BoxLayout(
            orientation='horizontal',
            size_hint=(1, 1)
        )
        
        # Add pie chart
        pie_chart = PieChart(
            size_hint=(0.5, 1),
            data={"Complete": 30, "Incomplete": 70}  # Dummy data
        )
        
        # Add legend
        legend_layout = BoxLayout(
            orientation='vertical',
            size_hint=(0.4, 1),
            padding=[10, 20, 10, 20],
            spacing=10
        )
        
        for label, value in pie_chart.data.items():
            legend_item = BoxLayout(
                orientation='horizontal',
                size_hint_y=None,
                height="30dp",
                spacing=5
            )
            
            color_box = Widget(size_hint=(None, None), size=(20, 20))
            color_idx = 0 if label == "Complete" else 1
            with color_box.canvas:
                Color(*pie_chart.colors[color_idx])
                Rectangle(pos=color_box.pos, size=color_box.size)
            
            legend_item.add_widget(color_box)
            legend_item.add_widget(
                MDLabel(
                    text=f"{label}: {value}%",
                    theme_text_color="Custom",
                    text_color=(0, 0, 0, 1)
                )
            )
            legend_layout.add_widget(legend_item)
        
        chart_container.add_widget(pie_chart)
        chart_container.add_widget(legend_layout)
        
        graph_card.add_widget(graph_label)
        graph_card.add_widget(chart_container)
        
        # Activities Card (rest remains the same)
        activities_card = MDCard(
            orientation="vertical",
            size_hint=(0.9, 0.4),
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            radius=[15, 15, 15, 15],
            padding=[20, 20, 20, 20],
        )
        
        activities_label = MDLabel(
            text="Activities",
            theme_text_color="Custom",
            text_color=(0, 0.6, 0, 1),
            font_style="H6",
            bold=True,
            size_hint_y=None,
            height="30dp"
        )
        
        scroll_view = ScrollView(size_hint=(1, 1))
        activities_layout = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            spacing="10dp"
        )
        activities_layout.bind(minimum_height=activities_layout.setter('height'))
        
        # Dummy activities
        activities = [
            {"name": "Quiz 1: Introduction", "done": True},
            {"name": "Assignment 1: Basic Concepts", "done": False},
            {"name": "Quiz 2: Advanced Topics", "done": False},
            {"name": "Project Milestone 1", "done": False},
            {"name": "Quiz 3: Final Review", "done": False},
        ]
        
        for activity in activities:
            activity_item = BoxLayout(
                orientation='horizontal',
                size_hint_y=None,
                height="40dp",
                spacing="10dp"
            )
            
            checkbox = MDIconButton(
                icon="checkbox-marked-circle" if activity["done"] else "checkbox-blank-circle-outline",
                theme_text_color="Custom",
                text_color=(0, 0.6, 0, 1),
                size_hint=(None, None),
                size=("24dp", "24dp")
            )
            
            activity_label = MDLabel(
                text=activity["name"],
                theme_text_color="Custom",
                text_color=(0, 0, 0, 1)
            )
            
            activity_item.add_widget(checkbox)
            activity_item.add_widget(activity_label)
            activities_layout.add_widget(activity_item)
        
        scroll_view.add_widget(activities_layout)
        activities_card.add_widget(activities_label)
        activities_card.add_widget(scroll_view)
        
        # Add all widgets to main layout
        layout.add_widget(header_card)
        layout.add_widget(graph_card)
        layout.add_widget(activities_card)
        
        self.add_widget(layout)
    
    def go_back(self, instance):
        self.manager.current = "Home_Student"

class CourseDetail(MDScreen):
    def __init__(self, course_code="", course_name="", **kwargs):
        super().__init__(**kwargs)
        
        layout = FloatLayout(size_hint=(1, 1))
        
        # Background
        background = Image(
            source="assets/background.png",
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(1, 1),
            pos_hint={"x": 0, "y": 0},
        )
        layout.add_widget(background)
        
        # Header Card with white background
        header_card = MDCard(
            orientation="vertical",
            size_hint=(1, None),
            height="70dp",
            pos_hint={"top": 1},
            radius=[0, 0, 0, 0],
            padding=0,
            elevation=2,
        )
        
        # Header with back button and course title
        header = BoxLayout(
            orientation='horizontal',
            size_hint=(1, 1),
            padding=[10, 10, 10, 10],
        )
        
        back_button = MDIconButton(
            icon="arrow-left",
            theme_text_color="Custom",
            text_color=(0, 0.6, 0, 1),
            on_release=self.go_back
        )
        
        title = MDLabel(
            text=f"{course_code} - {course_name}",
            theme_text_color="Custom",
            text_color=(0, 0.6, 0, 1),
            font_style="H6",
            bold=True
        )
        
        header.add_widget(back_button)
        header.add_widget(title)
        header_card.add_widget(header)
        
        # Graph Card
        graph_card = MDCard(
            orientation="vertical",
            size_hint=(0.9, 0.3),
            pos_hint={"center_x": 0.5, "center_y": 0.7},
            radius=[15, 15, 15, 15],
            padding=[20, 20, 20, 20],
        )
        
        graph_label = MDLabel(
            text="Progress Graph",
            theme_text_color="Custom",
            text_color=(0, 0.6, 0, 1),
            font_style="H6",
            bold=True,
            size_hint_y=None,
            height="30dp"
        )
        
        # Create pie chart container
        chart_container = BoxLayout(
            orientation='horizontal',
            size_hint=(1, 1)
        )
        
        # Add pie chart
        pie_chart = PieChart(
            size_hint=(0.5, 1),  # Smaller size
            data={"Complete": 30, "Incomplete": 70}  # Dummy data
        )
        
        # Add legend
        legend_layout = BoxLayout(
            orientation='vertical',
            size_hint=(0.5, 1),  # Smaller size
            padding=[10, 20, 10, 20],
            spacing=10
        )
        
        for label, value in pie_chart.data.items():
            legend_item = BoxLayout(
                orientation='horizontal',
                size_hint_y=None,
                height="30dp",
                spacing=5
            )
            
            color_box = Widget(size_hint=(None, None), size=(20, 20))
            color_idx = 0 if label == "Complete" else 1
            with color_box.canvas:
                Color(*pie_chart.colors[color_idx])
                Rectangle(pos=color_box.pos, size=color_box.size)
            
            legend_item.add_widget(color_box)
            legend_item.add_widget(
                MDLabel(
                    text=f"{label}: {value}%",
                    theme_text_color="Custom",
                    text_color=(0, 0, 0, 1)
                )
            )
            legend_layout.add_widget(legend_item)
        
        chart_container.add_widget(pie_chart)
        chart_container.add_widget(legend_layout)
        
        graph_card.add_widget(graph_label)
        graph_card.add_widget(chart_container)
        
        activities_card = MDCard(
            orientation="vertical",
            size_hint=(0.9, 0.3),  # Adjusted to smaller size
            pos_hint={"center_x": 0.5, "center_y": 0.3},  # Adjusted position
            radius=[15, 15, 15, 15],
            padding=[20, 20, 20, 20],
        )
        
        activities_label = MDLabel(
            text="Activities",
            theme_text_color="Custom",
            text_color=(0, 0.6, 0, 1),
            font_style="H6",
            bold=True,
            size_hint_y=None,
            height="30dp"
        )
        
        scroll_view = ScrollView(size_hint=(1, 1))
        activities_layout = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            spacing="10dp"
        )
        activities_layout.bind(minimum_height=activities_layout.setter('height'))

        activities = [
            {"name": "Quiz 1: Introduction", "done": True},
            {"name": "Assignment 1: Basic Concepts", "done": False},
            {"name": "Quiz 2: Advanced Topics", "done": False},
            {"name": "Project Milestone 1", "done": False},
            {"name": "Quiz 3: Final Review", "done": False},
        ]
        
        for activity in activities:
            activity_item = BoxLayout(
                orientation='horizontal',
                size_hint_y=None,
                height="40dp",
                spacing="10dp"
            )
            
            checkbox = MDIconButton(
                icon="checkbox-marked-circle" if activity["done"] else "checkbox-blank-circle-outline",
                theme_text_color="Custom",
                text_color=(0, 0.6, 0, 1),
                size_hint=(None, None),
                size=("24dp", "24dp")
            )
            
            activity_label = MDLabel(
                text=activity["name"],
                theme_text_color="Custom",
                text_color=(0, 0, 0, 1)
            )
            
            activity_item.add_widget(checkbox)
            activity_item.add_widget(activity_label)
            activities_layout.add_widget(activity_item)
        
        scroll_view.add_widget(activities_layout)
        activities_card.add_widget(activities_label)
        activities_card.add_widget(scroll_view)
        
        # Add all widgets to main layout
        layout.add_widget(header_card)
        layout.add_widget(graph_card)
        layout.add_widget(activities_card)
        
        self.add_widget(layout)
    
    def go_back(self, instance):
        self.manager.current = "Home_Student"
