# exemplo_getattr.py
novo_nome = 'YAY!'

def __getattr__(nome: str):
    print(nome)
    if nome == 'nome_antigo':
        return novo_nome
    else:
        raise AttributeError(f'{nome} não existe no módulo {__name__}')
