import os

if os.name == 'nt':
    filename = r'\\files\\pasta_0\\arquivo_1.txt'
else:
    filename = 'files/pasta_0/arquivo_1.txt'


with open(filename) as file:
    print(file.read())


from pathlib import Path

path_atual = Path()
pasta_0 = path_atual / 'files' / 'pasta_0'
arquivo_0 = pasta_0 / 'arquivo_0.txt'

arquivo_0.exists()  # True
arquivo_0.is_file  # True

arquivo_0.suffix  # .txt
arquivo_0.stem  # arquivo_0

arquivo_0.read_text()
# 'files/pasta_0/arquivo_0.txt'
