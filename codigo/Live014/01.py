import threading
from time import sleep


def wait():
    sleep(2)
    print('acabou')


class myThread(threading.Thread):
    def __init__(self, target, name='myThread'):
        super().__init__()
        self.target = target
        self.name = name

    def run(self):
        self.target()


t = myThread(wait)
t.start()
print(t.name)
