import numpy as np

lista1 = np.array([[5, 6, 9], [21, 18, 27]])
lista2 = np.array([[15, 33, 24], [4, 7, 1]])

print('A adição de dois arrays resulta em:\n')

lista_final = lista1 + lista2
print(f'{lista_final}\n')

print('Array resultante após calcular a exponênciação de todos os elementos\n')
print(lista_final ** 2)
