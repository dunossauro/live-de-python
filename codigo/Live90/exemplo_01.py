"""
Grafico simples de mais.
"""
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('tkagg')

X = range(10)
Y = [val ** 2 for val in X]

plt.plot(X, Y)
plt.show()
