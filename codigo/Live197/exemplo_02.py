def função_a():
    return ...


def função_b():
    return função_a()


def função_c():
    return função_b()


def função_d():
    return função_c()


breakpoint()

função_d()

print('FIM!')
