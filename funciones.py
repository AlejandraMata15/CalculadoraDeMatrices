import numpy as np
import os

#Mostrar matriz
def mostrar(tam,matriz):
	for i in range(1,(tam*tam)+1):
		print(matriz[i-1],end='')
		if i%tam==0:
			print('')
	print('')

#Pa'que Vanessa ama entienda, el determinante osi osi
def det(matriz,tam):
	#Caso base
	if tam==2:
		return matriz[0]*matriz[3]-matriz[1]*matriz[2]
	elif tam==3:
		return matriz[0]*det(list([matriz[4],matriz[5],matriz[7],matriz[8]]),tam-1)-matriz[1]*det(list([matriz[3],matriz[5],matriz[6],matriz[8]]),tam-1)+matriz[2]*det(list([matriz[3],matriz[4],matriz[6],matriz[7]]),tam-1)
	elif tam==4:
		return matriz[0]*det(list([matriz[5],matriz[6],matriz[7],matriz[9],matriz[10],matriz[11],matriz[13],matriz[14],matriz[15]]),tam-1)-matriz[1]*det(list([matriz[4],matriz[6],matriz[7],matriz[8],matriz[10],matriz[11],matriz[12],matriz[14],matriz[15]]),tam-1)+matriz[2]*det(list([matriz[4],matriz[5],matriz[7],matriz[8],matriz[9],matriz[11],matriz[12],matriz[13],matriz[15]]),tam-1)-matriz[3]*det(list([matriz[4],matriz[5],matriz[6],matriz[8],matriz[9],matriz[10],matriz[12],matriz[13],matriz[14]]),tam-1)




#Para ingresar la matriz
def ingreMatriz(tam):
	matriz=[]
	for i in range(0,tam*tam):
		print(' ---',end='')
		val=int(input())
		matriz.append(val)
	os.system('clear')
	mostrar(tam,matriz)
	print('\nDeterminante de la matriz : '+str(det(matriz,tam)))


