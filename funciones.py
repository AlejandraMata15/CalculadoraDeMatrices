import numpy as np
import os

#Convertir un array a matriz
def conv(matriz,tam):
	if tam==2:
		return [[matriz[0],matriz[1]],[matriz[2],matriz[3]]]
	elif tam==3:
		return [[matriz[0],matriz[1],matriz[2]],[matriz[3],matriz[4],matriz[5]],[matriz[6],matriz[7],matriz[8]]]
	elif tam==4:
		return [[matriz[0],matriz[1],matriz[2],matriz[3]],[matriz[4],matriz[5],matriz[6],matriz[7]],[matriz[8],matriz[9],matriz[10],matriz[11]],[matriz[12],matriz[13],matriz[14],matriz[15]]] 

#Pal determinante osi osi
def det(matriz):
	m=np.array(matriz)
	salida=np.linalg.det(m)
	return round(salida)

#Adjunta de una matriz
def cofactores(matrix):
	num_rows, num_cols = matrix.shape
	cofactors = np.zeros((num_rows, num_cols), dtype=int)

	for i in range(num_rows):
		for j in range(num_cols):
			submatrix = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
			cofactors[i, j] = (-1) ** (i + j) * int(round(np.linalg.det(submatrix)))
	return cofactors

def adjunta(matriz):
	matrizCof=cofactores(matriz)
	adjunta=matrizCof.T
	return adjunta

#Tranpuesta
def transpuesta(matriz):
	return np.transpose(matriz)

#Para saber si son coprimos su MCD debe ser 1
def mcd(n,modulo):
	x=modulo
	y=n
	while y>0:
		r=x%y
		x=y
		y=r
	return x

#Para mostrar la inversa
def mostrar(matriz,det):
	fila=len(matriz)
	columna=len(matriz[0])

	for i in range(fila):
		print('[',end='')
		for j in range(columna):
			print(' '+str(matriz[i][j])+'/'+str(det)+' ',end='')
		print(']')

#Algoritmo extendido de euclides
def aee(a,b):
	if b==0:
		return (a,1,0)
	else:
		(d,x1,y1)=aee(b,a%b)
		x=y1
		y=x1-(a//b)*y1
		return (d,x,y)

#Matriz inversa con modulo
def modulo(matriz,det,mod):
	f=len(matriz)
	c=len(matriz[0])
	m=aee(det,mod)[1]

	for i in range(f):
		print('[',end='')
		for j in range(c):
			print(' '+str(((matriz[i][j]%mod)*m)%mod),end='')
		print(']')

#Para ingresar la matriz
def ingreMatriz(tam,mod):
	matriz=[]
	for i in range(0,tam*tam):
		print('--> ',end='')
		val=int(input())
		matriz.append(val)
	os.system('clear')
	matriz=np.array(conv(matriz,tam))
	print(matriz)
	determinante=det(matriz)
	print('Determinante de la matriz : '+str(determinante))
	
	if mcd(determinante%mod,mod)==1:
		print('La matriz es invertible en módulo '+str(mod)+' ya que '+str(mod)+' y '+str(determinante%mod)+' son coprimos\n')
		matriz=adjunta(matriz)
		print('\nLa matriz inversa es : ')
		mostrar(matriz,determinante)
		print('\nLa matriz inversa con modulo : ')
		modulo(matriz,determinante,mod)
	else:
		print('La matriz no es invertible en módulo '+str(mod)+' porque no son coprimos\n')





