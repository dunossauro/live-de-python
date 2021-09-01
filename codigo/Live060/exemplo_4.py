from os.path import exists

def read_file(file):
    if not exists(file):
        raise FileNotFoundError(f'Arquivo {file} não existe')


try:
    read_file('bananas.txt')
except FileNotFoundError:
    print('ih, deu ruim')
