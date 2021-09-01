# Mais exemplos na live 5
from pdb import post_mortem
from sys import exc_info


def xpto_externo():
    bananas = 'pijamas'
    try:
        xpto()
    except:
        errors = exc_info()
        print(errors)
        post_mortem(errors[2])


def xpto():
    a = 1
    b = 2
    assert a == b


xpto_externo()
