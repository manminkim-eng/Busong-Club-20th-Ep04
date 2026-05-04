#!/usr/bin/env python3
# EP4 index.html YouTube 링크 패치 스크립트
# 사용법: EP4 폴더에서 python3 patch_ep4.py 실행

import os

filename = 'index.html'
if not os.path.exists(filename):
    print(f'오류: {filename} 파일을 찾을 수 없습니다')
    exit(1)

with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

old = 'https://youtu.be/Oii_nDE8oGs'
new = 'https://youtu.be/IZfGYWsk6V4'

count = content.count(old)
if count == 0:
    print('이미 교체되었거나 링크를 찾지 못했습니다')
else:
    result = content.replace(old, new)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(result)
    print(f'완료: {count}곳 교체 — {old} → {new}')
