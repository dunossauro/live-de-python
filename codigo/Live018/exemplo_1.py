from pprint import pprint

# 1
A = list(range(2, 11)) + 'Q J K A'.split()
B = ['E', 'O', 'P', 'C']

baralho = {(carta, naipe)
           for carta in A
           for naipe in B}

# for c in baralho:
#     pprint(c)

# 2
baralho = {(carta, naipe)
           for carta in A
           for naipe in B if naipe == 'C'}

# pprint(baralho)

# 3
baralho = {(carta, naipe)
           for carta in A
           for naipe in B if carta == 'K'}

# pprint(baralho)

# 4
print([(lambda x: x*2)(x) for x in [2,3,3,4]])
