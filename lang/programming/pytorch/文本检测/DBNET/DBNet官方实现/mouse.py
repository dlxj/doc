from time import sleep
import pyautogui, sys
#import keyboard

print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)

        pyautogui.moveTo(184, 941, 30)
        pyautogui.moveTo(1685, 121, 30)
        #if keyboard.is_pressed('b'):
            #break


except KeyboardInterrupt:
    print('\n')


"""
python3 -m pip install pyautogui
pip install keyboard
"""