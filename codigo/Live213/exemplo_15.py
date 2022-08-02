from datetime import datetime

def debug(*, verbose=False, level=0):

    def intermediaria(func):

        def interna(*args, **kwargs):
            tstart = datetime.now()
            result = func(*args, **kwargs)
            t_final = datetime.now() - tstart
            if verbose:
                print(
                    f'Chamada {func.__name__}\n'
                    f'parâmetros posicionais: {args}\n'
                    f'parâmetros nomeados: {kwargs}\n'
                )
            if level > 0:
                print(f'Resultado: {result}')
            if level > 1:
                print(f'Tempo total: {t_final.total_seconds()}')
            return result
        return interna
    return intermediaria


@debug(verbose=True, level=2)
def soma(x, y):
    return x + y


soma(1, 1)
