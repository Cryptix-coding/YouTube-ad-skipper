import numpy as np
import cv2
import pyautogui
import time
import keyboard

templates = [   #reading of the Ad screenshot(s)
    cv2.imread("Ad1.png", 0),
    cv2.imread("Ad2.png", 0),
    cv2.imread("Ad3.png", 0),
    cv2.imread("Ad4.png", 0)
]

threshold = 0.7     #Percentage used to determine whether the object found is also the object searched for

def find_button(sh, template):
    res = cv2.matchTemplate(sh, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    if loc[0].size != 0:
        pyautogui.click(list(zip(*loc[::-1]))[0])
        return True
    return False

print("press x for 3 seconds to stop the programm")

while True:
    if keyboard.is_pressed('x'):
        print("Unterbrechen")
        break
    else:
        time.sleep(0.5)
        sh = np.asarray(pyautogui.screenshot().convert(mode = "L"))
        for template in templates:
            if find_button(sh, template):
                break