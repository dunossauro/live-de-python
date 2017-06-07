
# 2 + 2 # 4

class vetor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, vetor):
        return (self.x + vetor.x, self.y + vetor.y)

    def __mul__(self, n):
        return (self.x * n, self.y * n)

# v1 = vetor(2, 3)
# v2 = vetor(2, 2)
#
# #v1 * 3
# print(v1 + v2)
# print(v1 * v2)
