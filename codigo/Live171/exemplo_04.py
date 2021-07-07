d = {'a': 1, 'c': 3}

match d:
    case {'a': chave_a, 'b': _}:
        print(f'chave A {chave_a=} + chave B')
    case {'a': _} | {'c': _}:
        print('chave A ou C')
    case {}:
        print('vazio')
    case _:
        print('Não sei')
