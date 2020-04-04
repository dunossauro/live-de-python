from fausto.mater_mortos_vivos import MatadorDeMortosVivos


class Ogro(MatadorDeMortosVivos):
    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return f'Ogro(nome={self.nome})'

    def arrancar_cabeca(self, morto_vivo):
        print('Arrancando cabeça de mortos vivo')

    def esmagar_coracao(self, morto_vivo):
        print('Esmagando cabeças de mortos vivo')
