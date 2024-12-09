from typing import TypeVar, Generic


T = TypeVar('T', default=str)


class C(Generic[T]):
    def __init__(self, val_1, val_2) -> None:
        self.val_1: T = val_1
        self.val_2: T = val_2


c = C[int](1, 2)
d = C('1', '2')

d.val_1.capitalize()
