from itertools import product

sizes = ["P", "M", "G"]
colors = ["vermelho", "verde", "azul"]

for combination in product(sizes, colors):
    print(combination)
