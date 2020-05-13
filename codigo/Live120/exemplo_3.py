def matar_terra():
    print('Dando um chute no inimigo')

def matar_agua():
    print('Afoga o inimigo')

def defender():
    print('Fechando os braços')

def atacar():
    print('Dá um soco no inimgo')


class Zumbi:
    def __init__(self, matar, defender, atacar):
        self._matar = matar
        self._defender = defender
        self._atacar = atacar

    def atacar(self):
        self._atacar()

    def defender(self):
        self._defender()

    def matar(self):
        self._matar()

class ZumbiAquatico(Zumbi):
    def __init__(
        self,
        matar,
        defender,
        atacar=lambda: print('Jogar Pedra')
    ):
        self._matar = matar
        self._defender = defender
        self._atacar = atacar

z_aquatico = Zumbi(
    matar=matar_agua,
    defender=defender,
    atacar=atacar
)
z_voador = Zumbi(matar_terra, defender, atacar)
z_montanha = Zumbi(matar_terra, defender, atacar)
z_da_terra = Zumbi(matar_terra, defender, atacar)



class AplicaPromocao:
    def __init__(self, cliente, promocao):
        ...

    def promocao(self):
        promocao.aplica(cliente)
