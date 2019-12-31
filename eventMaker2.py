import os
import time
import re
import sys
import datetime
from pynput import mouse
from pynput.keyboard import Key, Listener
inc=1
from pynput import keyboard

class DoneException(Exception):
   """Base class for other exceptions"""
   pass

print("Argument List: ", str(sys.argv))
filename = "./events/" + sys.argv[1] + ".txt"
if os.path.exists(filename):
  os.remove(filename)
f = open(filename, "a")


def on_keyboard(key):
    isMac = sys.platform == 'darwin'
    #for mac os
    if (key==keyboard.Key.f8):
        print('keyboard#click#{}'.format(key))
        key_listener.stop()
        listener.stop()
        return False
    if isMac:
        try:
            print('keyboard#click#{}'.format(key.char))
            f.write('keyboard#click#{}\n'.format(key.char))
        except AttributeError:
            print('keyboard#click#{}'.format(key))
            f.write('keyboard#click#{}\n'.format(key))
    else:
        if (key==keyboard.Key.f8):
            print('keyboard#click#{}'.format(key))
            key_listener.stop()
            listener.stop()
            return False
        print('keyboard#click#{}'.format(key))
        f.write('keyboard#click#{}\n'.format(key))


key_listener = keyboard.Listener(on_release=on_keyboard)
key_listener.start()

def on_move(x, y):
    print('mouse#move#{0}'.format(
        (x, y)))
    f.write('mouse#move#{0}\n'.format(
        (x, y)))

def on_click(x, y, button, pressed):
    if button == mouse.Button.left:
        print ('mouse#clickleft#{0}\n'.format(
        (x, y)))
        f.write ('mouse#clickleft#{0}\n'.format(
        (x, y)))

    if button == mouse.Button.right:
        print('mouse#clickright#{0}\n'.format(
        (x, y)))
        f.write('mouse#clickright#{0}\n'.format(
        (x, y)))

    if button == mouse.Button.middle:
        print('mouse#clickmiddle#{0}\n'.format(
        (x, y)))
        f.write('mouse#clickmiddle#{0}\n'.format(
        (x, y)))

def on_scroll(x, y, dx, dy):
    print('mouse#scroll{0}#{1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))
    f.write('mouse#scroll{0}#{1}\n'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

with mouse.Listener(on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()
    while True:
        if not listener.running:
            # breaks out of the loop and closes the program
            f.close()
            break
