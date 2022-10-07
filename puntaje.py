import openpyxl
from tkinter import *
from math import ceil as ceil

wb = openpyxl.load_workbook('result.xlsx')
sheet = wb.active

app = Tk()
app.title("Corrector de examenes")


#Parametros de usuario
correct = []
answers = []
#questions = int(input("¿Cuantas preguntas tiene el examen?: "))
questions = int(input("¿Cuantas preguntas tiene el examen?: "))

#alternativas = int(input("¿Cuantas alternativas tiene cada pregunta?: \n"))
alternativas = 5
    

col_answer = 0
for i in range(1, questions + 1):
    Label(app, text="Pregunta " + str(i) + ": ").grid(row=(i-1)%25, column=(ceil(i/25)-1)*2)
    ans = Entry(app, width=2)
    ans.grid(row=(i-1)%25,column= (ceil(i/25)-1)*2+1)
    answers.append(ans)


def correct_answers():
    for i in range(1, questions + 1):
        correct.append(ord((answers[i-1].get()).upper())-64)

Button(app, text="print", command=lambda : correct_answers() ).grid(row=questions, column=1, sticky=W+E)



#Parametros de usuario
vCorrecta = float(input("\n¿Cuantos puntos vale una respuesta correcta?: "))
vIncorrecta = float(input("¿Cuantos puntos vale una respuesta incorrecta?: "))
vBlanco = float(input("¿Cuantos puntos vale una respuesta en blanco?: "))

#Detrás de escena
correctas = 0
incorrectas = 0

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

app.mainloop()