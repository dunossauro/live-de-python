"""Exemplo de uma tarefa que diz a hora."""
import sched
import time

scheduler = sched.scheduler()


def saytime():
    print(time.ctime())
    scheduler.enter(delay=1, priority=1, action=saytime)


def ola():
    print('Olá')
    scheduler.enter(delay=1, priority=20, action=ola)


def start():
    scheduler.enter(delay=1, priority=1, action=saytime)
    scheduler.enter(delay=1, priority=0, action=ola)


start()

try:
    scheduler.run(blocking=True)
except KeyboardInterrupt:
    print('Parei com sched')
