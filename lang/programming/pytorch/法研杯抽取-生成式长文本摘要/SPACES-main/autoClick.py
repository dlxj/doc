
# 防止Colab 断线

# windows
# pip install pygetwindow==0.0.1
# pip install pyautogui===0.9.0

import pyautogui as pygui
import time

print( pygui.position() )

while True:
    pygui.moveTo(555,555,10)
    # time.sleep(10)
    pygui.moveTo(333,333,10)
    # time.sleep(10)
    pygui.moveTo(666,666,10)
    # time.sleep(10)