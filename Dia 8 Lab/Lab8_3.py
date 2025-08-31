# Aluno: Guilherme Martins Rangel
# programa que ativa uma função denominada letras_agrupadas que recebe um nome de arquivo e um número inteiro.
def alphabet(texto,n):
    alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    escrevendo = open(texto,"w")
    limite = 26//n
    count = 0
    x = n
    y = 0
    while count<limite:
        for i in range(y,x):
            escrevendo.write(str(alfabeto[i]))
        escrevendo.write("\n")
        y=x
        x+=n
        count+=1
    for j in range(y,26):
        escrevendo.write(str(alfabeto[j]))
    escrevendo.close()