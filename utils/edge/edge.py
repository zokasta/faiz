import pyautogui
import random
import time


def switch_window():
    pyautogui.hotkey('alt','tab')

word_list = [
    "apple", "banana", "cherry", "date", "elephant", "fish", "grape", "honey", "ice", "jungle",
    "car", "dog", "cat", "mountain", "tree", "computer", "phone", "coffee", "cake", "movie",
    "music", "holiday", "food", "weather", "beach", "sunshine", "vacation", "chocolate", "sports",
    "fashion", "travel", "books", "art", "science", "history", "technology", "health", "fitness",
    "shopping", "coffee", "restaurant", "game", "exercise", "yoga", "gym", "tea", "family", "home",
    "love", "friends", "relationship", "adventure", "party", "event", "workout", "nature", "flowers",
    "birds", "stars", "ocean", "mountains", "fitness", "business", "finance", "education", "career"
]

def perform_actions():
    pyautogui.hotkey("ctrl", "t")
    time.sleep(1)

    word1 = random.choice(word_list)
    word2 = random.choice(word_list)

    pyautogui.typewrite(f"{word1} {word2}")
    time.sleep(1)

    pyautogui.press("enter")
    print(f"Typed words: {word1} {word2} and pressed Enter.")


def perform_actions_mobile():
    pyautogui.hotkey("ctrl", "t")
    time.sleep(1)
    pyautogui.hotkey("ctrl", "l")
    time.sleep(1)

    word1 = random.choice(word_list)
    word2 = random.choice(word_list)

    pyautogui.typewrite(f"{word1} {word2}")
    time.sleep(1)

    pyautogui.press("enter")
    print(f"Typed words: {word1} {word2} and pressed Enter.")



def edge_main_func(args):
    count = int(args[0]) if args and str(args[0]).isdigit() else 20
    
    switch_window()
    
    iterations = count  
    
    for i in range(iterations):
        perform_actions()
        print(f"Iteration {i + 1}/{iterations} completed.")
        time.sleep(4.5)
        pyautogui.hotkey("ctrl", "w")
    
    print("✅ Process completed!")

    
    switch_window()
    
    iterations = count  
    
    for i in range(iterations):
        perform_actions()
        print(f"Iteration {i + 1}/{iterations} completed.")
        time.sleep(4.5)
        pyautogui.hotkey("ctrl", "w")
    print("Process completed!")

    
def edgeMobileFun(args):
    count = int(args[0]) if args and str(args[0]).isdigit() else 20
    switch_window()
    print('this is edge mobile')
    iterations = count

    for i in range(iterations):
        perform_actions_mobile()
        print(f"Iteration {i + 1}/{iterations} completed.")

        time.sleep(5)
        pyautogui.hotkey("ctrl", "w")
    print("Process completed!")
