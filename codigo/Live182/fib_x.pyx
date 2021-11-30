cpdef int fib(int n):
    cdef int i
    cdef unsigned long long int a = 0
    cdef unsigned long long int b = 1


    for i in range(n):
        a, b = a + b, a

    return a
