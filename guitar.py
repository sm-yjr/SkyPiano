import random
from skypiano import dec
from pykeyboard import PyKeyboard
import time

k = PyKeyboard()
interval = 0.25 + random.uniform(-0.03, 0.03)


def play():
    buf = []
    for x in range(0, len(tones) - 1, 2):
        code = tones[x] + tones[x + 1]
        tone = dec(code)
        if tone == 1:
            if buf:
                k.release_key(buf)
                time.sleep(0.03)
                buf = []
        elif tone == -1:
            time.sleep(interval)
        else:
            if buf:
                k.release_key(buf)
                time.sleep(0.03)
                buf = []
            k.press_key(tone)
            buf = tone
            time.sleep(interval)
    if buf:
        k.release_key(buf)
        time.sleep(0.03)


time.sleep(2)
#
# k.press_keys(['command', 'shift', '3'])
# time.sleep(3)
# k.press_keys(['command', 'shift', '4'])

fo = open('DaBeiZhou', 'r+')
tones = fo.read()
fo.close()

play()
