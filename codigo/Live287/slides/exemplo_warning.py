from warnings import warn

novo_nome = 'YAY!'

deprecated_names = {'nome_antigo': novo_nome}
__all__ = ['novo_nome']


def __getattr__(name: str):
    if name in deprecated_names:
        swapped_name = deprecated_names[name]
        warn(f'{name!r} está deprecado, use {swapped_name!r}')
        return swapped_name
    else:
        raise AttributeError(f'{name!r} não existe no módulo {__name__}')


def __dir__():
    return __all__ + list(deprecated_names.keys())
