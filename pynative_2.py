import numpy as np

print('Criação de array 5X2 com o uso do numpy.arange\n')

lista = np.array(np.arange(100, 200, 10)).reshape(5, 2)
print(lista)
