import openpyxl
from tkinter import *
from math import ceil as ceil

def close_window(root):
    root.destroy()

def parameters(root):
    root.destroy()
    param = Tk()
    param.title("Corrector de Examenes")
    param.geometry("1000x750")
    param.configure(background='white')


    #Labels
    Label(param, text="Parámetros del examen:", font=("Futura Md BT", 30),bg="white").grid(row=0, column=0,padx=30, pady=20,sticky=W)

    Label(param, text="¿Cuántas preguntas tiene el examen?", font=("Futura Bk BT", 23),bg="white").grid(row=1, column=0,padx=60,  pady=20,sticky=W)
    Label(param, text="¿Cuántas alternativas tiene cada pregunta?", font=("Futura Bk BT", 23),bg="white").grid(row=2, column=0,padx=60, pady=20,sticky=W)

    Label(param, text="¿Cuántos puntos vale una\nrespuesta correcta?", font=("Futura Bk BT", 23),bg="white").grid(row=3, column=0,padx=60, pady=20,sticky=W)

    Label(param, text="¿Cuántos puntos disminuye una\nrespuesta incorrecta?", font=("Futura Bk BT", 23),bg="white").grid(row=4,padx=60, column=0, pady=20,sticky=W)
    Label(param, text="¿Cuántos puntos disminuye una\nrespuesta en blanco?", font=("Futura Bk BT", 23),bg="white").grid(row=5,padx=60, column=0, pady=20,sticky=W)

    #Entrys
    txtQuestions = Entry(param, width=5, bg="#ECECEC", font= ("Futura Bk BT", 23))
    txtQuestions.grid(row=1, column=1, pady=20,sticky=W)
    txtOptions = Entry(param, width=5, bg="#ECECEC", font= ("Futura Bk BT", 23))
    txtOptions.grid(row=2, column=1, pady=20,sticky=W)
    txtCorrect = Entry(param, width=5, bg="#ECECEC", font= ("Futura Bk BT", 23))
    txtCorrect.grid(row=3, column=1, pady=20,sticky=W)
    txtIncorrect = Entry(param, width=5, bg="#ECECEC", font= ("Futura Bk BT", 23))
    txtIncorrect.grid(row=4, column=1, pady=20,sticky=W)
    txtBlank = Entry(param, width=5, bg="#ECECEC", font= ("Futura Bk BT", 23))
    txtBlank.grid(row=5, column=1, pady=20,sticky=W)

    def puntaje_window():
        puntaje = Toplevel()
        puntaje.title("Corrector de Examenes")
        puntaje.configure(background='white')
    
        wb = openpyxl.load_workbook('result.xlsx')
        sheet = wb.active

        #Privados
        col_answer = 0
        last_col = 0
        last_row = 0
        correct = []
        answers = []

        def correct_exam():
            correctas = 0
            incorrectas = 0
            for i in range(1, questions + 1):
                correct.append(ord((answers[i-1].get()).upper())-64)

            for question in range(questions):
                totalAnswers = 0
                for option in range(options):
                    if sheet.cell(row = option+2, column = question+2).value == 'X':
                        totalAnswers += 1
                        if option+2 == correct[question]+1:
                            correctas += 1
                        else:
                            incorrectas += 1
                            correctas -= 1

            print("--------------------")
            print("Resultado del examen")
            print("--------------------")
            print("Correctas: ", correctas)
            print("Incorrectas: ", incorrectas)
            print("Blancas: ", questions - correctas - incorrectas)
            print("Puntaje", vCorrect*correctas - vIncorrect*incorrectas + vBlank*(questions - correctas - incorrectas))

        def set_questions():
            for i in range(1, questions + 1):
                Label(puntaje, text="Pregunta " + str(i) + ": ", bg="white").grid(row=(i-1)%25, column=(ceil(i/25)-1)*2)
                ans = Entry(puntaje, width=2, bg="#ECECEC")
                ans.grid(row=(i-1)%25,column= (ceil(i/25)-1)*2+1)
                answers.append(ans)
                last_row, last_col = (i-1)%25, (ceil(i/25)-1)*2+1

            Button(puntaje, text="Cerrar", command= puntaje.destroy).grid(row=last_row+1, column=last_col+1, sticky=W+E)
            Button(puntaje, text="Corregir", command=lambda : correct_exam(), bg="#42B4FF", fg="white").grid(row=last_row+1, column=last_col+2, sticky=W+E)

        #Parametros
        questions = int(txtQuestions.get())
        set_questions()
        options = int(txtOptions.get())
        vCorrect = float(txtCorrect.get())
        vIncorrect = float(txtIncorrect.get())
        vBlank = float(txtBlank.get())

    #Buttons
    Button(param, text="Siguiente", font=("Futura Bk BT", 23), bg="#42B4FF", fg="white", command=puntaje_window).grid(row=6, column=2, pady=20,sticky=W)
    Button(param, text="Salir", font=("Futura Bk BT", 23), bg="white", fg="black", command=lambda: close_window(param)).grid(row=6, column=1, pady=20,sticky=W)
