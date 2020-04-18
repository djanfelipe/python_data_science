import numpy as np

lista = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
coluna = np.array([10, 10, 10])
print('Impressão do array original')
print(f'{lista}\n')

print('Array após deletar a segunda coluna no eixo horizontal')
lista = np.delete(lista, 1, axis=1)
print(f'{lista}\n')

print('Array após inserir uma nova segunda coluna no eixo horizontal')
lista = np.insert(lista, 1, coluna, axis=1)
print(lista)