from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

class WindowManager(ScreenManager):
    pass

class LoginWindow(Screen):
    pass

class CalendarWindow(Screen):
    pass

kv = Builder.load_file("scapp.kv")
class Scapp(App):
    def build(self):
        return kv
 
if __name__ == "__main__":
    Scapp().run()