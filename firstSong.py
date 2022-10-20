import random

from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time

interval = 0.2 + random.uniform(-0.05, 0.05)


def dec(code):
    tonedict = {'1-': 'y', '2-': 'u', '3-': 'i', '4-': 'o', '5-': 'p',
                '6-': 'h', '7-': 'j', '1=': 'k', '2=': 'l', '3=': ';',
                '4=': 'n', '5=': 'm', '6=': ',', '7=': '.', '11': '/',
                'xx': -1, '\n\n': -1}
    return tonedict[code]


def tap(tone):
    k.press_key(tone)
    time.sleep(0.05)
    k.release_key(tone)


def play():
    for x in range(0, len(tones) - 1, 2):
        code = tones[x] + tones[x + 1]
        tone = dec(code)
        if tone == -1:
            time.sleep(interval)
        else:
            tap(tone)
            time.sleep(interval)


k = PyKeyboard()

time.sleep(2)
#
# k.press_keys(['command', 'shift', '3'])
# time.sleep(3)
# k.press_keys(['command', 'shift', '4'])

fo = open('thankyou', 'r+')
tones = fo.read()
fo.close()

play()
