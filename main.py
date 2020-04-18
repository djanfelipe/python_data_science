# Primeira aula - Introdução ao Python
import numpy as np

kms = np.loadtxt("data/carros-km.txt")
# print(kms)

anos = np.loadtxt("data/carros-anos.txt", dtype=int)
# print(anos)

media_kms = kms / (2019 - anos)
print(media_kms)
