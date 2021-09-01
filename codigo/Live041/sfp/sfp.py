"""SFP - Simple Functional Programming."""


def head(iterable):
    return next(iter(iterable))


def last(iterable):
    for x in iterable:
        pass
    return x


def number(numero):
    if numero == 1:
        return 'Um'
    elif numero == 2:
        return 'Dois'
    elif numero == 3:
        return 'Três'
    elif numero == 4:
        return 'Quatro'
    elif numero == 5:
        return 'Cinco'
    elif numero == 6:
        return 'seis'
    elif numero == 7:
        return 'sete'
    else:
        return 'Não sei resolver'
