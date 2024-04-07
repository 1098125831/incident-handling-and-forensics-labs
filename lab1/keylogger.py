from pynput.keyboard import Key, Listener

def on_press(key):
    try:
        print(f'Alphanumeric key pressed: {key.char}')
    except AttributeError:
        print(f'Special key pressed: {key}')

def on_release(key):
    print(f'Key released: {key}')

# Collecting events until manually stopped
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
