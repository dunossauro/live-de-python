from timeit import timeit


def append_em_lista():
    nova_lista = []

    for el in range(1_000):
        nova_lista.append(el ** 2 ** 6 / 3)

    return nova_lista


def list_comp():
    return [el ** 2 ** 6 / 3 for el in range(1_000)]


print(
    'append',
    timeit("append_em_lista()", globals=globals(), number=10_000)
)

print(
    'list_comp',
    timeit("list_comp()", globals=globals(), number=10_000)
)
