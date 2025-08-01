from kivy.app import App
from  kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
import kivy
kivy.require("1.9.1")

class MyRoot(BoxLayout):
    def __init__(self):
        super(MyRoot, self).__init__()
    def backspace(self):
        self.cal_field.text = self.cal_field.text[:-1]
    def cal_sym(self, sym):

    
        self.cal_field.text +=sym

    def clear(self):
        self.cal_field.text = ""
    def equal(self):
        try:
            self.cal_field.text = str(eval(self.cal_field.text))
        except:
            self.cal_field.text = "Invalid Input"
            self.clear()

class AndriodCal(App):
    def build(self):
        return MyRoot()
    
Andcal = AndriodCal()
Andcal.run()