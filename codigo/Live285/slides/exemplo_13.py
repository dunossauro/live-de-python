# /// script
# requires-python = ">=3.11"
# dependencies = ["pytest", "hypothesis", "pydantic"]
# ///
from pydantic import BaseModel, Field
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


class Data(BaseModel):
    nome: str = Field(min_length=3)
    idade: int = Field(ge=18)
    cpf: str = Field(min_length=11, max_length=11, pattern=r'\d{11}')


@given(st.builds(Data, cpf=st.from_regex(r'\d{11}', fullmatch=True)))
def test_validation(data):
    assert validation(data.model_dump())


if __name__ == '__main__':
    import pytest

    pytest.main(['exemplo_13.py'])
