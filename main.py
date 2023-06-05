#Here is the code but  use it just for educational purpose!

import pynput
from pynput.keyboard import Key, Listener

def press(key):
    print(key)

def release(key):
    if key == Key.esc:
        return False    

with Listener(on_press=press, on_release=release) as listener:
    listener.join()
