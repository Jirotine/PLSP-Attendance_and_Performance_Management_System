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
from supabase_manager import get_supabase_client
from session_manager import SessionManager
from datetime import datetime

class PieChart(Widget):
    def __init__(self, data=None, **kwargs):
        super().__init__(**kwargs)
        self.data = data or {"Complete": 0, "Incomplete": 100}
        self.colors = [(0, 0.6, 0, 1), (0.8, 0.8, 0.8, 1)]
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
    def __init__(self, course_code="", course_name="", class_id=0, **kwargs):
        super().__init__(**kwargs)
        self.course_code = course_code
        self.course_name = course_name
        self.class_id = class_id
        self.client = get_supabase_client()
        self.session = SessionManager()
        self.student_id = self.session.get('student_id')
        
        # Fetch activities data from Supabase
        self.activities_data = self.fetch_activities_data()
        self.progress_data = self.calculate_progress()
        
        self.setup_ui()
    
    def fetch_activities_data(self):
        try:
            # Fetch all activities for this class
            activities_response = self.client.table('activity_table')\
                .select('*')\
                .eq('class_id', self.class_id)\
                .execute()
            
            activities = activities_response.data
            
            # Fetch completed activities for this student
            completed_response = self.client.table('activity_student')\
                .select('activity_id')\
                .eq('student_id', self.student_id)\
                .execute()
            
            completed_activities = {item['activity_id'] for item in completed_response.data}
            
            # Combine the data
            activities_with_status = []
            for activity in activities:
                activities_with_status.append({
                    'activity_id': activity['activity_id'],
                    'name': activity['activity_name'],
                    'done': activity['activity_id'] in completed_activities,
                    'created_at': activity['created_at']
                })
            
            # Sort by creation date
            return sorted(activities_with_status, key=lambda x: x['created_at'])
        except Exception as e:
            print(f"Error fetching activities: {e}")
            return []
    
    def calculate_progress(self):
        if not self.activities_data:
            return {"Complete": 0, "Incomplete": 100}
        
        total = len(self.activities_data)
        completed = len([a for a in self.activities_data if a['done']])
        
        complete_percentage = round((completed / total) * 100) if total > 0 else 0
        incomplete_percentage = 100 - complete_percentage
        
        return {
            "Complete": complete_percentage,
            "Incomplete": incomplete_percentage
        }
    
    def toggle_activity(self, activity_id, checkbox):
        try:
            if checkbox.icon == "checkbox-blank-circle-outline":
                # Mark as complete
                self.client.table('activity_student').insert({
                    'activity_id': activity_id,
                    'student_id': self.student_id,
                    'checked_at': datetime.now().isoformat()
                }).execute()
                checkbox.icon = "checkbox-marked-circle"
            else:
                # Mark as incomplete
                self.client.table('activity_student')\
                    .delete()\
                    .eq('activity_id', activity_id)\
                    .eq('student_id', self.student_id)\
                    .execute()
                checkbox.icon = "checkbox-blank-circle-outline"
            
            # Update progress
            self.activities_data = self.fetch_activities_data()
            self.progress_data = self.calculate_progress()
            self.update_pie_chart()
            
        except Exception as e:
            print(f"Error toggling activity: {e}")
    
    def update_pie_chart(self):
        if hasattr(self, 'pie_chart'):
            self.pie_chart.data = self.progress_data
            self.pie_chart.update_pie()
            
            # Update legend labels
            for legend_item in self.legend_layout.children:
                label_widget = legend_item.children[0]  # The MDLabel is the first child
                if "Complete" in label_widget.text:
                    label_widget.text = f"Complete: {self.progress_data['Complete']}%"
                elif "Incomplete" in label_widget.text:
                    label_widget.text = f"Incomplete: {self.progress_data['Incomplete']}%"
    
    def setup_ui(self):
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
        
        # Header Card
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
            text=f"{self.course_name}",
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
        
        # Add pie chart with actual data
        self.pie_chart = PieChart(
            size_hint=(0.5, 1),
            data=self.progress_data
        )
        
        # Add legend
        self.legend_layout = BoxLayout(
            orientation='vertical',
            size_hint=(0.5, 1),
            padding=[10, 20, 10, 20],
            spacing=10
        )
        
        for label, value in self.progress_data.items():
            legend_item = BoxLayout(
                orientation='horizontal',
                size_hint_y=None,
                height="30dp",
                spacing=5
            )
            
            color_box = Widget(size_hint=(None, None), size=(20, 20))
            color_idx = 0 if label == "Complete" else 1
            with color_box.canvas:
                Color(*self.pie_chart.colors[color_idx])
                Rectangle(pos=color_box.pos, size=color_box.size)
            
            legend_item.add_widget(color_box)
            legend_item.add_widget(
                MDLabel(
                    text=f"{label}: {value}%",
                    theme_text_color="Custom",
                    text_color=(0, 0, 0, 1)
                )
            )
            self.legend_layout.add_widget(legend_item)
        
        chart_container.add_widget(self.pie_chart)
        chart_container.add_widget(self.legend_layout)
        
        graph_card.add_widget(graph_label)
        graph_card.add_widget(chart_container)
        
        # Activities Card
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
        
        # Add activities from Supabase data
        for activity in self.activities_data:
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
            
            checkbox.bind(
                on_release=lambda instance, aid=activity['activity_id'], 
                cb=checkbox: self.toggle_activity(aid, cb)
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
