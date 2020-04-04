import numpy as np


lista = np.array([[11,22,33],[44, 55, 66], [77, 88, 99]])
print('Printing Input Array\n')
print(f'{lista}\n')

print('Printing array of items in the third column of all rows\n')

lista_tratada = lista[:, 2]
print(lista_tratada)
