class Guerreiro:
    def __init__(self, classe, ataque, defesa):
        self.classe = classe
        self.ataque = ataque
        self.defesa = defesa

    def clone(self):
        return self.__copy__()

    def __copy__(self) -> 'Guerreiro':
        """Esse objeto implementa o protocolo de cópia."""
        construtor = self.__new__
        clone = construtor(self.__class__)
        clone.__dict__ = self.__dict__.copy()

        return clone
