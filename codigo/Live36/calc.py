from argparse import ArgumentParser

parser = ArgumentParser(prog='calculadora',
                        description='Olá BB, isso é uma calculadora',
                        fromfile_prefix_chars='@')

parser.add_argument('operação', type=str,
                    help='Como o bb gostaria de usar?')
parser.add_argument('x', type=int,
                    help='Primeiro valor')
parser.add_argument('y', type=int,
                    help='Segundo valor')
parser.add_argument('-v', '--verbose', action='count',
                    help='Entenda o que estamos fazendo', default=0)

args = parser.parse_args()


def verbose(func):
    def _inner(x, y):
        if args.verbose == 1:
            print(f'Estamos operando com {x} e {y}')
        if args.verbose == 2:
            print(f'{func.__name__}({x} e {y})')
        if args.verbose >= 10:
            print('Vá se danar com tanta verbosidade')
            exit()
        return func(x, y)
    return _inner


@verbose
def soma(x, y):
    return x + y


@verbose
def subtração(x, y):
    return x - y


@verbose
def divisão(x, y):
    return x / y


@verbose
def multiplicação(x, y):
    return x * y


if __name__ == '__main__':
    operações = {'soma': soma,
                 'subtração': subtração,
                 'divisão': divisão,
                 'multiplicação': multiplicação}
    print(operações[args.operação](args.x, args.y))
