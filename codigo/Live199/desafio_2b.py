from pathlib3x import Path

output_path = Path('desafio_2')
output_path.rmtree(ignore_errors=True)
output_path.mkdir()

for file in Path('files/pasta_0').glob('*.txt'):
    new_file = output_path / file.name
    file.copy(new_file)
