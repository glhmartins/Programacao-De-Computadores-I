# Aluno: Guilherme Martins Rangel
# programa que ativa uma função que recebe dois parâmetros de entrada:
# o nome de um arquivo de entrada e o nome de um arquivo de saída.
def arquivos(entrada,saida):
    leitura = open(entrada,"r").readlines()
    escrita = open(saida,"w")
    matriz = []
    matriz_reordenada = []
    linha = None
    maior = 0
    for i in range(1,len(leitura)):
        conversao = leitura[i].split()
        country = ""
        for c in range(len(conversao)-3):
            country += f"{conversao[c]} "
        country+= "- "
        ouro = int(conversao[-3])
        prata = int(conversao[-2])
        bronze = int(conversao[-1])
        linha = [country, ouro, prata, bronze]
        matriz.append(linha)
    for w in range(len(matriz)):
        if matriz[w][1]>maior:
            maior = matriz[w][1]
            linha = matriz[w]
    matriz_reordenada.append(linha)
    matriz.remove(linha)
    matriz_range = matriz[:]
    linha2 = None
    for x in range(len(matriz_range)):
        linha2 = matriz[0]
        for y in range(len(matriz)):
            if linha2[1] < matriz[y][1] or linha2[1] == matriz[y][1]:
                if linha2[1]< matriz[y][1]:
                    linha2 = matriz[y]
                else:
                    if linha2[2] < matriz[y][2] or linha2[2] == matriz[y][2]:
                        if linha2[2] < matriz[y][2]:
                            linha2 = matriz[y]
                        else:
                            if linha2[3] < matriz[y][3]:
                                linha2 = matriz[y]
        matriz_reordenada.append(linha2)
        matriz.remove(linha2)
    escrita.write("Team - Gold - Silver - Bronze")
    escrita.write("\n")
    for z in range(len(matriz_reordenada)):
        for l in range(len(matriz_reordenada[z])):
            escrita.write(f"{matriz_reordenada[z][l]}  ")
        escrita.write("\n")
    escrita.close()
    leitura.close()
