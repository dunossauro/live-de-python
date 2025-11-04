class ManipulaArquivo:
    def __init__(self, target):
        self.target = target

    def __enter__(self):
        # retorna o arquivo para ser manipulado
        self.f = open(self.target)
        return self.f

    def __exit__(self, exc_type, exc_value, tb):
        self.f.close()


ma = ManipulaArquivo('exemplo_10.py')
        
with ma as f:
    print(f.read())

with ma as f:
    print(f.read())
