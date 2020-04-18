import numpy as np

lista = np.array([[3, 6, 9, 12],[15, 18, 21, 24], [27, 30, 33, 36], [39, 42, 45, 48], [51, 54, 57, 60]])

print('Impressão do array de entrada')
print(f'{lista}\n')

print('Impressão de array das linhas ímpares e colunas pares')
print(lista[::2, 1::2])
