def externa(func):
    def interna(x, y):
        return func(x, y)
    return interna


@externa
def soma(x, y):
    return x + y

print(soma(2,2))
