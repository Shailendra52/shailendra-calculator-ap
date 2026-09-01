name: Build AAB
on: [push]
jobs:
  build:
    runs-on: ubuntu-20.04
    steps:
      - uses: actions/checkout@v2
      - name: Build AAB
        uses: digreatbrian/buildozer-action@v2
        with:
          buildozer-cmd: buildozer android release
      - name: Upload AAB
        uses: actions/upload-artifact@v3
        with:
          name: aab-file
          path: bin/*.aab
