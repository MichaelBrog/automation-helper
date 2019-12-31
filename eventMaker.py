import sys
import os
from pynput import mouse

print("Argument List: ", str(sys.argv))
filename = "./events/" + sys.argv[1] + ".txt"
if os.path.exists(filename):
  os.remove(filename)
f = open(filename, "a")

def on_move(x, y):
    print('mouse#move#{0}'.format(
        (x, y)))
    f.write('mouse#move#{0}\n'.format(
        (x, y)))

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'mouse#click' if pressed else 'Released',
        (x, y)))
    f.write('{0}#{1}\n'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        # Stop listener
        return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))
    f.write('mouse#scroll{0}#{1}\n'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

# Collect events until released
with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()



import os
import time
import re
from pynput import mouse
from pynput.keyboard import Key, Listener
#f=open('maniac1.txt','a')

inc=1
#f.write('<mouse_new>\n')
from pynput import keyboard

def on_functionf8(key):
    if (key==keyboard.Key.f8):
        print('f8 is pressed')


key_listener = keyboard.Listener(on_release=on_functionf8)
key_listener.start()


def on_click(x, y, button, pressed):
    f=open('maniac1.txt','a')
    if button == mouse.Button.left:
        print ('Left')

    if button == mouse.Button.right:
        key_listener.stop()
        print ('right')
        #f.write('right\n')
    if button == mouse.Button.middle:
        print ('middle')
        #f.write('middle\n')

with mouse.Listener(on_click=on_click) as listener:
    try:
        listener.join()
    except MyException as e:
        print('Done'.format(e.args[0]))
