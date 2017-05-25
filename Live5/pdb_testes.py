import pdb
from testes_simples import validate
from operator import add

# TODO: criar relações de comandos
# step: entra na função/classe
# next: avança uma linha
# up: sobe um nível do estado atual
# down: Desce um nível do estado atual
# where: localiza onde estamos entre todos os módulos

# def soma(x: int, y: int) -> int:
#     return add(x, y)
# soma(2, 2)

def div(x, y):
    return validate(x, y)

try:
    div(2, 0)
except Exception:
    # raise Exception('Não divido por zero, nem a pau')
    from sys import exc_info
    pdb.post_mortem(exc_info()[2])
