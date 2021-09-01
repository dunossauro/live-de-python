from os.path import exists

def read_file(file):
    try:
        return open(file)
    except Exception:
        raise FileNotFoundError(f'Arquivo {file} não existe')


read_file('bananinhas')
