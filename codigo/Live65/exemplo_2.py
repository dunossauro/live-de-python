class Número:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print(other)
        return self.val + other

    def __sub__(self, other):
        ...

    def __lt__(self, other):
        ...
