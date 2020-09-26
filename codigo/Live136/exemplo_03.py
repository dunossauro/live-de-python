from functools import partial

def exp(x, y):
    return x ** y


quadrado = partial(exp, 2)
cubo = partial(exp, 3)
quarta = partial(exp, 4)
quinta = partial(exp, 5)
