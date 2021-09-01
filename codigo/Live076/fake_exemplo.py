"""Exemplo do dublê Fake."""


class Pedido:
    def __init__(self, valor, frete, usuario):
        self.valor = valor
        self.frete = frete
        self.usuario = usuario

    @property
    def resumo(self):
        """Informações gerais sobre o pedido."""
        return f'''
        Pedido por: {self.usuario.nome_completo}
        Valor: {self.valor}
        Frete: {self.frete}
        '''


class FakePessoa:
    @property
    def nome_completo(self):
        return 'Eduardo Mendes'


Pedido(100.00, 13.00, FakePessoa()).resumo
