from functools import reduce


def soma(x, y):
    return x + y


resultado = reduce(soma, [1, 2, 3, 4, 5])

print(resultado)  # 15
