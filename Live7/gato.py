class gatinho:
    def __init__(self, nome, cor, idade):
        self.nome = nome
        self.cor = cor
        self.idade = idade
        self.mingal_com_fome = False
        self.rodado = 0

    def miar(self):
        if self.mingal_com_fome:
            return 'MIAAAUUUUUUUUUUUUU'
        return 'Miau, Miau'

    def andar(self):
        self.rodado += 1
        self.mingal_com_fome = True
        return 'Mingau andando'

    @property
    def velho(self):
        return True if self.idade > 3 else False

    @property
    def cansado(self):
        return True if self.rodado > 5 else False

# mingau = gatinho('mingau', 'branco', 2)

# print(mingau.nome)
# print(mingau.cor)
# print(mingau.idade)
# print(mingau.miar())
# print(mingau.miar())

# print(mingau.andar())
# print(mingau.andar())
# print(mingau.andar())
# print(mingau.andar())
# print(mingau.andar())
# print(mingau.andar())
# print(mingau.velho)
# print(mingau.cansado)
