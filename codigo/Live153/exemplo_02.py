from collections import deque
from time import sleep


def contador(name, stop):
    cont = 1
    while cont <= stop:
        yield name, cont
        cont += 1
        sleep(.1)


def contador_regressivo(name, start):
    while start >= 1:
        yield name, start
        start -= 1
        sleep(1)


class Scheduler:
    def __init__(self):
        self.queue = deque()

    def add_new(self, coro):
        self.queue.append(coro)

    def run(self):
        while True:
            if self.queue:
                task = self.queue.popleft()
                try:
                    name, result = next(task)
                    print(f'Task {name}: {result=}')

                    self.queue.append(task)
                except StopIteration:
                    ...


s = Scheduler()
s.add_new(contador('A', 60))
s.add_new(contador('B', 60))
# s.add_new(contador('RunTime', 150))

from threading import Thread
t = Thread(target=s.run, daemon=True)
