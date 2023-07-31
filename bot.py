import time
import random
import pyautogui

stopFlag = False  # Global flag to stop loops gracefully

def bot_move(interval, x, y, times):
    try:
        i = 0
        while not stopFlag and i<times:
            pyautogui.moveTo(x, y)
            time.sleep(interval)
            print("Moved the mouse pointer without any errors")
            i = i + 1
    except KeyboardInterrupt:
        print("stopFlag detected")

def bot_random(interval, res_x, res_y, times):
    try:
        i = 0
        while not stopFlag and i<times:
            rand_x = random.randint(0, res_x - 1)
            rand_y = random.randint(0, res_y - 1)
            pyautogui.moveTo(rand_x, rand_y)
            time.sleep(interval)
            print("Moved the mouse pointer to a random position without any errors")
            i = i + 1
    except KeyboardInterrupt:
        print("stopFlag detected")

def click_mouse(button):
    pyautogui.click(button=button)
    print("Clicked with the selected button without any errors")

def get_bot_position(times):
    try:
        i = 0
        while not stopFlag and i<times:
            x, y = pyautogui.position()
            print(f"Pointer position: x={x}, y={y}", end="\r", flush=True)
            i = i + 1
    except KeyboardInterrupt:
        print("stopFlag detected")

def freeze(time_sec):
    time.sleep(time_sec)