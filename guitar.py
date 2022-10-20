import skypiano as sky
from pykeyboard import PyKeyboard
import time

k = PyKeyboard()
song_PATH = 'song/twilight'


def play():
    buf = []
    for x in range(0, len(tones) - 1, 2):
        code = tones[x] + tones[x + 1]
        tone = sky.dec(code)

        if tone == 1:
            sky.releasekey(tone)
        elif tone == -1:
            time.sleep(sky.interval)
        else:
            sky.releasekey(tone)

            buf = tone

            sky.presskey(tone)

    sky.releasekey(buf)


time.sleep(2)

fo = open(song_PATH, 'r+')
tones = fo.read()
fo.close()

play()
