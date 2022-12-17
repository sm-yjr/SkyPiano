import _thread
import time
import skypiano as sky



def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(threadName, time.ctime(time.time()))


try:
    time.sleep(2)
    _thread.start_new_thread(sky.shout, ("thread1", 0.1,))
    time.sleep(0.4)
    _thread.start_new_thread(sky.shout, ("thread2", 0.1,))

except:
    print("Error!")

while 1:
    pass
