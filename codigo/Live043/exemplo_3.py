from contextlib import contextmanager
from os import chdir, getcwd


@contextmanager
def cd(path):
    # __enter__
    old_path = getcwd()
    chdir(path)
    yield  # ponto de parada
    chdir(old_path)


print(getcwd())

with cd('/tmp'):
    print(getcwd())

print(getcwd())
