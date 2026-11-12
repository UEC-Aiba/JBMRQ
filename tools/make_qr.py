# -*- coding: utf-8 -*-
"""公開したページのアドレスから，スライドに貼るQRコード（PNG）を作る。
使い方：
  pip install "qrcode[pil]"
  python make_qr.py https://（アカウント名）.github.io/（リポジトリ名）/
→ qr.png ができる（スライドに貼る）。"""
import sys, qrcode
url = sys.argv[1] if len(sys.argv) > 1 else input("公開したページのアドレス：").strip()
img = qrcode.make(url, error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=12, border=4)
img.save("qr.png"); print("qr.png を作りました：", url)
