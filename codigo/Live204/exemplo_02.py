from timeit import timeit


def teste_if_igual():
    l = []

    if l == []:
        ...


def teste_if():
    l = []

    if l:
        ...


# print(
#     timeit('teste_if_igual()', globals=globals(), number=10_000)
# )

# print(
#     timeit('teste_if()', globals=globals(), number=10_000)
# )
