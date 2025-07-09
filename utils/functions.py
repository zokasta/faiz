import pyautogui
import random
import time


screen_width, screen_height = pyautogui.size()


def useMouse(x, y):
    pyautogui.moveTo(x, y, duration=0.5)
    time.sleep(random.uniform(0.1, 1.0))


def switchWindow():
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.5)


def keyclick():
    return pyautogui.hotkey()


def clickMouse(x=None, y=None):
    if x is not None and y is not None:
        pyautogui.click(x, y)
    else:
        pyautogui.click()
    time.sleep(0.5)


def holdClick(x=None, y=None, hold_time=1):
    if x is not None and y is not None:
        pyautogui.moveTo(x, y)
    pyautogui.mouseDown()
    time.sleep(hold_time)
    pyautogui.mouseUp()


def performActions():
    
    pyautogui.hotkey('shift', 'right')
    time.sleep(0.5)
    
    
    keyclick()
    time.sleep(0.5)
    
    
    pyautogui.press('down')
    time.sleep(0.5)


def main_loop(iterations=10):
    
    switchWindow()
    
    for i in range(iterations):
        print(f"Iteration {i+1}")
        performActions()
