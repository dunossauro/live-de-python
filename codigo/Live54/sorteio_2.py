from random import choice
with open('nomes.txt') as f:
    print(choice(f.readlines()))
