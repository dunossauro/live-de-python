"""Comparação do pickle com json."""
import json


class Carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor

    def __repr__(self):
        return f'Carro(modelo="{self.modelo}", cor="{self.cor}")'


carro_1 = Carro('Celta', 'Prata')
carro_2 = Carro('Fusca', 'bege')

obj = json.dumps({'carro': 'carro_1'})
