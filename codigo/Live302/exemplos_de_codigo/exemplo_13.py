from contextlib import contextmanager


@contextmanager
def context(batata):
    # __enter__
    print('entrei!')

    yield 42, batata

    # __exit__
    print('saí!')


with context('123') as c:
    print('dentro', c)
