import numpy as np
from fractions import Fraction

def submatriz(matriz, row, col):
    return [fila[:col] + fila[col + 1:] for fila in (matriz[:row] + matriz[row + 1:])]

def determinante(matriz):
    if len(matriz) != len(matriz[0]):
        raise ValueError("La matriz debe ser cuadrada para calcular el determinante.")
    if len(matriz) == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    det = 0
    for col in range(len(matriz)):
        cofactor = matriz[0][col] * determinante(submatriz(matriz, 0, col))
        if col % 2 == 1:
            cofactor = -cofactor
        det += cofactor
    return det

def matriz_inversa(matriz):
    matriz_inv = np.linalg.inv(matriz)

    filas,columnas = matriz_inv.shape
    for i in range(filas):
        for j in range(columnas):
            elemento = Fraction(matriz_inv[i,j]).limit_denominator(1000)
            print(elemento, end="\t")
        print()

matriz =[[5,17,20], [9,23,3],[2,11,13]]
det = determinante(matriz)
print("El determinante de la matriz es: ", det)
matriz_inv = matriz_inversa(matriz)



