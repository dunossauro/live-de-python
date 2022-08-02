def maior_que_5(valor):
    return valor > 5


def positivo(valor):
    return valor > 0


resultado = filter(positivo, [-1, 3, 4, 5, 6, 7])

print(list(resultado))
