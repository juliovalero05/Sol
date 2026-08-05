[app]
title = Sol
package.name = sol
package.domain = com.juliovalero.sol
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.0,Pillow,plyer,requests,android
orientation = portrait
android.permissions = INTERNET,CAMERA,RECORD_AUDIO
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk_path = /usr/local/lib/android/sdk
android.accept_sdk_license_agreements = True
android.archs = arm64-v8a, armeabi-v7a
p4a.branch = master

[buildozer]
log_level = 2
