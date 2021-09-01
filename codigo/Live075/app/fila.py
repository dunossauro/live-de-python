class Fila:
    """
    -> entrar:
        Entra sempre no final
    -> sair:
        Sai sempre do começo
    """
    def __init__(self):
        self.dado = []

    def entrar(self, valor):
        self.dado.append(valor)

    def __getitem__(self, pos: int):
        return self.dado[pos]

    def __repr__(self):
        return f'{self.dado}'
