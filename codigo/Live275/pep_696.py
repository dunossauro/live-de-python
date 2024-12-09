from typing import Generic, TypeVar

T = TypeVar('T', default=int)


class C(Generic[T]):
    def set_val(self, val: T) -> None:
        self.val = val

C().set_val(1)
C().set_val('1')  # error
C[str]().set_val('1')  # ok

from dataclasses import dataclass
from typing import Final

@dataclass
class D[S = int]:
    val: S | None = None


d = D()
d1 = D[str]()

d.val = '10'  # error!
d1.val = 1    # error!


reveal_locals()
