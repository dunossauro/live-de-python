def corrotina(func):
    def preparação(*args, **kwargs):
        coro = func(*args, **kwargs)
        next(coro)
        return coro
    return preparação
