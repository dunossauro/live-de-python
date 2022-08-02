def soma_1(x):
    return x + 1


def duas_vezes(func, val):
    return func(func(val))


print(duas_vezes(soma_1, 2))  # 4
