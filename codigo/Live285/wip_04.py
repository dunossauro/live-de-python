from pydantic import BaseModel, Field
from hypothesis import Verbosity, given, settings
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
    cpf: str = Field(
        min_length=11, max_length=11, pattern=r'[0-9]{11}'
    )


@given(st.builds(
    Data,
    cpf=st.from_regex(r'[0-9]{11}', fullmatch=True)
))
@settings(
    verbosity=Verbosity.verbose,
    max_examples=1_000,
)
def test_validation(data: Data):
    assert validation(data.model_dump())
