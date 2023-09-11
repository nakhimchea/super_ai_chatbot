import pyautogui

import time
for i in range(500):
    print("Running")
    pyautogui.click()

    time.sleep(500)

    pyautogui.press('tab')

    time.sleep(500)
    pyautogui.press('tab')
    time.sleep(100)

    pyautogui.press('enter')
