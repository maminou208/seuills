from turtle import screensize
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton
from kivy.core.window import Window 

Window.size = (400,630)

class DemoAPP(MDApp):
    def build(self):
        self.title = 'Seuils'
        self.theme_cls.primary_palette ="BlueGray"
        self.theme_cls.theme_style="Dark"
        return Builder.load_file('ui.kv')

if __name__=="__main__":
    DemoAPP().run()
