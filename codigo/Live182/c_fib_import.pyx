cdef extern from "c_fib.h":
    unsigned long long c_fib(int n)

def fib(n):
    return c_fib(n)
