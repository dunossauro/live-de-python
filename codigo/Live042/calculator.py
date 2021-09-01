from numbers import Number


def soma(x, y):
    """AOR."""
    return x + y


def invert(x):
    """
    AOD - Delete o operador.
    AOR - Troca o operador
    """
    return -x


def sum_(*vals):
    """
    ASR - Troca o operador de atribuição.
    CRP - Troca as constantes
    """
    result = 0  # aqui
    for val in vals:
        result += val  # Aqui
    return result


def is_number(val):
    """
    COD - Deletar operadores sozinhos (not)
    COI - Insere um operador lógico
    """
    if not isinstance(val, Number):
        return False
    return True


def check_numbers(x, y):
    if is_number(x) and is_number(y):
        return True
    return False
