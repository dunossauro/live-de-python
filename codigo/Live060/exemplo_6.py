class MeuErro(Exception):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return f'Meu erro foi crer que estar ao seu lado bastaria: {self.msg}'


raise MeuErro('Batatinha quando nasce')
