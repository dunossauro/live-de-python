from timeit import timeit

py = timeit('fib(93)', number=1_000_000, setup='from fib_py import fib')
cy = timeit('fib(93)', number=1_000_000, setup='from fib_cy import fib')
px = timeit('fib(93)', number=1_000_000, setup='from fib_x import fib')
cc = timeit('fib(93)', number=1_000_000, setup='from c_fib_import import fib')

print('Python Puro', py)
print('Cython/Python', cy)
print('Cython Puro', px)
print('C Puro', cc)
print(f'{py/cy=}')
print(f'{py/px=}')
print(f'{py/cc=}')
print(f'{cy/cc=}')
print(f'{px/cc=}')
