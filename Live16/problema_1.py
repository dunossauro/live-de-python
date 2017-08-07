import os
import os.path
import shutil
from pathlib import Path

# Criar path caso ele não exista
if not os.path.exists('aulinha_1'):
    os.mkdir('aulinha_1')

os.chdir('aulinha_1')

# Criar arquivo xpto
Path('xpto.txt').touch()

for el in range(1, 4):
    shutil.copy('xpto.txt', f'xpto_{el}.txt')

# print(os.getcwd())

# Assertiva
assert len(os.listdir('.')) == 4
