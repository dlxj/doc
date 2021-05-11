
# windows
# pip install pygetwindow==0.0.1
# pip install pyautogui===0.9.0

import pyautogui as pygui
import time

print( pygui.position() )

while True:
    pygui.moveTo(555,555,15)
    # time.sleep(10)
    pygui.moveTo(333,333,15)
    # time.sleep(10)
    pygui.moveTo(666,666,15)
    # time.sleep(10)

    pygui.moveTo(1711,184,15) # win10 colab busy button
    pygui.click(x=1711, y=184, clicks=2, interval=10, button='left') # # win10 colab busy button
    
