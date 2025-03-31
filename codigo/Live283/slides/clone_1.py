class Guerreiro:
    def __init__(self, classe, ataque, defesa):
        self.classe = classe
        self.ataque = ataque
        self.defesa = defesa


class Cliente:
    def clone(self, guerreiro):
        construtor = guerreiro.__new__
        estado = {
            'classe': guerreiro.classe,
            'ataque': guerreiro.ataque,
            'defesa': guerreiro.defesa,
        }

        clone = construtor(guerreiro.__class__)
        clone.__dict__ = estado

        return clone
