from numbers import Number


class Cliente:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self._nome_completo = f'{self.nome} {self.sobrenome}'

    @property
    def nome_completo(self):
        print('Estou pegando algo')
        return f'{self.nome} {self.sobrenome}'

    @nome_completo.setter
    def nome_completo(self, obj):
        print('Estou setando algo')
        if isinstance(obj, Number):
            print('Cara, não use números')
        else:
            self._nome_completo = obj
