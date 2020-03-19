import pymongo
import urllib.parse
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput

class Img(Image):
    pass

class FloatLay(FloatLayout):
    pass


class Login(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def reset(self):
        self.username.text = ""
        self.password.text = ""
    
    def login(self):
        self.username =  urllib.parse.quote(self.username.text) # passwordHell
        self.password =  urllib.parse.quote(self.password.text) # XR9lYeOp036C%@&@cQn*8z3BU4\

        try:
            client = pymongo.MongoClient(f"mongodb+srv://{self.username}:{self.password}@innoventory-vvoxp.azure.mongodb.net/test?retryWrites=true&w=majority")
            client.list_database_names()
            print("Connected")

        except pymongo.errors.OperationFailure:
            print("ruh-roh")


class Homepage(Screen):
    pass

class CreateAccount(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("Innoventory.kv")

winMan = WindowManager()
class main(App):
    def build(self):
        return kv

if __name__ == "__main__":
    main().run()