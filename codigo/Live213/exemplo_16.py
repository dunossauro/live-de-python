from functools import wraps


def retry(erro, vezes):
    count = 0

    def intermediaria(func):
        @wraps(func)
        def closure(*args, **kwargs):
            nonlocal count

            try:
                return func(*args, **kwargs)
            except erro as e:
                count += 1
                print(f'{func.__name__} error: {e} retry: {count}')
                if count < vezes:
                    return closure(*args, **kwargs)

        return closure
    return intermediaria


@retry(ZeroDivisionError, 5)
def div(x, y):
    return x / y


div(3, 0)
