class Vlad:
    """Contexto."""
    def __init__(self):
        self.state = None

    def se_mover(self):
        self.state.se_mover()


class Humanoide:
    def se_mover(self):
        print('Andando...')

class Morcego:
    def se_mover(self):
        print('Voando...')
