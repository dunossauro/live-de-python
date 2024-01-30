from abc import ABC, abstractclassmethod


class Originator(ABC):
    @abstractclassmethod
    def create_memento(self):
        ...

    @abstractclassmethod
    def set_memento(self, memento):
        ...


class Memento:
    def __init__(self, state) -> None:
        self.state = state

    def get_state(self):
        return self.state

    def __repr__(self):
        return f'Memento(state={self.state})'


class Pessoa(Originator):
    def __init__(self, nome):
        self.nome = nome

    def create_memento(self):
        return Memento(Pessoa(nome=self.nome))

    def set_memento(self, memento):
        state = memento.get_state()
        self.nome = state.nome

    def __repr__(self) -> str:
        return f'Originator(nome="{self.nome}")'


class Caretaker:
    def __init__(self, o):
        self.o = o
        self.history = []

    def create_memento(self):
        state = self.o.create_memento()
        self.history.append(state)

    def undo(self):
        if not self.history:
            return None

        memento = self.history.pop()
        self.o.set_memento(memento)


originator = Pessoa('Eduardo')
caretaker = Caretaker(originator)
print(originator)

caretaker.create_memento()

originator.nome = 'Fausto'
print(originator)

caretaker.create_memento()

originator.nome = 'Jarbas'
print(originator)

caretaker.create_memento()

print(caretaker.history)

caretaker.undo()
print(originator)

print(caretaker.history)
