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


sp = SuprimePrint()

sp.__enter__()

print('pei!')
sp.__exit__()

print('pei fim!')
