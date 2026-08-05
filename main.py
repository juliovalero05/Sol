from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
try:
    from plyer import tts
except:
    pass
class JarvisApp(App):
    def build(self):
        self.root = Label(text="JARVIS INVISIBLE\nDi: Oye Jarvis")
        Clock.schedule_once(self.hablar, 1)
        return self.root
    def hablar(self, dt):
        try:
            tts.speak("Jarvis invisible activado")
        except:
            pass
JarvisApp().run()
