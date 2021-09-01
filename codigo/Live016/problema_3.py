import os
import os.path
import shutil
from pathlib import Path

for x in range(1, 11):
    dir_ = 'pasta_{}'.format(x)
    if not os.path.exists(dir_):
        os.mkdir(dir_)

l = [path for path in os.listdir('.')
     if os.path.isdir(path) and path != 'aulinha_1']

for path in l:
    Path(os.path.join(path, 'arquivo_1.txt')).touch()
    Path(os.path.join(path, 'arquivo_2.txt')).touch()

for val in os.walk('.'):
    print(val)
