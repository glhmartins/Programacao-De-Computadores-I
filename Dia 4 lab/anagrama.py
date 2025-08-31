# Aluno: Guilherme Martins Rangel | Turma: A1 | Matéria: Programação I
# programa que leia duas strings e indica se elas são anagramas. Dizemos que duas palavras são anagramas
# se a primeira palavra pode ser transformada na segunda palavra somente pela troca de posição de seus caracteres.
palavras = input('Entre com duas palavras: ').strip().split()
palavra0 = (palavras[0]).lower()
palavra1 = (palavras[1]).lower()
word0 = ""
word1 = ""
alfabeto = "abcdefghijklmnopqrstuvwxyz"

for caracter in alfabeto:
    contador = 0
    inicio = 0
    comeco = 0
    x = 0

    while palavra0.find(caracter, comeco) != -1 and comeco != -1:
        comeco = palavra0.find(caracter, comeco)
        comeco = palavra0.find(caracter, comeco + 1)
        contador += 1

    while x != contador:
        if palavra0.find(caracter, inicio) != -1:
            word0 = word0 + caracter
            inicio = palavra0.find(caracter, inicio)
            x += 1

for caracter1 in alfabeto:
    contador1 = 0
    inicio1 = 0
    comeco1 = 0
    x1 = 0
    while palavra1.find(caracter1, comeco1) != -1 and comeco1 != -1:
        comeco1 = palavra1.find(caracter1, comeco1)
        comeco1 = palavra1.find(caracter1, comeco1 + 1)
        contador1 += 1

    while x1 != contador1:
        if palavra1.find(caracter1, inicio1) != -1:
            word1 = word1 + caracter1
            inicio1 = palavra1.find(caracter1, inicio1)
            x1 += 1

if word0 == word1:
    print(palavras[0], "e", palavras[1], "são anagramas")
else:
    print(palavras[0], "e", palavras[1], "não são anagramas")