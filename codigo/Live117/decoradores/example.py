from functools import wraps

def hook(funcao):

    @wraps(funcao)
    def implementacao(*args, **kwarg):
        aquilo_que_ia_fazer_antes()  # HOOK

        resultado = funcao(*args, **kwarg)

        aquilo_que_ia_fazer_depois()  # HOOK
        return resultado

    return implementacao


def aquilo_que_ia_fazer_antes():
    print('estou antes')

def aquilo_que_ia_fazer_depois():
    print('estou depois')

@hook
def aquilo_que_tenho_que_fazer():
    print('estou no momento')
