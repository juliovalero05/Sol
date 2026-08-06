from kivy.app import App
from kivy.uix.label import Label

class SolApp(App):
    def build(self):
        return Label(text="Hola Sol, si ves esto ya jalo!")

SolApp().run()
