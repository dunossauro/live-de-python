from itertools import count


def _in(val, seq):
    """__contains__."""
    c = count()
    for el in seq:
        print(next(c))
        if el == val:
            return True
    return False
