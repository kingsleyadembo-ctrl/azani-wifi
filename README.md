name: Build APK
on:
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install Flet
        run: pip install flet[all]
      
      - name: Build APK
        run: flet build apk --verbose
      
      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: azani-wifi-apk
          path: build/app/outputs/flutter-apk/app-release.apk
