import sys
from traceback import print_stack

def my_trace_function(frame, event, arg):
    print(
        frame.f_lineno,
        frame.f_code.co_name,
        frame.f_locals,
        event,
    )
    #print_stack(frame)
    return my_trace_function


def primeira_função():
    lista_original = [1, 2, 3, 4]
    nova_lista = []

    for valor in lista_original:
        nova_lista.append(segunda_função(valor))


def segunda_função(valor):
    retorno = valor * 2
    return retorno


sys.settrace(my_trace_function)
#primeira_função()
