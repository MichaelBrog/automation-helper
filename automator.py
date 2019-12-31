from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

def main():
    mouse = Controller()
    keyboard = KeyboardController()
    print ("Current position: " + str(mouse.position))
    mouse.move(20, -13)
    mouse.click(Button.left, 1)
    mouse.click(Button.right, 1)


if __name__ == '__main__':
    main()
