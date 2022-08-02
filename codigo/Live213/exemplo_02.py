def soma(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


def calculadora(op, x, y):
    operações = {
        '+': soma,
        '-': sub,
        '*': mul,
        '/': div
    }
    return operações[op](x, y)
