"""
1 - Funções nomeadas (def)
2 - Funções Anônimas (lambda)
3 - Funções de classe (class)
"""

def nomeada_soma(x, y):
    return x + y

anonima_soma = lambda x, y: x + y

class classe_soma:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self):
        return self.x + self.y
