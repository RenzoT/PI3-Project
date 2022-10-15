from tkinter import *
import tkinter

root = Tk()
root.title("Calculadora")

a = tkinter.Label(root, text="Ingrese el primer numero: ")
b = tkinter.Label(root, text="Ingrese el segundo numero: ")
a.pack(side = tkinter.TOP, anchor=NW)
b.pack(side = tkinter.TOP, anchor=NW)

root.mainloop()