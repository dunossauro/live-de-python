from pathlib import Path
from shutil import rmtree

output_path = Path('desafio_2')

if output_path.exists():
    # Sim, não tem rmtree na pathlib :(
    rmtree(output_path)

output_path.mkdir()

for file in Path('files/pasta_0').glob('*.txt'):
    new_file = output_path / file.name
    new_file.write_text(file.read_text())
