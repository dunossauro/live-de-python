# cython: profile=True
import cython


def fib(n: cython.int):

    i: cython.int
    a: cython.ulonglongint = 0
    b: cython.ulonglongint = 1

    for i in range(n):
        a, b = a + b, a

    return a
