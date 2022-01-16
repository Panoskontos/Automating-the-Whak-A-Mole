from pyautogui import *
import time
import pyautogui
# win32api is faster that pyautogui
import win32api
import win32con
import keyboard
import numpy as np
import cv2


def click(x, y):
    win32api.SetCursorPos((x, y))
    # press down
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    # release
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# click(412, 535)
# pyautogui.displayMousePosition()

# y = 226 , 653
# x = 45 , 712

# method to find images
iml = pyautogui.screenshot(region=(45, 226, 675, 653))
iml.save(r"C:\Users\Panagiotis\Documents\Job\python\bot\s.png")

head = pyautogui.screenshot(region=(71, 265, 25, 30))
head.save(r"C:\Users\Panagiotis\Documents\Job\python\bot\t.png")


while keyboard.is_pressed('q') == False:
    if pyautogui.locateOnScreen('t.png', region=(125, 226, 675, 653), grayscale=True, confidence=0.8) != None:
        print('found him')

        time.sleep(0.1)
    else:
        print('searching . . ')
        time.sleep(0.1)

"""
searching for a way to click the center of the image you find
"""
# location = pyautogui.locateCenterOnScreen('t.png', region=(
#     125, 226, 675, 653), grayscale=True, confidence=0.8)
# location = location.center(location)
# click(location.x, location.y)
