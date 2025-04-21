def x(): ...
def y(): ...

__all__ = ['x']


def __dir__():
    return __all__ + ['y']
