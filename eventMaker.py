import os
import time
import re
import sys
import datetime
from logger import createLogger
def eventListener(fileLocation):
    from pynput import mouse
    from pynput import keyboard

    log = createLogger()
    filename = "./events/" + fileLocation
    if os.path.exists(filename):
        os.remove(filename)
    f = open(filename, "a")


    def on_keyboard(key):
        try:
            log.debug('{0}#keyboard#click#{1}'.format(datetime.datetime.utcnow(), key.char))
            f.write('{0}#keyboard#click#{1}\n'.format(datetime.datetime.utcnow(), key.char))
        except AttributeError:
            log.debug('{}keyboard#click#{}'.format(datetime.datetime.utcnow(), key))
            f.write('{}#keyboard#click#{}\n'.format(datetime.datetime.utcnow(), key))

        if (key==keyboard.Key.f8):
            k_listener.stop()
            m_listener.stop()
            return False

    def on_click(x, y, button, pressed):
        if button == mouse.Button.left:
            log.debug ('{0}#mouse#clickleft#{1}'.format(datetime.datetime.utcnow(),
            (x, y)))
            f.write ('{0}#mouse#clickleft#{1}\n'.format(datetime.datetime.utcnow(),
            (x, y)))

        if button == mouse.Button.right:
            log.debug('{0}#mouse#clickright#{1}'.format(datetime.datetime.utcnow(),
            (x, y)))
            f.write('{0}#mouse#clickright#{1}\n'.format(datetime.datetime.utcnow(),
            (x, y)))

        if button == mouse.Button.middle:
            log.debug('{0}#mouse#clickmiddle#{1}'.format(datetime.datetime.utcnow(),
            (x, y)))
            f.write('{0}#mouse#clickmiddle#{1}\n'.format(datetime.datetime.utcnow(),
            (x, y)))

    def on_scroll(x, y, dx, dy):
        log.debug('{0}#mouse#scroll{1}#{2}'.format(datetime.datetime.utcnow(),
            'down' if dy < 0 else 'up',
            (x, y)))
        f.write('{0}#mouse#scroll{1}#{2}\n'.format(datetime.datetime.utcnow(),
            'down' if dy < 0 else 'up',
            (x, y)))

    with keyboard.Listener(on_release=on_keyboard) as k_listener, mouse.Listener(on_click=on_click, on_scroll=on_scroll) as m_listener:
        k_listener.join()
        m_listener.join()
        while True:
            if not k_listener.running or not m_listener.running:
                # breaks out of the loop and closes the program
                f.close()
                break