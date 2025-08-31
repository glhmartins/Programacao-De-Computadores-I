# Aluno: Guilherme Martins Rangel | Turma: A1 | Matéria: Programação I
# programa para converter um número inteiro positivo em string. O programa deve ler o número inteiro positivo
# e escrevê-lo como string indicando o tipo da variável que contém seu valor.
number = int(input("Entre com um número inteiro positivo: "))
number_string = ""
algarismos = "0123456789"

while number>0:
    for x in algarismos:
        if int(x) == number%10:
            number_string = number_string + x
    number = number//10

number = ""

for y in range(len(number_string)-1,-1,-1):
    number = number + number_string[y]

print('O número foi atribuido à variável do tipo "string" e tem o valor "'+ number +'"')