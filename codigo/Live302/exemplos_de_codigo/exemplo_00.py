from contextlib import suppress


with suppress(Exception):
    1 / 0
    a + 1
    x.append(1)


print('Depois do erro! fora do contexto!')
