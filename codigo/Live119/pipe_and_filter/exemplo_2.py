from typing import Text
from functools import partial


class Pipeline:
    def __init__(self, *filters):
        self.filters = filters

    def __call__(self, value):
        final_value = value
        for filter in self.filters:
            final_value = filter(final_value)

        return final_value


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

ans_morfologica = Pipeline(
    trocar_massa, achar_adjetivos, achar_verbos, achar_nome, limpa_texto
)

print(ans_morfologica(texto))
