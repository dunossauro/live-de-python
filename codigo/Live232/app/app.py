"""
Esse programa faz conversões.
"""


def converte_F_para_C(temperatura):
    """
    Testes:

    >>> converte_F_para_C(32)
    0.0

    >>> converte_F_para_C(-40)
    -40.0
    """
    return ((temperatura - 32) / 9) * 5


def converte_C_para_F(temperatura):
    return temperatura * (9 / 5) + 32
