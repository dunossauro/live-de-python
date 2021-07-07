# valor = 2

lista = ['2', 7, 5]

match lista:
    case [] | [_]:
        print('Vazio ou somente com 1')

    case [1, *resto]:
        print(f'O primeiro é 1 e o {resto=}')

    case [1|'2', _, _] | [_, 1|2, _]:
        print('Inicia com 1 ou 2')


# match valor:
#     case 1 | 2:
#         print('1 ou 2')
