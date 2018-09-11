class Pássaro:
    def __init__(self, nome):
        self.nome = nome

class Jogador:
    def __init__(self, camisa):
        self.camisa = camisa

class CanarinhoPistola(Pássaro, Jogador):
    def __init__(self, nome, camisa):
        Pássaro.__init__(self, nome)
        Jogador.__init__(self, camisa)

    def __str__(self):
        return f'CanarinhoPistola(nome="{self.nome}", camisa="{self.camisa}")'

    def __repr__(self):
        return f'CanarinhoPistola(nome="{self.nome}", camisa="{self.camisa}")'
