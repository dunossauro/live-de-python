from __future__ import annotations
from abc import ABC, abstractmethod


class Prototype(ABC):
    @abstractmethod
    def clone(self) -> Prototype:
        ...


class User(Prototype):
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email

    def clone(self) -> User:
        new = self.__class__.__new__(self.__class__)
        new.__dict__ = self.__dict__.copy()
        return new

    def __copy__(self) -> User:
        print('Estou em __copy__')
        new = self.__class__.__new__(self.__class__)
        new.__dict__ = self.__dict__.copy()
        return new

    def __replace__(self, **attrs) -> User:
        new = self.__class__.__new__(self.__class__)
        copy = self.__dict__.copy()

        new.__dict__ = copy | {
            key: value for key,value in attrs.items() if key in copy
        }

        return new

    def __eq__(self, other) -> bool:
        return vars(self) == vars(other)


class Client:
    def __init__(self, xpto: Prototype):
        self.xpto = xpto

    def create_new(self) -> Prototype:
        return self.xpto.clone()


c = Client(User('Cicinho', 'ci@cinho.net'))
d = c.create_new()
e = c.create_new()



from copy import deepcopy
