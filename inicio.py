from tkinter import *
from parameters import *

root = Tk()
root.title("Corrector de Examenes")
root.geometry("1000x750")
root.configure(background='white')

center = Frame(root, bg='white')
center.pack(pady=0.05*root.winfo_screenheight() ,anchor=CENTER)

logo = PhotoImage(file="images/logo.png")
Label(center, image=logo, bg="white").pack(pady=30)
Label(center, text="Bienvenido a Corrector de Exámenes", font=("Calibri", 20),bg="white").pack()
Button(center, text="Iniciar", font=("Calibri", 20), bg="#42B4FF", fg="white", command= lambda: parameters(root)).pack(pady=30)

root.mainloop()

 