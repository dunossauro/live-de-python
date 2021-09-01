from collections import deque


def tail(filename, n=10):
    with open(filename) as f:
        return deque(f, n)
