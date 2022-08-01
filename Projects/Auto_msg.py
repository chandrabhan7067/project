import pyautogui
import time

time.sleep(2)
for i in range(40):
    pyautogui.write('hello ')
    pyautogui.press('enter')