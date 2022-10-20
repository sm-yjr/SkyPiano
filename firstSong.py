import random
from skypiano import dec
from pykeyboard import PyKeyboard
import time

k = PyKeyboard()
interval = 0.25 + random.uniform(-0.03, 0.03)


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
            if tone == 1:
                a = 1
            else:
                tap(tone)
                time.sleep(interval)


time.sleep(2)
#
# k.press_keys(['command', 'shift', '3'])
# time.sleep(3)
# k.press_keys(['command', 'shift', '4'])

fo = open('thankyou', 'r+')
tones = fo.read()
fo.close()

play()
