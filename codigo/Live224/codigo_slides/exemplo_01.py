"""
Exemplo 01

O poder dos formatadores do rich
"""
from rich import print

texto = '''
[i]Boas [s]vindas[/i][/s] [d]a[/d] [b]Live de [u]Python[/b][/u]!

[r]Live [blink]Rich[/blink][/]
'''

print(texto)
