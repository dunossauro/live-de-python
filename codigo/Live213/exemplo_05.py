from functools import partial


def soma(x, y):
    return x + y


soma_1 = partial(soma, 1)
soma_10 = partial(soma, 10)

print(soma_1(10))  # 11
print(soma_10(11))  # 21
