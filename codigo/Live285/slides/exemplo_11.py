# /// script
# requires-python = ">=3.11"
# dependencies = ["pytest", "hypothesis"]
# ///
from hypothesis import example, given
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


@st.composite
def custom_dict(draw):
    return {
        'idade': draw(st.integers(min_value=18)),
        'nome': draw(st.text(min_size=3)),
        'cpf': draw(st.from_regex(r'\d{11}', fullmatch=True))
    }


# @example(
#     {'nome': '', 'idade': 22, 'cpf': '12345678901'}
# ).xfail(reason='Nome vazio')
# @example(
#     {'nome': 'fausto', 'idade': 17, 'cpf': '1234567890'}
# ).xfail(reason='menor de idade')
# @example(
#     {'nome': 'fausto', 'idade': 22, 'cpf': '123'}
# ).xfail(reason='cpf inválido')
@given(custom_dict())
def test_validation(data):
    assert validation(data)


if __name__ == '__main__':
    import pytest

    pytest.main(['exemplo_11.py'])
