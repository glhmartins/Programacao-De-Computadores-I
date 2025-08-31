# Aluno: Guilherme Martins Rangel
# Programa que recebe um número inteiro e que retorna a função de Lempner deste número que é o menor inteiro
# maior que zero cujo fatorial é dividido exatamente pelo número.
import math
def kempner(x):
    count = 1
    fatorial = 1
    while fatorial%x != 0:
        fatorial = math.factorial(count)
        if fatorial%x != 0:
            count+=1
    return count