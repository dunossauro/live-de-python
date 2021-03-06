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

def acha_nomes(text):
    nomes = ('Eduardo', 'Fausto')
    final = text
    for nome in nomes:
        final = final.replace(nome, f'NOME({nome})')

    return final

def acha_verbos(text):
    nomes = ('é',)
    final = text
    for nome in nomes:
        final = final.replace(nome, f'VERBO({nome})')

    return final

def acha_adjetivos(text):
    nomes = ('massa', 'chatão')
    final = text
    for nome in nomes:
        final = final.replace(nome, f'ADJ({nome})')

    return final

texto = '\n\n\n\n Eduardo e Fausto são massa\n\n\n'

p = Pipeline(limpa_texto, acha_nomes, acha_verbos, acha_adjetivos, troca_eh_massa)
print(texto)
print(p(texto))
