
# 2 + 2 # 4

class vetor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, vetor):
        return (self.x + vetor.x, self.y + vetor.y)

    def __mul__(self, n):
        return (self.x * n, self.y * n)

    def __rmul__(self, n):
        return (self.x * n, self.y * n)

# 2 + 2 - > 2.__add__(2)
# 2 * 2 - > 2.__mul__(2)

# v1 * 3 -> v1.__mul__(3)
# 3 * v1 -> 3.__mul__(v1) -> TypeError
# 3 * v1 -> v1.__rmul__(3) -> (6, 9)


v1 = vetor(2, 3)
# v2 = vetor(2, 2)
#
# #v1 * 3
# print(v1 + v2)
print(3 * v1)
