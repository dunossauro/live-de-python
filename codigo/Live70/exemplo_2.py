class Cliente:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'
