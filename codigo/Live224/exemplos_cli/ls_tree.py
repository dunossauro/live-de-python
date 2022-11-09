from pathlib import Path
from rich.console import Console
from rich.tree import Tree


def ls_files(path):
    p = Path(path)
    for path in p.iterdir():
        if path.is_file():
            yield path


def ls_paths(path):
    p = Path(path)
    for path in p.iterdir():
        if path.is_dir() and not str(path).startswith('.'):
            yield path

t = Tree(label='.')

path = t.add(':open_file_folder:')

for x in ls_files('.'):
    path.add(f':pencil: {x}')

for dire in ls_paths('.'):
    t_dir = t.add(f':open_file_folder: {dire}')
    for x in ls_files(dire):
        t_dir.add(f':pencil: {x}')

c = Console()

c.print(t)
