def d():
    return 1/0


def c():
    return d()


def b():
    return c()


def a():
    return b()


print(a())
