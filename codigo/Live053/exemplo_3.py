"""Ideia de funções não serializaveis."""
from pickle import dumps
from multiprocessing import Process


def closure(func):
    """A função (func) está no escopo da closure."""

    def inner(*args):
        """Os argumentos estão no escopo de inner."""
        return print(func(*args))
    return inner

def add(x, y):
    return x + y


func = closure(add)

print(dumps(closure))
print(dumps(add))
print(dumps(func))

p = Process(target=func, args=(7, 7))
p.start()
p.join()
