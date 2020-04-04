from typing import Text


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


def achar_nome(texto: Text):
    nomes = ('Eduardo', 'Fausto')
    final_value = texto
    for nome in nomes:
        final_value = final_value.replace(nome, f'NOME({nome})')

    return final_value

def achar_verbos(texto: Text):
    nomes = ('é', )
    final_value = texto
    for nome in nomes:
        final_value = final_value.replace(nome, f'VERBO({nome})')

    return final_value

def achar_adjetivos(texto: Text):
    nomes = ('massa', 'chatão')
    final_value = texto
    for nome in nomes:
        final_value = final_value.replace(nome, f'ADJ({nome})')

    return final_value

def trocar_massa(texto: Text):
    return texto.replace('massa', 'chatão')


texto = "\n\n\n\n Eduardo é massa\n\n\n"

print(texto)
ans_morfologica = Pipeline(
    trocar_massa, achar_adjetivos, achar_verbos, achar_nome, limpa_texto
)

# print(
#     trocar_massa(
#         achar_adjetivos(
#             achar_verbos(
#                 achar_nome(
#                     limpa_texto(texto)
#                 )
#             )
#         )
#     )
# )

print(ans_morfologica(texto))
