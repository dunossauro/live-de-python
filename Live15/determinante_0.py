from threading import Thread
from queue import Queue
from time import sleep

q = Queue()

matriz = [[2, 9],
          [-1, 6]]


def principal(mat):
    sleep(10)
    q.put(mat[0][0] * mat[1][1])


def secundaria(mat):
    count = 0
    while q.empty():
        count += 1

    print(count)
    q.put(mat[1][0] * mat[0][1])


t_p = Thread(target=principal, kwargs={'mat': matriz}, name='principal')
t_p.start()

t_s = Thread(target=secundaria, kwargs={'mat': matriz}, name='secundária')
t_s.start()
t_s.join()

print(q.queue)

val_p = q.queue[0]
val_s = q.queue[1]

print(val_p - val_s)
