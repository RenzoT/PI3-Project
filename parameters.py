from tkinter import *
def parameters():
    root.destroy()
    root = Tk()
    root.title("Corrector de Examenes")
    root.geometry("1000x750")
    root.configure(background='white')

    #Labels
    Label(root, text="Parámetros del examen:", font=("Futura Md BT", 30),bg="white").grid(row=0, column=0,padx=30, pady=20,sticky=W)

    Label(root, text="¿Cuántas preguntas tiene el examen?", font=("Futura Bk BT", 23),bg="white").grid(row=1, column=0,padx=60,  pady=20,sticky=W)
    Label(root, text="¿Cuántas alternativas tiene cada pregunta?", font=("Futura Bk BT", 23),bg="white").grid(row=2, column=0,padx=60, pady=20,sticky=W)

    Label(root, text="¿Cuántos puntos vale una\nrespuesta correcta?", font=("Futura Bk BT", 23),bg="white").grid(row=3, column=0,padx=60, pady=20,sticky=W)

    Label(root, text="¿Cuántos puntos disminuye una\nrespuesta incorrecta?", font=("Futura Bk BT", 23),bg="white").grid(row=4,padx=60, column=0, pady=20,sticky=W)
    Label(root, text="¿Cuántos puntos disminuye una\nrespuesta en blanco?", font=("Futura Bk BT", 23),bg="white").grid(row=5,padx=60, column=0, pady=20,sticky=W)

    #Entrys
    txtQuestions = Entry(root, width=5, bg="#ECECEC", font= ("Futura Bk BT", 23)).grid(row=1, column=1, pady=20,sticky=W)
    txtOptions = Entry(root, width=5, bg="#ECECEC", font= ("Futura Bk BT", 23)).grid(row=2, column=1, pady=20,sticky=W)
    txtCorrect = Entry(root, width=5, bg="#ECECEC", font= ("Futura Bk BT", 23)).grid(row=3, column=1, pady=20,sticky=W)
    txtIncorrect = Entry(root, width=5, bg="#ECECEC", font= ("Futura Bk BT", 23)).grid(row=4, column=1, pady=20,sticky=W)
    txtBlank = Entry(root, width=5, bg="#ECECEC", font= ("Futura Bk BT", 23)).grid(row=5, column=1, pady=20,sticky=W)

    #Buttons
    Button(root, text="Siguiente", font=("Futura Bk BT", 23), bg="#42B4FF", fg="white").grid(row=6, column=2, pady=20,sticky=W)
    Button(root, text="Atrás", font=("Futura Bk BT", 23), bg="white", fg="black").grid(row=6, column=1, pady=20,sticky=W)

    root.mainloop()