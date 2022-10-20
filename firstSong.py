import skypiano as sky
from pykeyboard import PyKeyboard
import time

k = PyKeyboard()
song_PATH = 'song/DaBeiZhou'


def tap(tone):
    k.press_key(tone)
    time.sleep(0.05)
    k.release_key(tone)


def play():
    for x in range(0, len(tones) - 1, 2):
        code = tones[x] + tones[x + 1]
        tone = sky.dec(code)
        if tone == -1:
            time.sleep(sky.interval)
        else:
            if tone == 1:
                a = 1
            else:
                tap(tone)
                time.sleep(sky.interval)


time.sleep(2)
#
# k.press_keys(['command', 'shift', '3'])
# time.sleep(3)
# k.press_keys(['command', 'shift', '4'])

fo = open(song_PATH, 'r+')
tones = fo.read()
fo.close()

play()
