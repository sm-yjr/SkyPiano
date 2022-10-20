import _thread
import time
import skypiano as sky
import guitar
import firstSong

def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(threadName, time.ctime(time.time()))


try:
    time.sleep(2)
    _thread.start_new_thread(guitar.play, ())
    time.sleep(2)
    _thread.start_new_thread(guitar.play, ())

except:
    print("Error!")

while 1:
    pass
