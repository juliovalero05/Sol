[app]
title = Sol
package.name = sol
package.domain = com.juliovalero.sol
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,json
version = 0.1
requirements = python3,kivy
orientation = portrait

[buildozer]
log_level = 2

[app:android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license_agreement = True
android.build_tools_version = 33.0.2
name: Build APK
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - name: Install deps
        run: |
          pip install buildozer cython
          sudo apt-get update && sudo apt-get install -y libffi-dev libssl-dev
          yes | $ANDROID_HOME/cmdline-tools/latest/bin/sdkmanager --licenses
          $ANDROID_HOME/cmdline-tools/latest/bin/sdkmanager --install "build-tools;33.0.2" "build-tools;37.0.0" "platforms;android-33" "platform-tools"
      - name: Build
        run: |
          buildozer android debug || true
          yes | $HOME/.buildozer/android/platform/android-sdk/cmdline-tools/latest/bin/sdkmanager --licenses || true
          $HOME/.buildozer/android/platform/android-sdk/cmdline-tools/latest/bin/sdkmanager --install "build-tools;33.0.2" "build-tools;37.0.0" || true
          buildozer android debug --verbose
      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: Sol-APK
          path: bin/*.apk
