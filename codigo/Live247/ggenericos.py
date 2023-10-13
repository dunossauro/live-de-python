# Forma antiga:
from typing import TypeVar, Generic

T = TypeVar('T')

class Xpto(Generic[T]):
    def __init__(self, x: T):
        self.x = x

Xpto[float](2.0)  # opcional
Xpto(2.0)

# Forma nova:
class Xpto[T]:
    def __init__(self, x: T):
        self.x = x


Xpto[list[str]](['1']) # opcional
Xpto([1])
