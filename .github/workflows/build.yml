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
      - name: Fix SDK
        run: |
          SDK="$ANDROID_HOME/cmdline-tools/latest/bin/sdkmanager"
          echo "y" | $SDK --install "build-tools;33.0.2" "platforms;android-33" > /dev/null
          echo "y" | $SDK "build-tools;33.0.2" > /dev/null || true
      - name: Install deps
        run: |
          pip install buildozer cython
          sudo apt-get update && sudo apt-get install -y libffi-dev libssl-dev
      - name: Build
        run: buildozer android debug --verbose
      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: Sol-APK
          path: bin/*.apk
