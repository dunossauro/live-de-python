from warnings import warn

novo = 'YAY!'
__velho = 'YOW'
deprecateds = {'velho': __velho}

__all__ = ['novo']


def __getattr__(name: str):
    print(name)
    if name in deprecateds.keys():
        warn('Velho mudou, chame novo!')
        return deprecateds[name]
    else:
        raise AttributeError('Deu ruim!')


def __dir__() -> list[str]:
    return __all__ + list(deprecateds.keys())
