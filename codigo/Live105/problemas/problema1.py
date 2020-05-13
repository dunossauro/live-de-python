def maior(x, y):
    '''problema 1.'''
    if x < y:
        return y
    return x


def é_vogal(letra):
    '''problema 2.'''
    vogais = 'a e i o u'.split()
    if letra.lower() in vogais:
        return 'vogal'
    return 'consoante'
