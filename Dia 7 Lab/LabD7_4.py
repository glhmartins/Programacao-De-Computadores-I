# Aluno: Guilherme Martins Rangel
# função que, recebe um layout de ocupação de assentos e o número de amigos n, e retorna o número de
# configurações disponíveis para todos os n amigos sentarem juntos.
def assentos(x):
    matriz = []
    sequencia = 0
    count = 0
    y = 0
    for _ in range(6):
        matriz.append(input().split())
    print(matriz)
    while y<=5:
        for i in range(7):
            if matriz[y][i] == "0":
                sequencia +=1
                if sequencia >= x:
                    count+=1
            else:
                sequencia = 0
        sequencia = 0
        y+=1
    return count