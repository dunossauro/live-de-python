from pathlib import Path
from tempfile import TemporaryDirectory


with TemporaryDirectory() as temp_dir:
    print(temp_dir)
    arquivo = Path(temp_dir) / 'batatinhas.txt'
    arquivo.write_text('Paulo Braga')

    breakpoint()
