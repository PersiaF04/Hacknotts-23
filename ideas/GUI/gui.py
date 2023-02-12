from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window
import kivy
from kivy.properties import ObjectProperty

kivy.require('1.0.8')
Window.maximize()

class SoundApp(MDApp):
   def build(self):
      global Screen_Manager
      Screen_Manager = ScreenManager()
      Screen_Manager.add_widget(Builder.load_file("TheSoundProject.kv"))
      Screen_Manager.add_widget(Builder.load_file("TSPLogin.kv"))
      Screen_Manager.add_widget(Builder.load_file("graph.kv"))
      return Screen_Manager

   def on_start(self):
      Clock.schedule_once(self.login, 1)
   
   def login(self, *args):
      Screen_Manager.current = "TSPLogin"

   def graph(self, *args):
      Screen_Manager.current = "graph"
      grid = ObjectProperty("grid")
      print(grid)
   
   def key_note():
      print("hello")
   
if __name__=='__main__':
   SoundApp().run()
































































