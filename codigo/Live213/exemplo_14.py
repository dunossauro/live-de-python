from time import sleep

def retry(erro, vezes, tempo):
    count = 0

    def intermediaria(func):

        def closure(*args, **kwargs):
            nonlocal count

            try:
                return func(*args, **kwargs)
            except erro as e:
                count += 1
                print(f'{func.__name__} error: {e} retry: {count}')
                if count < vezes:
                    sleep(tempo)
                    return closure(*args, **kwargs)

        return closure
    return intermediaria


@retry(ZeroDivisionError, 5, 3)
def div(x, y):
    return x / y


div(3, 0)
