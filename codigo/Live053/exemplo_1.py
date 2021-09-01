"""Exemplo de como compartilhar uma queue entre processos e threads."""
from collections import namedtuple
from multiprocessing import Process, Queue
from threading import Thread
# from queue import Queue
from os import getpid, getppid

q = Queue()
pstate = namedtuple('pstate', 'name pid ppid')


def info(name):
    obj = pstate(name, getpid(), getppid())
    print(obj)
    q.put(obj)


info('main line')
t = Thread(target=info, args=('Thread',))
p = Process(target=info, args=('Process',))

t.start()
p.start()

t.join()
p.join()

# print(q.qeue)
print([q.get() for e in range(3)])
