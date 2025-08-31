# Aluno: Guilherme Martins Rangel
# programa que ativa uma função que recebe o nome de um arquivo texto e retorna a palavra mais repetida no arquivo.
def biggest_repetition(texto):
    lendo = open(texto,"r")
    words = lendo.readlines()
    palavra = ""
    maior = 0
    lista = []
    for i in words:
        lista.append(i.rstrip("\n"))
    for x in lista:
        y = lista.count(x)
        if y>maior:
            maior = y
            palavra = x
    lendo.close()
    return palavra