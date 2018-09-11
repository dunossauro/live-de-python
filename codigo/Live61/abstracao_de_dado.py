class Fila:

    def __init__(self):
        self.fila = []

    def entrar(self, nome):
        self.fila.append(nome)

    def sair(self):
        self.fila.pop(0)
