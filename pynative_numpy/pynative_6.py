import numpy as np

print("Criação de array 8x3 com uso do numpy.arange\n")

lista = np.array(np.arange(10, 34).reshape(8, 3))
print(f'{lista}\n')

print("Divisão do array 8x3 em quatro sub-arrays\n")

lista_final = np.array_split(lista, 4)
print(lista_final)