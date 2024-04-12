import numpy as np
from fractions import Fraction

# Definir la matriz de adyacencia
matriz_adyacencia = np.array([ 
    [0, 0, 1/3, 1/2, 0],
    [1, 0, 0, 1/2, 0],
    [0, 1/2, 0, 0, 1],
    [0, 1/2, 1/3, 0, 0],
    [0, 0, 1/3, 0, 0]
])

# Definir el vector de probabilidad inicial
vector_probabilidad = np.array([1/5, 1/5, 1/5, 1/5, 1/5])

# Realizar iteraciones
for i in range(10):
    vector_probabilidad = np.dot(matriz_adyacencia, vector_probabilidad)
    print(f'Iteración {i+1}: {vector_probabilidad}')