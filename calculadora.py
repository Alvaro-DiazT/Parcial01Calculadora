from tkinter import *
from tkinter import ttk
import math

#Dimensionar la ventana principal
windowRoot = Tk()
windowRoot.title("Calculadora")
windowRoot.geometry("+500+80")

#Adapta el tamaño de la columna y fila de la ventana principal junto con los widgets
windowRoot.columnconfigure(0, weight= 1)
windowRoot.rowconfigure(0, weight= 1)



windowRoot.mainloop() #Mostrar la ventana principal