import pickle


class Carro:
    pass


with open('carro.pkl', 'rb') as r_file:
    car_1 = pickle.load(r_file)
    car_2 = pickle.load(r_file)
    print(car_1, car_2)
