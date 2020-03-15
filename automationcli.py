import click
import os

from classtest import classTest
from eventMakerCLI import eventListener
from controllertimecli import eventReplayer
@click.command()
@click.option('--startrecording/--playrecording', '-s/-p')
@click.argument('text', nargs=-1)
# @click.option('--key', '-k', default=1)
def clickRecorder(startrecording, text):
    text_string = ' '.join(text)
    filename = "./events/" + text_string + ".txt"

    print(startrecording)
    if(startrecording):
        print('start recording')
        meow = classTest(text_string)
        print(meow.name)
        eventListener(text_string)
        clickRecorder()
    else:
        if not os.path.exists(filename):
            print(filename + "Does not exist")
            return
        clickRecorder()
        eventReplayer(text_string)
        print('play recording')
if __name__ == '__main__':
    clickRecorder()
    