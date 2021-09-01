from collections import namedtuple

# j = namedtuple('Jogador', 'nome time camisa n')

# n = namedtuple('ABC', 'slot1 slot2 slot3')

naipes = 'P C O E'.split()
valores = list(range(2, 11)) + 'A J Q K'.split()

carta = namedtuple('Carta', 'naipe valor')

baralho = [carta(naipe, valor) for naipe in naipes for valor in valores]
