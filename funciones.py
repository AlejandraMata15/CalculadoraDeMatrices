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


#Para saber si son coprimos su MCD debe ser 1
def mcd(n,modulo):
	x=modulo
	y=n
	while y>0:
		r=x%y
		x=y
		y=r
	return x

#Para ingresar la matriz
def ingreMatriz(tam,mod):
	matriz=[]
	for i in range(0,tam*tam):
		print(' -> ',end='')
		val=int(input())
		matriz.append(val)
	os.system('clear')
	mostrar(tam,matriz)
	determinante=det(matriz,tam)
	print('Determinante de la matriz : '+str(determinante))
	
	if mcd(determinante%mod,mod)==1:
		print('La matriz es invertible en módulo '+str(mod)+' ya que '+str(mod)+' y '+str(determinante%mod)+' son coprimos\n')
	else:
		print('La matriz no es invertible en módulo '+str(mod)+' porque no son coprimos\n')





