# Aluno: Guilherme Martins Rangel
# Função que gera um tabuleiro de Xadrez. Ela recebe como entrada a variável n e dois elementos, e gera um
# tabuleiro n x n com os elementos alterados em cada casa.
def tabuleiro_xadrez(n,x,y):
    matriz = []
    linha1 = []
    linha2 = []
    for _ in range(n):
        if len(linha1)<n:
            linha1.append(x)
        if len(linha1)<n:
            linha1.append(y)
    for _ in range(n):
        if len(linha2) <n:
            linha2.append(y)
        if len(linha2) <n:
            linha2.append(x)
    for _ in range(n):
        if len(matriz) <n:
            matriz.append(linha1)
        if len(matriz) <n:
            matriz.append(linha2)
    return matriz