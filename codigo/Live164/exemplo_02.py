from pydantic.dataclasses import dataclass, validator
from pydantic import StrictInt


@dataclass
class Pessoa:
    nome: str
    idade: StrictInt

    # @validator


print(Pessoa(nome='Eduardo', idade='29'))
