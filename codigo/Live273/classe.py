from typing import Literal


class Aluno:
    def __init__(self, nome, ra, curso):
        self.nome = nome
        self.ra = ra
        self.curso = curso

    def nota(self, avaliação: Literal['p1', 'p2', 'p3', 'final'], diciplina):
        portal.checa_avaliação(self.ra, avaliação, diciplina)   # abstração!


fausto = Aluno('Fausto', '0816192313', 'Tecnologia em magias')
fausto.nota('final', 'futurologia 1')
