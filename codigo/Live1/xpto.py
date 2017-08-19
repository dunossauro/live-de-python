def eh_par(val: int) -> bool:
    """
    Função que verifica se numero é par.

    Arg:
        - val: Valor de entrada do tipo inteiro
    """
    if isinstance(val, int) or isinstance(val, float):
        return True if val % 2 == 0 else False
    else:
        return False
