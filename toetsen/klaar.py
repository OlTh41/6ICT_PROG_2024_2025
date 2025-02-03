from pynput import keyboard
import time

def on_press(key):
    return False

def main():
    # Disable the keyboard listener
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    print("The keyboard is disabled for 5 seconds.")
    time.sleep(5)

    # Enable the keyboard listener
    listener.stop()

    print("The keyboard is enabled again.")

if __name__ == "__main__":
    main()