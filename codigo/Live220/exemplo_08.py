from sys import platform


try:
    1/0
except ZeroDivisionError as zde:
    if platform == 'linux':
        zde.add_note(
            'Divisão por zero, não funciona no Linux'
        )
    zde.add_note("""
    Não divida por zero, veja mais em:
    https://pt.wikipedia.org/wiki/Divis%C3%A3o_por_zero
    """)
    print(zde.__notes__)
    raise
