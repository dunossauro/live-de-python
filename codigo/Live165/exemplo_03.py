from pydantic import BaseModel


class Pessoa(BaseModel):
    nome: str
    idade: int


class Pessoas(BaseModel):
    pessoas: list[Pessoa]


class Festa(BaseModel):
    maiores: Pessoas
    menores: Pessoas


d = {
    'maiores': {
        'pessoas': [
            {'nome': 'Fausto', 'idade': 29},
            {'nome': 'Cássia', 'idade': 25}
        ]
    },
    'menores': {
        'pessoas': [
            {'nome': 'Fausto', 'idade': 29},
            {'nome': 'Cássia', 'idade': 25}
        ]
    }
}


Festa(**d)
