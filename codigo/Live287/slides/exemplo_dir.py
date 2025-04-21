novo_nome = 'YAY!'

deprecated_names = {'nome_antigo': novo_nome}
__all__ = ['novo_nome']


def __dir__():
    return __all__ + list(deprecated_names.keys())
