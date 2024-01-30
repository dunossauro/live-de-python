from copy import copy
from collections import deque


def memento(obj):
    state = copy(obj.__dict__)

    def restore() -> None:
        obj.__dict__.clear()
        obj.__dict__.update(state)

    return restore


class Originator:
    def __init__(self, nome) -> None:
        self.nome = nome

    def save(self):
        return memento(self)

    def rollback(self, memento):
        memento()


class Carataker:
    def __init__(self, _obj) -> None:
        self._obj = _obj
        self.history = deque(maxlen=10)

    def save(self):
        state = self._obj.save()
        self.history.append(state)

    def rollback(self):
        state = self.history.pop()
        self._obj.rollback(state)


originator = Originator(nome='Eduardo')
caretaker = Carataker(originator)

print(originator.nome)
caretaker.save()
print(caretaker.history)

originator.nome = 'Fausto'
print(originator.nome)
caretaker.save()
print(caretaker.history)

caretaker.rollback()
print(originator.nome)
print(caretaker.history)


caretaker.rollback()
print(originator.nome)
print(caretaker.history)
