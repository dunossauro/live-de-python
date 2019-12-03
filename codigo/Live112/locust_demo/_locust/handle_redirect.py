import functools


def redirect_handle(_func):

    @functools.wraps(_func)
    def wrapper(_self):
        func = _func(_self)
        if func and func.history and func.history[0].status_code == 302:
            func.failure(f'{func.history[0].status_code}'
                         f' - houve redirect. Verifique cookie')
            return
    return wrapper
