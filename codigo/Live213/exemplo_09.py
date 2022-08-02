def ola(nome):

    def func_interna(nome):
        if nome.lower() == 'marilene':
            print(f'Olá {nome}. A noite, tainha, vinho e muito ...')
        else:
            print(f'Olá {nome}, boas vindas!')

    func_interna(nome)


ola('Marilene')
