import pyautogui
import random
import time

def main(args):
    print('Starting to move cursor randomly')
    screen_width, screen_height = pyautogui.size()  
    try:
        while True:
            
            x = random.randint(0, screen_width - 1)
            y = random.randint(0, screen_height - 1)
            
            pyautogui.moveTo(x, y, duration=1)  
            time.sleep(2)  
    except KeyboardInterrupt:
        print("Script terminated by user.")
