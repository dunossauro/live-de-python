from typing import Self

class Vector[S: complex]:
    def __init__(self: Self, x: S, y: S) -> None:
        self.x = x
        self.y = y


v0 = Vector[bool](False, True)
v1 = Vector[int](1, 1)
v2 = Vector[float](1.2, 1.7)
