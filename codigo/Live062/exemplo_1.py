class Fila:
    c_fila = []

    @classmethod
    def c_entrar(cls, obj):
        cls.c_fila.append(obj)
        print(cls.c_fila)

    def __init__(self):
        self.s_fila = []

    def s_entrar(self, obj):
        self.s_fila.append(obj)
        print(self.s_fila)
