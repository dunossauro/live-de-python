from pathlib import Path

files = Path('files')
PATH = 'pasta_{}/'
FILE = 'arquivo_{}.txt'

files.mkdir()

for value_path in range(10):
    pasta = files / PATH.format(value_path)
    pasta.mkdir()
    for value_file in range(10):
        arquivo = pasta / FILE.format(value_file)
        arquivo.write_text(str(arquivo))

