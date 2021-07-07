cor = (255, 255, 255)
# cor = (255, 255, 255, 255)

match cor:
    case r, g, b if r == 255:
        print(f'Tá muito vermelho!!!!!')
    case r, g, b:  # len(3)
        print(f'{r=}, {g=}, {b=}')
    case r, g, b, a:  # len(4)
        print(f'Com alpha: {r=}, {g=}, {b=}, {a=}')
    case r, g, b, a, *_:  # len(5)
        print(f'Com alpha: {r=}, {g=}, {b=}, {a=}')
