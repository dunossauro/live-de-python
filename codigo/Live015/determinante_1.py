from threading import Thread, Event
from queue import Queue
from time import sleep
from functools import reduce

e = Event()
q = Queue(maxsize=2)
r = Queue()

matriz = [[2, 9],
          [-1, 6]]


def principal(mat):
    sleep(3)
    q.put(mat[0][0] * mat[1][1])
    e.set()


def secundaria(mat):
    sleep(2)
    count = 0
    while q.empty():
        count += 1

    print(count)
    q.put(mat[1][0] * mat[0][1])
    # e.set()


def result():
    e.wait()
    r.put(reduce(lambda x, y: x - y, q.queue))


t_p = Thread(target=principal, kwargs={'mat': matriz}, name='principal')
t_p.start()

t_s = Thread(target=secundaria, kwargs={'mat': matriz}, name='secundária')
t_s.start()

t_r = Thread(target=result, name='result')
t_r.start()
t_r.join()

print(r.queue[0])
