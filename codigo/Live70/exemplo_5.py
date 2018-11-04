class Retangulo:
    def __init__(self, l, a):
        self.l = l
        self.a = a

    @property
    def area(self):
        return self.a * self.l
