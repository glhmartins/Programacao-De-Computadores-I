# Alunos: Guilherme Martins Rangel | Turma: A1 | Matéria: Programação I
# Programa que recebe 6 números digitados pelo usuário e retorna quantos são positivos
# e a media deles
somapositivos = 0
numerospositivos = 0
for numeros in range(6):
    numero = float(input("Entre com um valor:"))
    if numero > 0:
        somapositivos = somapositivos + numero
        numerospositivos +=1
print(numerospositivos, "valores positivos")
print(somapositivos/numerospositivos)
