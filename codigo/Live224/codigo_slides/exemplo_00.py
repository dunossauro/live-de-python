"""
Exemplo 00.

Subistituindo o print tradicional do python pelo print do rich
"""
import rich

l = [1, 2, 3, 4]
d = {'nome': 'Eduard', 'idade': 29, 'hobbies': ['Fazer Lives']}

print(l)
print(d)

rich.print(l)
rich.print(d)
