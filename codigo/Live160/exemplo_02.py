from exemplo_01 import Pessoa, Grupo, Nota

eduardo = Pessoa(
    nome='eduardo',
    idade=18,
    senha='1234567',
    email='eu@dunossauro.live'
)

try:
    eduardo.save()
    Pessoa.create(
        nome='Fausto',
        idade=3,
        email='fausto@live',
        senha='7654321'
    )

except:
    ...


pessoas = [
    {'nome': 'Irmão do jorel', 'email': 'irmao@live', 'idade': 1, 'senha': '123'},
    {'nome': 'Gesonel', 'email': 'gesinho@live', 'idade': 1, 'senha': '123'},
    {'nome': 'Lara', 'email': 'lara@live', 'idade': 1, 'senha': '123'},
]

Pessoa.insert_many(pessoas).execute()

