import numpy as np

lista = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])

print('Impressão do array original')
print(f'{lista}\n')

print('Impressão do amin do eixo horizontal')
eixoHorizontal = np.amin(lista, axis=1)
print(f'{eixoHorizontal}\n')

print('Impressão do amax do eixo vertical')
eixoVertical = np.amax(lista, axis=0)
print(eixoVertical)