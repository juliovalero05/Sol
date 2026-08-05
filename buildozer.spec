[app]
title = JARVIS Invisible
package.name = jarvisinvisible
package.domain = com.jarvis.invisible
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = hostpython3==3.10.13,python3==3.10.13,kivy==2.3.0,plyer,requests,android,pyjnius
orientation = portrait
fullscreen = 0
android.permissions = CAMERA,RECORD_AUDIO,INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreements = True
android.ant = auto

[buildozer]
log_level = 2
