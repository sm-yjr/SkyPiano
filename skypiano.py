import time
import random
from pykeyboard import PyKeyboard

k = PyKeyboard()
interval = 0.15 + random.uniform(-0.03, 0.03)


def dec(code):
    tonedict = {'1-': 'y', '2-': 'u', '3-': 'i', '4-': 'o', '5-': 'p',
                '6-': 'h', '7-': 'j', '1=': 'k', '2=': 'l', '3=': ';',
                '4=': 'n', '5=': 'm', '6=': ',', '7=': '.', '11': '/',
                'xx': -1, '\n\n': 1, '  ': 1, '00': 0}
    return tonedict[code]


def presskey(key):
    k.press_key(key)
    time.sleep(interval)


def releasekey(buf):
    if buf:
        k.release_key(buf)
        time.sleep(0.03)
        buf = []  # check
