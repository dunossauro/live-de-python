def soma(x, y):
    return x + y

def mul(x, y):
    return x * y


def zip_with(func, iter_a, iter_b):
    return list(map(func, iter_a, iter_b))


print(zip_with(soma, [1, 2, 3], [1, 2, 3]))
# [2, 4, 6]

print(zip_with(mul, [1, 2, 3], [1, 2, 3]))
# [1, 4, 9]
