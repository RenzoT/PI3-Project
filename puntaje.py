import openpyxl

wb = openpyxl.load_workbook('result.xlsx')
sheet = wb.active

#Parametros de usuario
correct = []
questions = int(input("¿Cuantas preguntas tiene el examen?: "))
alternativas = int(input("¿Cuantas alternativas tiene cada pregunta?: \n"))

for i in range(1, questions + 1):
    correct.append(ord((input("¿Cual es la respuesta correcta de la pregunta " + str(i) + "?: ")).upper())-64)
    
#Parametros de usuario
vCorrecta = float(input("\n¿Cuantos puntos vale una respuesta correcta?: "))
vIncorrecta = float(input("¿Cuantos puntos vale una respuesta incorrecta?: "))
vBlanco = float(input("¿Cuantos puntos vale una respuesta en blanco?: "))

#Detrás de escena
correctas = 0
incorrectas = 0

# for i in range(questions):
#     if sheet.cell(row = correct[i]+1, column = i+2).value == 'X':
#         correctas += 1
#     else:
#         incorrectas += 1

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