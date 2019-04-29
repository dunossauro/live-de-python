class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def __hash__(self):
        return hash(self.nome)

lulu = Pessoa('Lugão')
hash(lulu)

luluzinho = Pessoa('Lugão')

print(lulu == luluzinho) # False

print(hash(lulu) == hash(luluzinho)) # True
