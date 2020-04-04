import numpy as np

print('Creating 5X2 array using numpy.arange\n')

lista = np.array(np.arange(100, 200, 10)).reshape(5, 2)
print(f'{lista}')
