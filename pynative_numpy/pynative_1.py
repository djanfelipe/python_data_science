import numpy as np

print('Impressão do array\n')

lista = np.empty([4, 2], dtype=np.uint16)
print(f'{lista}\n')

print('Impressão dos atributos do array numpy\n')

print(f'1>. A forma do array é: {lista.shape}')
print(f'2>. As dimensões do array são: {lista.ndim}')
print(f'3>. O tamanho de cada elemento do array em bytes é: {lista.itemsize}')
