# Aluno: Guilherme Martins Rangel
# Programa que ativa uma função que recebe o nome de um arquivo texto e retorna a maior palavra do arquivo.
def maior_palavra(texto):
    lendo = open(texto,"r")
    words = lendo.readlines()
    palavra = ""
    for x in words:
        x = x.rstrip("\n")
        if len(x)>len(palavra):
            palavra = x
    lendo.close()
    return palavra