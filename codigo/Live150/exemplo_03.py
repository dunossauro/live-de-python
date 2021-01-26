from collections import namedtuple

pessoa = namedtuple('Pessoa', 'nome sobrenome telefone ddd')

dados = [
    pessoa('Eduardo', 'Mendes', {'residencial': '1111-111', 'móvel': '999-999-999'}, 19),
    pessoa('Fausto', 'mago', {'residencial': '2222-2222', 'móvel': '888-888-888'}, 51),
]

eduardo = dados[0]
eduardo = pessoa('Eduardo', 'Mendes', {'residencial': '1111-111', 'móvel': '999-999-999'}, 19)

eduardo.nome # 'Eduardo'
eduardo.sobrenome # 'Mendes'
