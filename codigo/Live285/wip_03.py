from hypothesis import Verbosity, example, given, settings
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
def custom_dict(draw: st.DrawFn):
    return {
        'nome': draw(st.text(min_size=3)),
        'idade': draw(st.integers(min_value=18)),
        'cpf': draw(st.from_regex(r'[0-9]{11}', fullmatch=True))
    }


@given(custom_dict())
@settings(
    verbosity=Verbosity.verbose
)
@example(
    {'nome': '', 'idade': 22, 'cpf': '12345678901'}
).xfail(reason='Nome vazio')
@example(
    {'nome': 'fausto', 'idade': 17, 'cpf': '1234567890'}
).xfail(reason='menor de idade')
@example(
    {'nome': 'fausto', 'idade': 22, 'cpf': '123'}
).xfail(reason='cpf inválido')
@example(
    {'nome': 'fausto', 'idade': 22, 'cpf': '12312312312'}
).xfail().via('issue 572')
def test_validation(data: dict):
    assert validation(data)
