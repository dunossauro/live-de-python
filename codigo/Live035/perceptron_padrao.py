import csv
import random

# Carrega os valores do dataset para serem manipulados
dataset = []
with open('data.csv') as _file:
    data = csv.reader(_file, delimiter=',')
    for line in data:
        line = [float(elemento) for elemento in line]
        dataset.append(line)


def treino_teste_split(dataset, porcentagem):
    """ 
    Separa e monta o conjunto principal 
    em dois para teste e treino. 
    """
    percent = porcentagem*len(dataset) // 100
    data_treino = random.sample(dataset, percent)
    data_teste = [data for data in dataset if data not in data_treino]

    def montar(dataset):
        x, y = [], []
        for data in dataset:
            x.append(data[1:3])
            y.append(data[0])
        return x, y

    x_train, y_train = montar(data_treino)
    x_test, y_test = montar(data_teste)
    return x_train, y_train, x_test, y_test


def sinal(u):
    """ Retorna a classe baseada no valor de u. """
    return 1 if u >= 0 else -1

def ajuste(w, x, d, y):
    """ Define a taxa de aprendizagem e ajusta o valor do w. """
    taxa_aprendiz = 0.01
    return w + taxa_aprendiz * (d - y) * x

def perceptron_fit(x, d):
    """ Executa o treinamento da rede """
    epoca = 0
    w = [random.random() for i in range(3)]
    print(w)
    while True:
        erro = False
        for i in range(len(x)):
            u = sum([w[0]*-1, w[1]*x[i][0], w[2]*x[i][1]])
            y = sinal(u)
            if y != d[i]:
                w[0] = ajuste(w[0], -1, d[i], y)
                w[1] = ajuste(w[1], x[i][0], d[i], y)
                w[2] = ajuste(w[2], x[i][1], d[i], y)
                erro = True
        epoca += 1
        if erro is False or epoca == 1000:
            break 
    print(epoca)
    return w


def perceptron_predict(x_teste, w_ajustado):
    """ 
    Valida o treino de acordo com o w ajustado 
    e as variáveis atributo do conjunto de 
    teste.
    """
    y_predict = []
    for i in range(len(x_teste)):
        predict = sum([w_ajustado[0]*-1, w_ajustado[1]*x_teste[i][0], w_ajustado[2]*x_teste[i][1]])
        y_predict.append(sinal(predict))
    return y_predict


def acuracia(y_teste, y_validado):
    """ 
    Retorna um valor entre 0 e 1
    que representa a porcentagem 
    de acertos da rede.
    """
    total = 0
    for i in range(len(y_teste)):
        if y_teste[i] == y_validado[i]:
            total += 1
        else:
            pass
    return total / len(y_validado)

# Split Treino e teste
x_treino, y_treino, x_teste, y_teste = treino_teste_split(dataset, 80)

# Treinamento 
w_fit = perceptron_fit(x_treino, y_treino)
print(w_fit)

# Validação
y_validado = perceptron_predict(x_teste, w_fit)
print(y_validado)

# Acurácia
accuracy = acuracia(y_teste, y_validado)
print(accuracy)




