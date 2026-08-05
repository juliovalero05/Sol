[app]
title = Sol
package.name = sol
package.domain = com.juliovalero.sol
source.dir =./Sol
version = 1.0
requirements = python3,kivy,Pillow,plyer,requests,android
orientation = portrait
android.permissions = INTERNET,CAMERA,RECORD_AUDIO
android.api = 33
android.minapi = 21
android.ndk = 25b
android.build_tools_version = 33.0.1
android.accept_sdk_license_agreements = True
android.archs = arm64-v8a, armeabi-v7a
p4a.branch = master

[buildozer]
log_level = 1
