import numpy as np

print('Printing Array\n')

lista = np.empty([4, 2], dtype=np.uint16)
print(f'{lista}\n')

print('Printing numpy array Atributes\n')

print(f'1>. Array shape is: {lista.shape}')
print(f'2>. Array dimensions are {lista.ndim}')
print(f'3>. Length of each element of array in bytes is {lista.itemsize}')
