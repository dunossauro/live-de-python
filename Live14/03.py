from threading import Thread, currentThread
from queue import Queue
from time import sleep
from functools import reduce

q = Queue(maxsize=2)

matriz = [[2, 9],
          [-1, 6]]


def principal(mat):
    sleep(10)
    q.put(mat[0][0] * mat[1][1])


def secundaria(mat):
    count = 0
    while q.empty():
        count += 1

    print('secundaria', count)
    q.put(mat[1][0] * mat[0][1])


def result():
    count = 0
    while not q.full():
        count += 1

    print('result', count)
    return reduce(lambda x, y: x - y, q.queue)


t_p = Thread(target=principal, kwargs={'mat': matriz}, name='Principal')
t_p.start()

t_s = Thread(target=secundaria, kwargs={'mat': matriz}, name='Secundaria')
t_s.start()


class Result(Thread):
    def __init__(self, target):
        super().__init__()
        self.result = None
        self.target = target
        self.stoped = False

    def start(self):
        self.result = self.target()
        self.stoped = True

    def join(self):
        while not self.stoped:
            sleep(0.1)
        return self.result


t_r = Result(target=result)
print(currentThread())
t_r.start()
print(t_r.join())
