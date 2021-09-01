from collections import ChainMap
# problema: Unir dois dicionário
a = {1: 'a', 2: 'b', 3: 'c'}
b = {2: 'x', 3: 'z', 4: 'w'}

c = ChainMap(a, b)
