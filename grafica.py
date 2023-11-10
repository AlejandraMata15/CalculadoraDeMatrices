import os
import funciones as f
import tkinter as tk
from tkinter import Entry, StringVar

def inversa(matriz,tam):
	nueva_ventana = tk.Toplevel(pantalla)
	nueva_ventana.title("Matriz inversa")
	nueva_ventana.geometry('400x300')
	tam_Matriz = int(tam)
	#Crear una lista para almacenar los Entry widgets
	# entries = []
	#Crear filas y columnas de Entry widgets
	i=0
	print(matriz)
	for fila in range(tam_Matriz):
		fila_entries = []
		for columna in range(tam_Matriz):
			entry = Entry(nueva_ventana, width=5)
			entry.insert(0,str(matriz[i]))
			entry.grid(row= fila+6, column= columna)
			fila_entries.append(entry)
			i=i+1
		entries.append(fila_entries)
	#button2 = tk.Button(pantalla, text="Calcular", command=obtenerValores)
	#button2.grid(row=20, column=1)


def matriz(valores):
	val=[]
	print("siguiente")
	tamM = int(tam.get())
	tamM = tamM
	modulo = int(mod.get())
	for i in valores:
		val.append(int(i))
	matriz = f.ingreMatriz(tamM, modulo,val)
	print(matriz)
	inversa(matriz,tamM)

def crear_entries():

	#Obtener el valor de tam y convertirlo en entero
	tam_Matriz = int(tam.get())
	#Crear una lista para almacenar los Entry widgets
	# entries = []
	#Crear filas y columnas de Entry widgets
	for fila in range(tam_Matriz):
		fila_entries = []
		for columna in range(tam_Matriz):
			entry = Entry(pantalla, width=5)
			entry.grid(row= fila+6, column= columna)
			fila_entries.append(entry)
		entries.append(fila_entries)
	button2 = tk.Button(pantalla, text="Calcular", command=obtenerValores)
	button2.grid(row=20, column=1)


def obtenerValores():
	valores = []
	for fila_entries in entries:
		fila_valores = [entry.get() for entry in fila_entries]
		valores.append(fila_valores)

	# Verificar que se hayan ingresado suficientes valores
	tam_Matriz = int(tam.get())
	if all(len(fila) == tam_Matriz for fila in valores) and len(valores) == tam_Matriz:
		valores = aplanarLista(valores)
		matriz(valores)
	else:
		print("Asegúrate de ingresar valores en cada celda de la matriz.")
	#matriz(valores)

def aplanarLista(valores):
	lista = []
	for sublista in valores:
		lista.extend(sublista)
	valores = lista[:]
	return valores

entries = []
os.system('clear')
pantalla = tk.Tk()
pantalla.title("Calculadora de matrices")
pantalla.geometry("400x300")

label_tam = tk.Label(pantalla, text="Tamaño de la matriz: ")
label_tam.grid(row=0, column=2)
tam = Entry(pantalla, width=15)
tam.grid(row=0, column=3)

label_mod = tk.Label(pantalla, text="Modulo: ")
label_mod.grid(row=3, column=2)
mod = Entry(pantalla, width=15)
mod.grid(row=3, column=3)

button = tk.Button(pantalla, text="Siguiente", command=crear_entries)
button.grid(row=5, column=3)


pantalla.mainloop()
'''while True:
	print('Tamaño de la matriz : ',end='')
	tam=int(input())
	if tam>0 and tam<5:
		break

print('Modulo dudoso : ',end='')
mod=int(input())

f.ingreMatriz(tam,mod)'''



