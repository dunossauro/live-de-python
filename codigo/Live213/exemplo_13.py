def decorador(func):

    def interna(*args):
        resultado = func(*args)
        return f'Sou uma closure e sua função retorou {resultado}'


    return interna


@decorador
def soma(x, y):
    return x + y


@decorador
def inverte(text):
    return text[::-1]



# print(decorada(1, 2))

# print(soma(1, 2))
