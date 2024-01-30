from rich import print

class Memento:
    def __init__(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def __repr__(self) -> str:
        return f'Memento(state={self.state})'


class Originator:
    def __init__(self, nome):
        self.nome = nome

    def save(self) -> Memento:
        return Memento(
            Originator(self.nome)
        )

    def restore(self, memento: Memento) -> None:
        state: Originator = memento.get_state()
        self.nome = state.nome

    def __repr__(self) -> str:
        return f'Originator(nome="{self.nome}")'


class Caretaker:
    def __init__(self, obj: Originator) -> None:
        self.obj = obj
        self.history: list[Memento] = []

    def save(self):
        """
        snapshot / Checkpoint / Record ...
        """
        memento: Memento = self.obj.save()
        self.history.append(memento)

    def rollback(self):
        """
        undo
        """
        last_state = self.history.pop()
        self.obj.restore(last_state)

    def __repr__(self) -> str:
        return f'Caretaker(history={self.history})'


originator = Originator(nome='Lengo')
caretaker = Caretaker(originator)

# Estado inicial
caretaker.save()
print(caretaker)

# Estado 2
originator.nome = 'Jhonata'
caretaker.save()
print(caretaker)

# Estado 3
originator.nome = 'Ronivaldo'
caretaker.save()
print(caretaker)
print(originator)


# De volta ao Estado 3
caretaker.rollback()
print(originator)

# De volta ao Estado 2
caretaker.rollback()
print(originator)


# De volta ao Estado 1
caretaker.rollback()
print(originator)
