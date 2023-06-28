from statistics import mean
from itertools import zip_longest

ES = (22, 26, 18)
MG = (16, 20, 29, 18, 14)
RJ = (22, 17, 26, 19, 24)
SP = (31, 27, 29, 17, 19)

for dia in zip(ES, MG, RJ, SP):
    print(mean(dia))  # 22.75, 22.5, 25.5


for dia in zip_longest(ES, MG, RJ, SP, fillvalue=None):
    print(mean(filter(None, dia)))
    # 22.75, 22.5, 25.5, 18 19
