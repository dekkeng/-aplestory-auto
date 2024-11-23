import time

import keyboard
import pyautogui

print("Press s to get your mouse position!")
while True:
    pos = pyautogui.position()
    if keyboard.is_pressed('s'):
        im1 = pyautogui.screenshot(region=(pos.x,pos.y,150,100))
        print(pos)