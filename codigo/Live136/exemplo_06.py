from functools import reduce
from operator import mul, add


reduce(add, [1,2,3,4,5]) == 15
reduce(mul, [1,2,3,4,5]) == 120
reduce('FUNC', [1,2,3,4,5]) == 120


# ((((1 + 2) + 3) + 4) + 5)
# ((((1 * 2) * 3) * 4) * 5)
# FUNC(FUNC(1, 2), 3)

def xpto(t1, t2):
    return t1 + t2


# reduce(xpto, [(1, 2), (2, 3)]
