from collections import deque

cache_values = deque(maxlen=3)


def cache(func):
    def inner(*args):
        cache_values.append(args)
        return func(*args)
    return inner


@cache
def soma(x, y):
    return x + y
