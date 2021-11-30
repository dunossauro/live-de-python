from random import randint
from fib_cy import fib

numeros = [randint(0, 93) for _ in range(100_000)]

for n in numeros:
    fib(n)
