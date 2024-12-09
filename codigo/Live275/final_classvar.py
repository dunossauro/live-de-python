from dataclasses import dataclass
from typing import ClassVar, Final

@dataclass
class D:
    val: ClassVar[Final[int | None]] = None


d = D()
d.val # acessível
d.val = 10  # error!
