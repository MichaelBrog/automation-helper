# from pynput.mouse import Button, Controller as MouseController
# from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Controller as MouseController
from pynput.mouse import Button as MouseButton

from pynput.keyboard import Controller as KeyboardController
from pynput.keyboard import Key as KeyboardKey
from pynput.keyboard import KeyCode as KeyCode

import sys
import os
import re

def main():
    print("Argument List: ", str(sys.argv))
    filename = "./events/" + sys.argv[1] + ".txt"
    if not os.path.exists(filename):
        return
    with open(filename) as f: 
        for line in f:
            if line != '':
                line = line.replace('\n', '')
                line = line.split("#")
                if(line[0] == "mouse"):
                    mouseCommand(line[1], line[2])
                if(line[0] == "keyboard"):
                    keyboardCommand(line[1], line[2])

def mouseCommand(action, value):
    mouse = MouseController()
    x, y = map(float, re.findall(r'-?\d+\.?\d*', value))
    print('mouse is {} with vals X:{} Y: {}'.format(action, x, y))
    if action == 'move':
        mouse.position = (x, y)
    if action == 'clickleft':
        mouse.press(MouseButton.left)
        mouse.release(MouseButton.left)
        print('clickleft')
    if action == 'clickright':
        mouse.press(MouseButton.right)
        mouse.release(MouseButton.right)
        print('clickright')
    if action == 'scrolldown':
        mouse.scroll(1, 0)
        print('scroll')

def keyboardCommand(action, value):
    keyboard = KeyboardController()
    print('keyboard is {} with val: {}'.format(action, value))
    if action == 'click':
        print('type is: {}'.format(type(value)))
        print('value is: {}'.format(value))
        if value.count("'"):
            value = "'"
        else: 
            value = value.replace("'", "")
        if "." in value:
            # value = KeyboardKey
            print('split value is: {}'.format(value))
            # value = KeyCode.from_char(value)
            # print('KeyCode type is: {}'.format(type(value)))
            # print('KeyCode value is: {}'.format(value))
            value = translate_key(value)
        keyboard.press(value)
        keyboard.release(value)




def translate_key(value):
    isMac = sys.platform == 'darwin'
    print(isMac)
        # print('KeyCode value is: {}'.format(value))
    keyType = value.split(".")[1]
    if keyType == 'space':
        return KeyboardKey.space
    if keyType == 'enter':
        return KeyboardKey.enter
    if keyType == 'backspace':
        return KeyboardKey.backspace
    if keyType == 'media_next':
        return KeyboardKey.media_next
    if keyType == 'media_next':
        return 't' if isMac else KeyboardKey.media_next
    if keyType == 'media_volume_up':
        return 'a' if isMac else KeyboardKey.media_volume_up
    if keyType == 'shift':
        return KeyboardKey.shift
    if keyType == 'media_play_pause':
        return KeyboardKey.media_play_pause
    if keyType == 'media_volume_mute':
        return 'x' if isMac else KeyboardKey.media_volume_mute
    if keyType == 'media_previous':
        return '1' if isMac else KeyboardKey.media_previous
    if keyType == 'media_volume_down':
        return 's' if isMac else KeyboardKey.media_volume_down
    if keyType == 'ctrl':
        return KeyboardKey.ctrl
    if keyType == 'alt':
        return KeyboardKey.ctrl


    print('Random ass key is: {}'.format(value))
    return value


if __name__ == '__main__':
    main()
