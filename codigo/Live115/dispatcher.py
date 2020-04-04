from functools import singledispatch


class Cor:
    ...


class Verde(Cor):
    ...


class Roxo(Cor):
    ...


class Amarelo(Cor):
    ...


@singledispatch
def paul(evento):
    return 'default'


@paul.register(Verde)
def entregar_unicornio(evento):
    return 'Enviado para unicório'


@paul.register(Amarelo)
def entregar_centauro(evento):
    return 'Enviado para centauro'


@paul.register(Roxo)
def entregar_fausto(evento):
    return 'Enviado para Fausto'
