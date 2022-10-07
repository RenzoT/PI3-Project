from tkinter import *

root = Tk()
root.title("Calculadora")

number_one = Entry(root)
print(number_one)
number_one.grid(row=0, columnspan=6, sticky=W+E)
number_two = Entry(root)
number_two.grid(row=1, columnspan=6, sticky=W+E)
result = Entry(root, state="readonly")
result.grid(row=2, columnspan=6, sticky=W+E)


def plus():
    result.configure(state="normal")
    result.delete(1, END)
    result.insert(1, float(number_one.get()) + float(number_two.get()))
    result.configure(state="readonly")

def minus():
    result.configure(state="normal")
    result.delete(1, END)
    
    result.insert(1, float(number_one.get()) + float(number_two.get()))
    result.configure(state="readonly")

def times():
    result.configure(state="normal")
    result.delete(1, END)
    result.configure(state="normal")
    result.insert(1, float(number_one.get()) + float(number_two.get()))
    result.configure(state="readonly")

def divide():
    result.configure(state="normal")
    result.delete(1, END)
    result.configure(state="normal")
    result.insert(1, float(number_one.get()) + float(number_two.get()))
    result.configure(state="readonly")

#Botones
Button(root, text="+", command=lambda : plus() ).grid(row=3, column=0, sticky=W+E)
Button(root, text="-", command=lambda : minus()).grid(row=3, column=1, sticky=W+E)
Button(root, text="/", command=lambda : divide()).grid(row=4, column=0, sticky=W+E)
Button(root, text="*", command=lambda : times()).grid(row=4, column=1, sticky=W+E)

root.mainloop()