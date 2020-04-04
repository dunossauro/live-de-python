from functools import singledispatch

class Amarelo:
    ...

class Verde:
    ...

class Roxo:
    ...

@singledispatch
def paul(evento):
    print(f'Paul se perdeu com {evento}')


@paul.register
def mandar_para_centauro(evento: Roxo):
    print('Centauro recebeu a cor roxa')

@paul.register(Amarelo)
def mandar_para_fausto(evento):
    print('Fausto recebeu a cor Aamarela')

@paul.register(Verde)
def mandar_para_unicornio(evento):
    print('Unicornio recebeu a cor Verde')
