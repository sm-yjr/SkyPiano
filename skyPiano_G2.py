import time
from pykeyboard import PyKeyboard

k = PyKeyboard()
interval = 0.25
song_PATH = 'song/CherryGrass'


def dec(code):
    tonedict = {'1L': 'y', '2L': 'u', '3L': 'i', '4L': 'o', '5L': 'p',
                '6L': 'h', '7L': 'j', '1H': 'k', '2H': 'l', '3H': ';',
                '4H': 'n', '5H': 'm', '6H': ',', '7H': '.', '1S': '/',
                'xx': 1, '\n\n': 1, '  ': 1, '00': 0}
    tonecode = code[0:2]
    return tonedict[tonecode] + code[2]


def presskey(key, n):
    if key:
        k.press_key(key)
    n = int(n)
    time.sleep(interval * n)


# random.uniform(-0.03,0.03)

def releasekey(buf):
    if buf:
        k.release_key(buf)
        time.sleep(0.03)

def play(path):
    time.sleep(2)

    fo = open(path, 'r+')
    tones = fo.read()
    fo.close()

    buf = 0
    for x in range(0, len(tones) - 1, 3):
        tone = dec(tones[x:x+3])

        if tone[0] == 1:
            continue
        # elif tone[0] == -1:
        #     time.sleep(interval)
        # elif tone[0] == 0:
        #     releasekey(buf)
        #     time.sleep(interval)
        # else:
        #     releasekey(buf)
        #
        #     buf = tone
        #
        #     presskey(tone)
        else:
            releasekey(buf)
            buf = tone[0]
            presskey(buf, tone[1])
    releasekey(buf)

play(song_PATH)