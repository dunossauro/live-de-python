from __future__ import annotations

from typing import Protocol
from memory_profiler import profile


class Originator(Protocol):
    def create_memento(self) -> 'Memento':
        ...

    def set_memento(self, memento: 'Memento') -> None:
        ...


class Memento[T]:
    def __init__(self, state: T) -> None:
        self.state = state

    def get_state(self) -> T:
        return self.state

    def __repr__(self) -> str:
        return f'Memento(state={self.state})'


class Pessoa:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    @profile
    def create_memento(self) -> Memento:
        return Memento(Pessoa(nome=self.nome))

    def set_memento(self, memento: Memento) -> None:
        state: Pessoa = memento.get_state()
        self.nome = state.nome

    def __repr__(self) -> str:
        return f'Originator(nome="{self.nome}")'


class Caretaker:
    def __init__(self, o: Originator) -> None:
        self.o = o
        self.history: list[Memento] = []

    def create_memento(self) -> None:
        state = self.o.create_memento()
        self.history.append(state)

    def undo(self) -> None:
        state = self.history.pop()
        self.o.set_memento(state)


# Exemplo de uso!
originator = Pessoa('Eduardo')
caretaker = Caretaker(originator)
print(caretaker.history)

caretaker.create_memento()
print(caretaker.history)

originator.nome = 'Fausto'
caretaker.create_memento()
print(caretaker.history)

caretaker.undo()
print(originator)
print(caretaker.history)

caretaker.undo()
print(originator)
print(caretaker.history)
