# /// script
# requires-python = ">=3.11"
# dependencies = ["pytest", "hypothesis"]
# ///
from dataclasses import dataclass, asdict
from hypothesis import given
from hypothesis import strategies as st


def validation(data: dict) -> bool:
    return all([
        # Nenhum campo é vazio
        all([value for value in data.values()]),
        # Idade maior que 18
        data['idade'] >= 18,
        # cpf é formado por números
        data['cpf'].isnumeric(),
        # cpf tem o tamanho certo
        len(data['cpf']) == 11
    ])


from dataclasses import dataclass, asdict
from hypothesis import given
from hypothesis import strategies as st

@dataclass
class Data:
    nome: str
    idade: int
    cpf: str


@given(st.from_type(Data))
def test_validation(data):
    assert validation(asdict(data))


if __name__ == '__main__':
    import pytest

    pytest.main(['exemplo_12.py'])
