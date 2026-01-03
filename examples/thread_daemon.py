from threading import Thread
from time import sleep

def func():
    for i in range(5):
        print(f"from child thread: {i}")
        sleep(0.5)

th = Thread(target=func, daemon=True)  # или th.daemon = True
th.start()
sleep(0.2)
print("App stop")
