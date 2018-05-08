"""
Exemplo básico de objetos serializados em disco.

Criados por nós mesmos
"""
import pickle


class Carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor

    def __repr__(self):
        return f'Carro(modelo="{self.modelo}", cor="{self.cor}")'


carro_1 = Carro('Celta', 'Prata')
carro_2 = Carro('Fusca', 'bege')


with open('carro.pkl', 'wb') as w_file:
    pickle.dump(Carro, w_file)
    pickle.dump(carro_1, w_file)
    pickle.dump(carro_2, w_file)


with open('carro.pkl', 'rb') as r_file:
    car_1 = pickle.load(r_file)
    car_2 = pickle.load(r_file)
    print(car_1, car_2)
