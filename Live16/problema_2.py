import os
import os.path
import shutil
from pathlib import Path

# Criando arquivos
for el in range(1, 11):
    Path('live_{}.txt'.format(el)).touch()

l = [f for f in os.listdir('.') if f.startswith('live_')]

# Removendo arquivos menores ou iguais a 5
for _file in l:
    if int(_file.partition('_')[2][0]) <= 5:
        os.remove(_file)

l = [f for f in os.listdir('.') if f.startswith('live_')]

# Alterando os valores restantes
for val, el in enumerate(sorted(l), 1):
    shutil.move(el, 'live_{}'.format(val))

l = [f for f in os.listdir('.') if f.startswith('live_')]
print(l)
