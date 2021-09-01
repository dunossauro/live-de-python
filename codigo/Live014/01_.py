"""
Parte 1
"""
import threading

print(threading.active_count())  # Retorna a contagem das threads
print(threading.enumerate())  # Retonar uma iterável das threads
"""
parte 2
"""
import threading

print(threading.enumerate()[0].name)  # Nome da thread
print(threading.enumerate()[0].is_alive())  # Stado da thread

"""
Parte 3

Criando uma Thread
"""
import threading
from time import sleep

def wait():
    sleep(2)

t = threading.Thread(target=wait, name='wait')
t.start()
print(threading.enumerate()[1].name)
print(threading.enumerate()[1].is_alive())

"""
parte 4
"""
import threading
from time import sleep


def wait():
    count = 0
    while True:
        print(count)
        count += 1
        sleep(0.1)


t = threading.Thread(target=wait, name='wait')
t.start()
print(threading.enumerate()[1].name)
print(threading.enumerate()[1].is_alive())

"""
parte 5
"""
import threading
from time import sleep


def wait():
    sleep(2)


t = threading.Thread(target=wait, name='wait', daemon=True)
t.start()
print(threading.enumerate()[1].name)
print(threading.enumerate()[1].is_alive())
t.join()

"""
parte 6
"""
import threading
from time import sleep


def wait():
    sleep(2)
    print('acabou')


t1 = threading.Thread(target=wait, name='wait', daemon=True)
t1.start()
print(threading.enumerate()[1].name)
print(threading.enumerate()[1].is_alive())

t2 = threading.Thread(target=wait, name='wait')
t2.start()
print(threading.enumerate()[2].name)
print(threading.enumerate()[2].is_alive())
"""
parte 7
"""
import threading
from time import sleep


def wait():
    sleep(2)
    print('acabou')


class myThread(threading.Thread):
    def __init__(self, target, name='MyThread'):
        super().__init__()
        self.target = target
        self.name = name

    def run(self):
        self.target()


t = myThread(wait, 'wait')
t.start()
print(threading.enumerate()[1].name)
print(threading.enumerate()[1].is_alive())
