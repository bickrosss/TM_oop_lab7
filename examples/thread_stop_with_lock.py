from threading import Thread, Lock
from time import sleep

lock = Lock()
stop_thread = False

def infinite_worker():
    print("Start infinite_worker()")
    while True:
        print("--> thread work")
        lock.acquire()
        if stop_thread is True:
            break
        lock.release()
        sleep(0.1)
    print("Stop infinite_worker()")

# Create and start thread
th = Thread(target=infinite_worker)
th.start()
sleep(2)

# Stop thread
lock.acquire()
stop_thread = True
lock.release()
