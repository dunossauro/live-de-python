import pickle

class Carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor

    def __repr__(self):
        return f'Carro(modelo="{self.modelo}", cor="{self.cor}")'


carro_1 = Carro('Celta', 'Prata')

data = {
    'a': 'Eduardo',
    'b': 'Banans',
    'c': [1, 2, 3, 4],
    'd': {1, 2, 3, 4},
    'car': carro_1
}

dumped_data = pickle.dumps(data)
xpto = pickle.loads(dumped_data)
