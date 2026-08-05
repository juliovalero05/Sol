name: Build APK
on: push
jobs:
  build:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Delete broken build-tools 37
        run: |
          rm -rf /usr/local/lib/android/sdk/build-tools/37* || true
          mkdir -p $HOME/.android
          echo '### User Sources for Android SDK Manager' > $HOME/.android/repositories.cfg

      - name: Install deps
        run: |
          sudo apt-get update
          sudo apt-get install -y openjdk-17-jdk zip unzip libffi-dev libssl-dev
          pip install Cython==0.29.36 buildozer==1.5.0

      - name: Build
        run: buildozer android debug

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: Sol-APK
          path: bin/*.apk
