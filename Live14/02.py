from threading import Thread, Lock

c = 0
lock = Lock()


def count_30000():
    global c
    lock.acquire()
    try:
        while c < 30000:
            c += 1
        print(c)
    finally:
        lock.release()


def count_10000():
    global c
    x = 340
    lock.acquire()
    try:
        while c < 100000:
            c += 1
        print(c)
    finally:
        lock.release()


t_0 = Thread(target=count_30000, name='30000', daemon=True)
t_0.start()

t_1 = Thread(target=count_10000, name='10000')
t_1.start()
