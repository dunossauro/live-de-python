from contextlib import chdir
from os import getcwd

print(getcwd())

with chdir('path'):
    print(getcwd())

print(getcwd())
