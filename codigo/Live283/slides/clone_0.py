from  abc import ABC, abstractmethod


class Prototype(ABC):
    @abstractmethod
    def clone(self) -> 'Prototype':
        ...


class Guerreiro(Prototype):
    def __init__(self, classe, ataque, defesa):
        self.classe = classe
        self.ataque = ataque
        self.defesa = defesa

    def clone(self) -> 'Guerreiro':
        construtor = self.__new__
        estado = {
            'classe': self.classe,
            'ataque': self.ataque,
            'defesa': self.defesa,
        }

        clone = construtor(self.__class__)
        clone.__dict__ = estado

        return clone

        
if __name__ == '__main__':
    g = Guerreiro('Pedra', 7, 31)
    
