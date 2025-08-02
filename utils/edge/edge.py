import pyautogui
import random
import time

def switch_window():
    pyautogui.hotkey('alt', 'tab')

word_list = [
    "apple", "banana", "cherry", "date", "elephant", "fish", "grape", "honey", "ice", "jungle",
    "car", "dog", "cat", "mountain", "tree", "computer", "phone", "coffee", "cake", "movie",
    "music", "holiday", "food", "weather", "beach", "sunshine", "vacation", "chocolate", "sports",
    "fashion", "travel", "books", "art", "science", "history", "technology", "health", "fitness",
    "shopping", "coffee", "restaurant", "game", "exercise", "yoga", "gym", "tea", "family", "home",
    "love", "friends", "relationship", "adventure", "party", "event", "workout", "nature", "flowers",
    "birds", "stars", "ocean", "mountains", "fitness", "business", "finance", "education", "career"
]

def type_like_human(text):
    for char in text:
        pyautogui.typewrite(char)
        time.sleep(random.uniform(0.05, 0.2))  # Vary typing speed

def perform_actions():
    pyautogui.hotkey("ctrl", "t")
    time.sleep(random.uniform(0.5, 1.5))

    num_words = random.choice([2, 3])
    words = " ".join(random.sample(word_list, num_words))

    type_like_human(words)
    time.sleep(random.uniform(0.5, 1.2))  # Pause before pressing enter

    pyautogui.press("enter")
    print(f"Typed words: {words} and pressed Enter.")

def perform_actions_mobile():
    pyautogui.hotkey("ctrl", "t")
    time.sleep(random.uniform(0.5, 1.5))
    pyautogui.hotkey("ctrl", "l")
    time.sleep(random.uniform(0.3, 0.8))

    num_words = random.choice([2, 3])
    words = " ".join(random.sample(word_list, num_words))

    type_like_human(words)
    time.sleep(random.uniform(0.5, 1.2))

    pyautogui.press("enter")
    print(f"Typed words: {words} and pressed Enter.")

def edge_main_func(args):
    count = int(args[0]) if args and str(args[0]).isdigit() else 20
    
    switch_window()
    iterations = count  
    
    for i in range(iterations):
        perform_actions()
        print(f"Iteration {i + 1}/{iterations} completed.")
        time.sleep(random.uniform(3.5, 5.5))
        pyautogui.hotkey("ctrl", "w")
    
    print("✅ Process completed!")

def edgeMobileFun(args):
    count = int(args[0]) if args and str(args[0]).isdigit() else 20
    switch_window()
    print('This is edge mobile')
    iterations = count

    for i in range(iterations):
        perform_actions_mobile()
        print(f"Iteration {i + 1}/{iterations} completed.")

        time.sleep(random.uniform(4, 6))
        pyautogui.hotkey("ctrl", "w")
    print("✅ Mobile process completed!")
