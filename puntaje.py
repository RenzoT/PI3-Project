import openpyxl
from tkinter import *
from math import ceil as ceil

wb = openpyxl.load_workbook('result.xlsx')
sheet = wb.active

app = Tk()
app.title("Corrector de examenes")

#Parametros privados
col_answer = 0
last_col = 0
last_row = 0
correct = []
answers = []

#Funciones
def correct_exam():
    correctas = 0
    incorrectas = 0
    for i in range(1, questions + 1):
        correct.append(ord((answers[i-1].get()).upper())-64)

    for question in range(questions):
        totalAnswers = 0
        for option in range(alternativas):
            if sheet.cell(row = option+2, column = question+2).value == 'X':
                totalAnswers += 1
                if option+2 == correct[question]+1:
                    correctas += 1
                else:
                    incorrectas += 1
                if totalAnswers > 1:
                    correctas -= 1

    print("--------------------")
    print("Resultado del examen")
    print("--------------------")
    print("Correctas: ", correctas)
    print("Incorrectas: ", incorrectas)
    print("Blancas: ", questions - correctas - incorrectas)
    print("Puntaje", vCorrecta*correctas - vIncorrecta*incorrectas + vBlanco*(questions - correctas - incorrectas))

def set_questions():
    for i in range(1, questions + 1):
        Label(app, text="Pregunta " + str(i) + ": ").grid(row=(i-1)%25, column=(ceil(i/25)-1)*2)
        ans = Entry(app, width=2)
        ans.grid(row=(i-1)%25,column= (ceil(i/25)-1)*2+1)
        answers.append(ans)
        last_row, last_col = (i-1)%25, (ceil(i/25)-1)*2+1
    Button(app, text="Atras").grid(row=last_row+1, column=last_col+1, sticky=W+E)
    Button(app, text="Corregir", command=lambda : correct_exam() ).grid(row=last_row+1, column=last_col+2, sticky=W+E)




#Parametros de usuario
questions = int(input("¿Cuantas preguntas tiene el examen?: "))
set_questions()
alternativas = int(input("¿Cuantas alternativas tiene cada pregunta?: "))
vCorrecta = float(input("\n¿Cuantos puntos vale una respuesta correcta?: "))
vIncorrecta = float(input("¿Cuantos puntos vale una respuesta incorrecta?: "))
vBlanco = float(input("¿Cuantos puntos vale una respuesta en blanco?: "))



#Buttons


app.mainloop()