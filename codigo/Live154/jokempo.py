"""
Modificado de:
https://nbviewer.jupyter.org/github/wardi/iterables-iterators-generators/blob/master/Iterables,%20Iterators,%20Generators.ipynb
"""


def jokempo():
    validos = ('pedra', 'papel', 'tesoura')
    ganha = ('pedra', 'tesoura'), ('tesoura', 'papel'), ('papel', 'pedra')
    result = None

    while True:
        escolhas = [None, None]
        while None in escolhas:
            player, play = yield result
            result = None

            if play in validos:
                escolhas[player] = play
            else:
                result = 'Chave inválida'

        if (escolhas[0],  escolhas[1]) in ganha:
            result = ['win', 0] + escolhas

        elif (escolhas[1], escolhas[0]) in ganha:
            result = ['win', 1] + escolhas

        else:
            result = ['empate', None] + escolhas


c = jokempo()
next(c)
c.send((0, 'papel'))
c.send((1, 'papel'))
