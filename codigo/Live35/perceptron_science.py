from sklearn import linear_model, model_selection, metrics
import pandas as pd

# Carrega os elementos do dataset
dataset = pd.read_csv('data1.csv')
x = dataset.iloc[:, 1:].values
y = dataset.iloc[:, 0].values

# Cria um objeto Perceptron
perceptron = linear_model.Perceptron()

# Split em conjunto de treino e teste
x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.2, random_state=0)

# Treinamento
classificador = perceptron.fit(x_train, y_train)

# Validação
y_predict = classificador.predict(x_test)

# Acurácia
print(metrics.accuracy_score(y_test, y_predict))