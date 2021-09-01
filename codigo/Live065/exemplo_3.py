class Número:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('__add__')
        return self.val + other

    def __radd__(self, other):
        print('__radd__')
        return self.val + other
