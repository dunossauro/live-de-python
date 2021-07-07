def movimento(ação: str):
    match ação.split():
        case 'pular':
            return 'Pulando'
        case ['mover', 'direita' | 'esquerda' as direção]:
            return f'Movendo horizontalmente para {direção}'
        case ['mover', 'cima' | 'baixo' as direção]:
            return f'Movendo verticalmente para {direção}'
        case _:
            return 'Não sei o que aconteceu'

print(movimento(1))
