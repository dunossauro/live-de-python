
# função nomeada
def div(x, y):
    """
    Função que soma dois valores.
    """
    return x / y

# função anônima
# 'f(x) | x + 2'
soma_2 = lambda x: x + 2

# print(soma_2(2))

# função como classe
class classe_soma:
    def __call__(self, x, y):
        return x + y


print(classe_soma(2, 2))
