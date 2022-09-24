def func_a(x):
    assert False
    return x + 2


def func_b(y):
    return func_a(y) - 3

val = 7

val_2 = func_b(val)

print(val_2)
