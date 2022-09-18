import openpyxl

wb = openpyxl.load_workbook('result.xlsx')
sheet = wb.active

#Parametros de usuario
correct = [1, 4, 2, 4, 5]
questions = 5
alternativas = 5

vCorrecta = 5
vIncorrecta = -1
vBlanco = 0


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
            print(option+1, " ", question)
            if option+2 == correct[question]:
                correctas += 1
            else:
                incorrectas += 1


print(vCorrecta*correctas + vIncorrecta*incorrectas + vBlanco*(questions - correctas - incorrectas))