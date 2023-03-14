from tkinter import *
from tkinter import ttk
import math

"""----------------------------------------ROOT------------------------------------------"""
#Dimensionar la ventana principal
windowRoot = Tk()
windowRoot.title("Calculadora")
windowRoot.geometry("+500+80")

#Adapta el tamaño de la columna y
# fila de la ventana principal junto con los widgets
windowRoot.columnconfigure(0, weight= 1)
windowRoot.rowconfigure(0, weight= 1)

"""----------------------------------------FRAME------------------------------------------"""
#Agrega estilos a la calculadora
#Viene una por defecto llamada vista
#pero presenta problemas al agregar estilos
estilos = ttk.Style()
estilos.theme_use("clam")
estilos.configure("mainframe.TFrame", background ="#DBDBDB")

#Con la etiqueta style hará que plasme los diseños que se colocaron anteriormente
#Para que el frame esté dentro de la ventana principal
mainFrame = ttk.Frame(windowRoot, style="mainframe.TFrame")

#Adaptar los widgets a la ventana principal
mainFrame.grid(column=0, row=0, sticky= ( W, N, E, S) )

"""----------------------------------------LABEL------------------------------------------"""
#Estilo de los labels
estilos_label1 = ttk.Style()
estilos_label1.configure("Label1.TLabel", font ="arial 15", anchor="e")

estilos_label2 = ttk.Style()
estilos_label2.configure("Label2.TLabel", font ="arial 40", anchor="e")

#Esta creando una variable que estará vinculada a un widget
#Lo que se escriba en entrada 1 se vera reflejado en el textvariable
entrada1 = StringVar()
label_entrada1 = ttk.Label(mainFrame, textvariable= entrada1, style="Label1.TLabel")
label_entrada1.grid(column=0, row = 0, columnspan=4, sticky= ( W, N, E, S))

entrada2 = StringVar()
label_entrada2 = ttk.Label(mainFrame, textvariable= entrada2, style="Label2.TLabel")
label_entrada2.grid(column=0, row = 1, columnspan=4, sticky= ( W, N, E, S))

"""----------------------------------------Button------------------------------------------"""
#Estilos para los botones
estilos_botones_numeros = ttk.Style()
estilos_botones_numeros.configure("Botones_numeros.TButton", font="arial 22", width=5,
                                  background="#FFFFFF", relief="flat")
estilos_botones_numeros.map("Botones_numeros.TButton",
                            background=[("active","#B9B9B9")])

estilos_botones_borrar = ttk.Style()
estilos_botones_borrar.configure("Botones_borrar.TButton", font="arial 22", width= 5,
                                 background="#CECECE", relief="flat")
estilos_botones_borrar.map("Botones_borrar.TButton",
                           foreground= [("active", "#FF0000")],
                           background=[("active","#858585")])

estilos_botones_operacion = ttk.Style()
estilos_botones_operacion.configure("Botones_operacion.TButton", font="arial 22",
                                    width= 5, background="#CECECE", relief="flat")
estilos_botones_operacion.map("Botones_operacion.TButton", background=[("active","#858585")])








#Mostrar la ventana principal hasta que se cierre
windowRoot.mainloop()