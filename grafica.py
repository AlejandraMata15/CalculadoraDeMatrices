import os
import funciones as f

os.system('clear')

while True:
	print('Tamaño de la matriz : ',end='')
	tam=int(input())
	if tam>0 and tam<5:
		break

print('Modulo dudoso : ',end='')
mod=int(input())

f.ingreMatriz(tam,mod)



