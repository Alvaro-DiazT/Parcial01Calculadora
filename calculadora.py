from tkinter import *
from tkinter import ttk
import math


def ingresarValores(tecla):
    if tecla >= '0' and tecla <= '9' or tecla == '(' or tecla == ')' or tecla == '.':
        entrada2.set(entrada2.get() + tecla)

    if tecla == '*' or tecla == '/' or tecla == '+' or tecla == '-' or tecla == '%' or tecla == '^':
        if tecla == '*':
            entrada1.set(entrada2.get() + '*')
        if tecla == '/':
            entrada1.set(entrada2.get() + '/')
        if tecla == '+':
            entrada1.set(entrada2.get() + '+')
        if tecla == '-':
            entrada1.set(entrada2.get() + '-')
        if tecla == '%':
            entrada1.set(entrada2.get() + '%')
        if tecla == '^':
            entrada1.set(entrada2.get() + '**')

        entrada2.set("")

    if tecla == "=":

        entrada1.set(entrada1.get() + entrada2.get())
        resultado = eval(entrada1.get())
        entrada2.set(resultado)

def ingresarValoresTeclado(event):
    tecla = event.char
    if tecla >= '0' and tecla <= '9' or tecla == '(' or tecla == ')' or tecla == '.':
        entrada2.set(entrada2.get() + tecla)

    if tecla == '*' or tecla == '/' or tecla == '+' or tecla == '-' or tecla == '%' or tecla == '^':
        if tecla == '*':
            entrada1.set(entrada2.get() + '*')
        if tecla == '/':
            entrada1.set(entrada2.get() + '/')
        if tecla == '+':
            entrada1.set(entrada2.get() + '+')
        if tecla == '-':
            entrada1.set(entrada2.get() + '-')
        if tecla == '%':
            entrada1.set(entrada2.get() + '%')
        if tecla == '^':
            entrada1.set(entrada2.get() + '**')

        entrada2.set("")

    if tecla == "=":
        entrada1.set(entrada1.get() + entrada2.get())
        resultado = eval(entrada1.get())
        entrada2.set(resultado)

def calcularRaizCuadrada():
    entrada1.set("")
    resultado = math.sqrt(float(entrada2.get()))
    entrada2.set(resultado)
def calcularLogaritmo():
    entrada1.set("")
    resultado = math.log10(float(entrada2.get()))
    entrada2.set(resultado)

def borrar(event = ""):
    inicio = 0
    final = len(entrada2.get())

    entrada2.set(entrada2.get()[inicio:final-1])

def borrarTodo(event = ""):
    entrada2.set("")
    entrada1.set("")

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

#Botones para los numeros 0-9
button0 = ttk.Button(mainFrame, text="0", style="Botones_numeros.TButton", command = lambda: ingresarValores('0'))
button1 = ttk.Button(mainFrame, text="1", style="Botones_numeros.TButton", command = lambda: ingresarValores('1'))
button2 = ttk.Button(mainFrame, text="2", style="Botones_numeros.TButton", command = lambda: ingresarValores('2'))
button3 = ttk.Button(mainFrame, text="3", style="Botones_numeros.TButton", command = lambda: ingresarValores('3'))
button4 = ttk.Button(mainFrame, text="4", style="Botones_numeros.TButton", command = lambda: ingresarValores('4'))
button5 = ttk.Button(mainFrame, text="5", style="Botones_numeros.TButton", command = lambda: ingresarValores('5'))
button6 = ttk.Button(mainFrame, text="6", style="Botones_numeros.TButton", command = lambda: ingresarValores('6'))
button7 = ttk.Button(mainFrame, text="7", style="Botones_numeros.TButton", command = lambda: ingresarValores('7'))
button8 = ttk.Button(mainFrame, text="8", style="Botones_numeros.TButton", command = lambda: ingresarValores('8'))
button9 = ttk.Button(mainFrame, text="9", style="Botones_numeros.TButton", command = lambda: ingresarValores('9'))

#Botones de borrado y agrupacion
#chr(9003) es un el simbolo para borrar uno a uno
button_borrar = ttk.Button(mainFrame, text= chr(9003), style="Botones_borrar.TButton", command = lambda: borrar())
button_borrar_todo = ttk.Button(mainFrame, text="C", style="Botones_borrar.TButton", command= lambda: borrarTodo())
button_parentesis1 = ttk.Button(mainFrame, text="(", style="Botones_operacion.TButton", command = lambda: ingresarValores("("))
button_parentesis2 = ttk.Button(mainFrame, text=")", style="Botones_operacion.TButton", command = lambda: ingresarValores(")"))
button_punto = ttk.Button(mainFrame, text=".", style="Botones_operacion.TButton", command = lambda: ingresarValores("."))
button_igual = ttk.Button(mainFrame, text="=", style="Botones_operacion.TButton", command = lambda: ingresarValores('='))

#Botones operaciones basicas
#chr(247) Simbolo de division
button_division = ttk.Button(mainFrame, text= chr(247), style="Botones_operacion.TButton", command = lambda: ingresarValores('/'))
button_multiplicacion = ttk.Button(mainFrame, text="x", style="Botones_operacion.TButton", command = lambda: ingresarValores('*'))
button_resta = ttk.Button(mainFrame, text="-", style="Botones_operacion.TButton", command = lambda: ingresarValores('-'))
button_suma = ttk.Button(mainFrame, text="+", style="Botones_operacion.TButton", command = lambda: ingresarValores('+'))
button_modulo = ttk.Button(mainFrame, text="%", style="Botones_operacion.TButton", command = lambda: ingresarValores('%'))
button_potencia = ttk.Button(mainFrame, text="^", style="Botones_operacion.TButton", command = lambda: ingresarValores('^'))

#Botones operaciones avanzadas
button_raiz_cuadrada = ttk.Button(mainFrame, text="√", style="Botones_operacion.TButton", command= lambda : calcularRaizCuadrada())
button_logaritmo = ttk.Button(mainFrame, text="ln", style="Botones_operacion.TButton", command= lambda: calcularLogaritmo())

#Ubicar botones en la pantalla frame
button_parentesis1.grid(column=0, row=2, sticky= ( W, N, E, S))
button_parentesis2.grid(column=1, row=2, sticky= ( W, N, E, S))
button_borrar_todo.grid(column=2, row=2, sticky= ( W, N, E, S))
button_borrar.grid(column=3, row=2, sticky= ( W, N, E, S))

button_suma.grid(column=0, row=3, sticky= ( W, N, E, S))
button_resta.grid(column=1, row=3, sticky= ( W, N, E, S))
button_multiplicacion.grid(column=2, row=3, sticky= ( W, N, E, S))
button_division.grid(column=3, row=3, sticky= ( W, N, E, S))

button7.grid(column=0, row=4, sticky= ( W, N, E, S))
button8.grid(column=1, row=4, sticky= ( W, N, E, S))
button9.grid(column=2, row=4, sticky= ( W, N, E, S))
button_raiz_cuadrada.grid(column=3, row=4, sticky= ( W, N, E, S))

button4.grid(column=0, row=5, sticky= ( W, N, E, S))
button5.grid(column=1, row=5, sticky= ( W, N, E, S))
button6.grid(column=2, row=5, sticky= ( W, N, E, S))
button_potencia.grid(column=3, row=5, sticky= ( W, N, E, S))

button1.grid(column=0, row=6, sticky= ( W, N, E, S))
button2.grid(column=1, row=6, sticky= ( W, N, E, S))
button3.grid(column=2, row=6, sticky= ( W, N, E, S))
button_modulo.grid(column=3, row=6, sticky= ( W, N, E, S))

button_punto.grid(column=0, row=7, sticky= ( W, N, E, S))
button0.grid(column=1, row=7, sticky= ( W, N, E, S))
button_igual.grid(column=2, row=7, sticky= ( W, N, E, S))
button_logaritmo.grid(column=3, row=7, sticky= ( W, N, E, S))




#Mostrar la ventana principal hasta que se cierre
windowRoot.mainloop()