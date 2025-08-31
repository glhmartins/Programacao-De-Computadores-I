# Aluno: Guilherme Martins Rangel e João Pedro Balaciano | Turma: A1 | Matéria: Programação I
# programa que lê um valor qualquer e apresenta uma mensagem que diz em qual dos seguintes intervalos
# ([0,25], (25,50], (50,75], (75,100]) o valor se encontra.
# Caso  o valor não esteja em nenhum dos intervalos, será mostrada a mensagem “Fora de intervalo”.
# Variável que recebe o número digitado pelo usuário
numero = float(input("Entre com um número real: "))
# Condição caso o número esteja entre 0 e 25
if 0<=numero<=25:
    print("Intervalo [0,25]")
# Condição caso o número seja maior que 25 e menor ou igual a 50
elif 25<numero<=50:
    print("Intervalo (25,50]")
# Condição caso o número seja maior que 50 e menor ou igual a 75
elif 50<numero<=75:
    print("Intervalo (50,75]")
# Condição caso o número seja maior que 75 e menor ou igual a 100
elif 75<numero<=100:
    print("Intervalo (75,100]")
# Condição caso o número esteja fora do intervalo
else :
    print("Fora do intervalo")