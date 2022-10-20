import skypiano as sky
import time


class MyGuitar:
    def __init__(self):
        self.data = []

def play(path):
    time.sleep(2)

    fo = open(path, 'r+')
    tones = fo.read()
    fo.close()

    buf = []
    for x in range(0, len(tones) - 1, 2):
        code = tones[x] + tones[x + 1]
        tone = sky.dec(code)

        if tone == 1:
            continue
        elif tone == -1:
            time.sleep(sky.interval)
        elif tone == 0:
            sky.releasekey(buf)
            time.sleep(sky.interval)
        else:
            sky.releasekey(buf)

            buf = tone

            sky.presskey(tone)

    sky.releasekey(buf)


play(sky.song_PATH)
