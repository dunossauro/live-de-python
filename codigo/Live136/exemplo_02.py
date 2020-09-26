from operator import add, mul, sub, floordiv

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def case_operator(op):
    return {
        '+': add,
        '-': sub,
        '*': mul,
        '/': floordiv
    }[op]


case_operator('+')(1, 2)
case_operator('-')(1, 2)
