# from pynput.mouse import Button, Controller as MouseController
# from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Controller as MouseController
from pynput.mouse import Button as MouseButton
from pynput.keyboard import Controller as KeyboardController
from pynput.keyboard import Key as KeyboardKey
from pynput.keyboard import KeyCode as KeyCode
import datetime
import sys
import os
import re
import time


def eventReplayer(filename):
    filename = "./events/" + filename + ".txt"
    f = open(filename)
    if not os.path.exists(filename):
        return
    prevTime = 0
    shiftup = False
    with open(filename) as f: 
        for line in f:
            if line != '' or line is None or len(line) == 0:
                print('Current value is: {}'.format(line))
                line = line.replace('\n', '')
                print(line)
                if(line.endswith('#')):
                    print('hashtag true')
                    line = line.split("#")
                    line[3] = '#'
                else:
                    line = line.split("#")
                print(line)
                if line[1] == "keyboard" and line[2] == 'click' and (line[3] == 'Key.shift' or line[3] == 'Key.shift_r'):
                    print('shift is true\n\n')
                    shiftup = True
                else:
                    if prevTime == 0:
                        prevTime1 = datetime.datetime.strptime(line[0], '%Y-%m-%d %H:%M:%S.%f')
                        prevTime = float(prevTime1.timestamp() * 1000)
                        '{0:.15f}'.format(prevTime)
                    else:
                        currentTime1 = datetime.datetime.strptime(line[0], '%Y-%m-%d %H:%M:%S.%f')
                        currentTime = float(currentTime1.timestamp() * 1000)
                        '{0:.15f}'.format(currentTime)
                        interval = (currentTime - prevTime) / 1000
                        '{0:.15f}'.format(interval)
                        print('currentTime: {} prevTime: {} interval: {}'.format(currentTime, prevTime, interval))
                        prevTime = currentTime
                        print(prevTime)
                        print(float(prevTime))
                        time.sleep(interval)
                    if(line[1] == "mouse"):
                        mouseCommand(line[2], line[3])
                    if(line[1] == "keyboard"):
                        keyboardCommand(line[2], line[3], shiftup)
                    shiftup = False
    print("Done.")

def mouseCommand(action, value):
    mouse = MouseController()
    x, y = map(float, re.findall(r'-?\d+\.?\d*', value))
    print('mouse is {} with vals X:{} Y: {}'.format(action, x, y))
    if action == 'move':
        mouse.position = (x, y)
    if action == 'clickleft':
        mouse.press(MouseButton.left)
        mouse.release(MouseButton.left)
    if action == 'clickright':
        mouse.press(MouseButton.right)
        mouse.release(MouseButton.right)
    if action == 'scrolldown':
        mouse.scroll(1, 0)

def keyboardCommand(action, value, shift):
    keyboard = KeyboardController()
    # print('keyboard is {} with val: {}'.format(action, value))
    if action == 'click':
        print('type is: {}'.format(type(value)))
        print('value is: {}'.format(value))
        if value.count("'"):
            value = "'"
        else: 
            value = value.replace("'", "")
        if not "None" in value:
            if "." in value:
                value = translate_key(value)
            if value != KeyboardKey.f8:
                if shift:
                    # print('value: {} isalpha: {}'.format(value, value.isalpha()))
                    print('TYPE OF VALUE: {} is: {}'.format(value, type(value)))
                    if isinstance(value, str) and value.isalpha() or value == 'a' or value == 's':
                        print('\n\n\n\n inside of isalpha')
                        value = value.strip()
                        value = value.capitalize()
                keyboard.press(value)
                keyboard.release(value)

def translate_key(value):
    isMac = sys.platform == 'darwin'
    # print(isMac)
        # print('KeyCode value is: {}'.format(value))
    keyType = value.split(".")[1]
    if keyType == 'space':
        return KeyboardKey.space
    if keyType == 'enter':
        return KeyboardKey.enter
    if keyType == 'backspace':
        return KeyboardKey.backspace
    if keyType == 'media_next':
        return 't' if isMac else KeyboardKey.media_next
    if keyType == 'media_volume_up':
        return 'a' if isMac else KeyboardKey.media_volume_up
    if keyType == 'shift':
        return KeyboardKey.shift
    if keyType == 'media_play_pause':
        return 'y' if isMac else KeyboardKey.media_play_pause
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
    if keyType == 'f8':
        return KeyboardKey.f8
    if keyType == 'caps_lock':
        return KeyboardKey.caps_lock
    if keyType == 'shift_r':
        return KeyboardKey.shift_r
    if keyType == 'ctrl_r':
        return KeyboardKey.ctrl_r
    if keyType == 'cmd':
        return KeyboardKey.cmd
    if keyType == 'tab':
        return KeyboardKey.tab

    print('Random ass key is: {}'.format(value))
    return value

numDict = {
    '1': '!',
    '2': '@',
    '3': '#',
    '4': '$',
    '5': '^',
    '6': '&',
    '8': '*',
    '9': '(',
    '0': ')',
    '`': '~',
    '-': '_',
    '=': '+',
    '[': '{',
    ']': '}',
    '\\': '|',
    ';': ':',
    '\'': '"',
    ',': '<',
    '.': '>',
}