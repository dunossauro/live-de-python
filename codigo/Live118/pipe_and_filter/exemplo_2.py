from functools import partial


class Pipeline:
    def __init__(self, *filters):
        self.filters = filters

    def __call__(self, value):
        final_value = value
        for filter in self.filters:
            final_value = filter(final_value)

        return final_value

def limpa_texto(text):
    return text.replace('\n', '')

def troca_eh_massa(text):
    return text.replace('massa', 'chatão')


def acha(text, palavras, troca):
    final = text
    for nome in palavras:
        final = final.replace(nome, troca.format(nome))

    return final


acha_nomes = partial(acha, palavras=('Eduardo', 'Fausto'), troca='NOME({})')
acha_verbos = partial(acha, palavras=('é', 'são'), troca='VERBO({})')
acha_adjetivos = partial(acha, palavras=('massa', 'chatão'), troca='ADJ({})')


texto = '\n\n\n\n Eduardo e Fausto são massa\n\n\n'

p = Pipeline(limpa_texto, acha_nomes, acha_verbos, acha_adjetivos)
print(texto)
print(p(texto))
