import sys, io
from contextlib import contextmanager


@contextmanager
def suprime_print():
    out = io.StringIO()
    original_stdout = sys.stdout
    sys.stdout = out

    try:
        yield out

    finally:
        sys.stdout = original_stdout

with suprime_print() as sp:
    print('batatinha')
    1 / 0


print('pei!')


