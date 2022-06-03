from timeit import timeit

print(
    timeit('"".join(str(x) for x in range(100))')
)
