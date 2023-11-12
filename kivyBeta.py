from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.label import MDLabel
from kivy.metrics import dp

class Screen1(Screen):
    pass

class Manager(ScreenManager):
    pass

class Screen2(Screen):
    def __init__(self, **kwargs):
        super(Screen2, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation="vertical")
        self.label = MDLabel(text="Screen 2")
        self.layout.add_widget(self.label)
        self.add_md_table()
        self.add_widget(self.layout)
    
    def add_md_table(self):
        # Create an instance of MDDataTable and add it to the layout
        table = MDDataTable(column_data=[("Column 1", dp(30)), ("Column 2", dp(30))],
                            row_data=[("Row 1 Data 1", "Row 1 Data 2"),
                                      ("Row 2 Data 1", "Row 2 Data 2")])
        self.layout.add_widget(table)

class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Indigo"
        
        return Builder.load_file("app.kv")

if __name__ == "__kivyBeta__":
    MyApp().run()
