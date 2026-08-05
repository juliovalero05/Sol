from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.camera import Camera
from plyer import tts
import requests

# Permisos automaticos
try:
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.CAMERA, Permission.RECORD_AUDIO, Permission.INTERNET])
except:
    pass

try:
    from plyer import stt
    TIENE_OIDOS = True
except:
    TIENE_OIDOS = False

Window.clearcolor = (0, 0, 0, 1)

KV = '''
<SolFinal>:
    orientation: 'vertical'
    FloatLayout:
        Camera:
            id: cam
            index: 0
            resolution: (1280, 720)
            play: True
            size_hint: 1, 1
            pos_hint: {'center_x': 
