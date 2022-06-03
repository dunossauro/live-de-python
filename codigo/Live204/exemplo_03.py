from memory_profiler import profile
from time import sleep

@profile
def carregar_arquivo():
    with open('br-utf8.txt') as file:
        conteudo = file.read()

    return conteudo


@profile
def carregar_arquivo_em_lista():
    with open('br-utf8.txt') as file:
        conteudo = file.readlines()

    return conteudo


@profile
def join(a, b):
    return list(a) + list(b)


a = carregar_arquivo()
b = carregar_arquivo_em_lista()
sleep(3)
c = carregar_arquivo_em_lista()
del b
sleep(3)
d = carregar_arquivo()

e = join(c, d)
