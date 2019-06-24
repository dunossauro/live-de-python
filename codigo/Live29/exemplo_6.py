class Pessoa:
    def __init__(self, n, s):
        self.n = n
        self.s = s

    def __hash__(self):
        return hash((self.n,self.s))

ll = Pessoa('Lugão','Ricardo')

lulu = Pessoa('Lugão','Ricardinho')

print(hash(ll)) # True
print(hash(lulu)) # True
