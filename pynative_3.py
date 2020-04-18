import numpy as np

lista = np.array([[11,22,33],[44, 55, 66], [77, 88, 99]])
print('Impressão do array de entrada\n')
print(f'{lista}\n')

print('Impressão de array dos itens na terceira coluna de todas as linhas\n')

lista_tratada = lista[:, 2]
print(lista_tratada)
