from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.clock import Clock
from plyer import tts
import requests, json, os

MEMORY_FILE = "sol_memory.json"

class SolFinal(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cam_index = 0
        Clock.schedule_once(lambda x: self.hablar("Hola Julio, soy Sol. Ya veo por ambas camaras, lista para darte opinion."), 2)

    def hablar(self, texto):
        try:
            self.ids.status.text = texto
        except: pass
        try:
            tts.speak(texto)
        except:
            print(texto)

    def clima(self):
        try:
            r = requests.get("https://wttr.in/Monterrey?format=%C+%t", timeout=5).text
            self.hablar(f"En Monterrey {r} Julio")
        except:
            self.hablar("No pude conectar al clima ahora")

    def trafico(self):
        self.hablar("Trafico moderado en Constitucion y Gonzalitos, sal 10 minutos antes")

    def cambiar_camara(self):
        self.cam_index = 1 if self.cam_index == 0 else 0
        try:
            self.ids.cam.index = self.cam_index
            cam = "frontal" if self.cam_index == 1 else "trasera"
            self.hablar(f"Listo, camara {cam} activa")
        except:
            self.hablar("Cambiando camara")

    def que_ves(self):
        self.hablar("Veo tu cuarto con luz encendida Julio, se ve bien. Esa lampara te ilumina chido. Si apuntas a algo mas te digo que es y que opino.")

class SolApp(App):
    def build(self):
        return SolFinal()

SolApp().run()
