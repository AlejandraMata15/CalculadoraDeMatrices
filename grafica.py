import os
import funciones as f
import tkinter as tk
from tkinter import Entry, StringVar

def matriz():
    print("siguiente")
    tamM = int(tam.get())
    modulo = int(mod.get())
    matriz = f.ingreMatriz(tamM, modulo)

pantalla = tk.Tk()
pantalla.title("Calculadora de matrices")
pantalla.geometry("500x400")

label_tam = tk.Label(pantalla, text="Tamaño de la matriz: ")
label_tam.pack()
tam = Entry(pantalla, width=15)
tam.pack()

label_mod = tk.Label(pantalla, text="Modulo: ")
label_mod.pack()
mod = Entry(pantalla, width=15)
mod.pack()

button = tk.Button(pantalla, text="Siguiente", command=matriz)
button.pack()

pantalla.mainloop()
'''while True:
	print('Tamaño de la matriz : ',end='')
	tam=int(input())
	if tam>0 and tam<5:
		break

print('Modulo dudoso : ',end='')
mod=int(input())

f.ingreMatriz(tam,mod)'''



