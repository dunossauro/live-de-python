from collections import deque


def contador(stop):
    cont = 1
    while cont <= stop:
        yield cont
        cont += 1


def contador_regressivo(start):
    while start >= 1:
        yield start
        start -= 1


class Scheduler:
    def __init__(self):
        self.queue = deque()

    def add_new(self, coro):
        self.queue.append(coro)

    def run(self):
        while self.queue:
            task = self.queue.popleft()
            try:
                result = next(task)
                print(f'{task=}: {result=}')

                self.queue.append(task)
            except StopIteration:
                ...


s = Scheduler()
s.add_new(contador(10))
s.add_new(contador_regressivo(15))
