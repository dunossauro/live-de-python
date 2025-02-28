from dataclasses import dataclass
from typing import Literal, get_args

import faker

type Target = Literal['name', 'desc']

@dataclass
class Todo:
    name: str
    desc: str | None


class TodoManager:
    def __init__(self) -> None:
        self.todos: list[Todo] = []

    def add(self, todo: Todo) -> None:
        self.todos.append(todo)

    def _find(self, target, text) -> Todo | None:
        if target in get_args(Target):
            return next(
                filter(lambda t: getattr(t, target) == text, self.todos),
                None
            )

    def remove(self, target: Target, text: str) -> None:
        if todo := self._find(target, text):
            self.todos.remove(todo)
            

    def get_by(self, target: Target, text: str):
        return self._find(target, text)


def test_add_test():
    tm = TodoManager()
    f = faker.Faker()
    todo = Todo(f.name(), f.text())

    tm.add(todo)

    assert todo in tm.todos

    assert tm.get_by('name', todo.name)

    tm.remove('name', todo.name)
    
    assert todo not in tm.todos
