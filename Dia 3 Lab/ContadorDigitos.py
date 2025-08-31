# Alunos: Guilherme Martins Rangel | Turma: A1 | Matéria: Programação I
# Programa que contabiliza a quantidade de dígitos de um número inteiro positivo digitado pelo usuário
numero = int(input("Entre com um número inteiro positivo: "))
number = numero
# Uso a variavel number para guardar o número digitado pelo usuário pois o número digitado pelo usuário sera modificado
# pelo while
contador = 0
while numero > 0:
    numero = numero//10
    contador += 1
print("O número", number, "tem", contador, "dígitos")