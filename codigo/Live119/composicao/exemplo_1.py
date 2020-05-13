from typing import Text
from functools import partial


def compose(*funcs):

    def interna(value):
        final_value = value
        for func in reversed(funcs):
            final_value = func(final_value)

        return final_value

    return interna


def limpa_texto(texto: Text):
    return texto.replace('\n', '')


def trocar_massa(texto: Text):
    return texto.replace('massa', 'chatão')


def achar(texto, palavras, troca):
    nomes = palavras
    final_value = texto
    for nome in nomes:
        final_value = final_value.replace(nome, troca.format(nome))

    return final_value


achar_nome = partial(achar, palavras=('Eduardo', 'Fausto'), troca='NOME({})')
achar_verbos = partial(achar, palavras=('é', ), troca='VERBO({})')
achar_adjetivos = partial(achar, palavras=('massa', 'chatão'), troca='ADJ({})')


texto = "\n\n\n\n Eduardo é massa\n\n\n"

ans_morfologica = compose(
    trocar_massa, achar_adjetivos, achar_verbos, achar_nome, limpa_texto
)

print(ans_morfologica(texto))
