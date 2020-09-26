from functools import singledispatch

@singledispatch
def mostra_tipo(val):
    raise ValueError('Não sei esse tipo')


@mostra_tipo.register
def _(val: int):
    print('É um valor inteiro')


@mostra_tipo.register(list)
@mostra_tipo.register(tuple)
@mostra_tipo.register(set)
def _(val):
    print('É uma lista')


@mostra_tipo.register(dict)
def _(val):
    print('É um dicionario')
