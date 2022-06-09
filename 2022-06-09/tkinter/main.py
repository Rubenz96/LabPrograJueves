import tkinter as tk
from tkinter import ttk

def imprimirConsola():
    texto_casilla = casilla.get()
    print(texto_casilla)


ventana = tk.Tk()
#---------------------------------------
ventana.title('Prueba tkinter')
ventana.config(width=600,height=500)

texto = ttk.Label(text = 'Ingrese numero:')
texto.place(x=10,y=10)

casilla = ttk.Entry()
casilla.place(x=130 ,y=10)

boton = ttk.Button(text = 'Click', command=imprimirConsola)
boton.place(x=130,y=50)

#---------------------------------------
ventana.mainloop()