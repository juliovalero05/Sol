[app]
title = Sol
package.name = sol
package.domain = com.juliovalero.sol
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/25.2.9519653
android.accept_sdk_license_agreements = True
android.ant_path = /usr/bin/ant
android.build_tools_version = 33.0.2
