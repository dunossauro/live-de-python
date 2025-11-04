import sys, io

class SuprimePrint:
    def __init__(self):
        self.out = io.StringIO()

    def __enter__(self):
        self.orig = sys.stdout
        sys.stdout = self.out

        # retornei eu mesmo!
        return self

    def __exit__(self, *args):
        sys.stdout = self.orig


print('antes')

with SuprimePrint() as sp:
    print('PEI!')
    print('PEI2!')
    print('PEI3!')
    print('PEI4!')

    a = 7

print('depois')


print(sp.out.getvalue())
print(a)
