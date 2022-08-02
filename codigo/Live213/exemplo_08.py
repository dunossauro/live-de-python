from functools import partial


def soma(x, y):
    return x + y


def mul(x, y):
    return x * y


def zip_with_2(func):
    return partial(map, func)


zip_soma = zip_with_2(soma)
zip_mul = zip_with_2(mul)

print(list(
    zip_soma([1, 2, 3], [1, 2, 3])
))  # [2, 4, 6]
print(list(
    zip_mul([1, 2, 3], [1, 2, 3])
))  # [1, 4, 9]
