import numpy as np

lista = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])

print('Impressão do array original')
print(f'{lista}\n')

print('Impressão do array ordenado pela segunda linha')

segundaLinha = lista[1, :]
# print(f'Sem argsort(): {segundaLinha}')
# print(f'Com argsort(): {segundaLinha[segundaLinha.argsort()]}\n')

listaOrdenadaPorLinha = lista[:, segundaLinha.argsort()]
print(f'{listaOrdenadaPorLinha}\n')

print('Impressão do array ordenado pela segunda coluna')

segundaColuna = lista[:, 1]
# print(f'Sem argsort(): {segundaColuna}')
# print(f'Com argsort():{segundaColuna[segundaColuna.argsort()]}')

listaOrdenadaPorColuna = lista[segundaColuna.argsort()]
print(listaOrdenadaPorColuna)