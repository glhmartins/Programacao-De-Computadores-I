# Aluno: Guilherme Martins Rangel
# programa que verifica um tabuleiro final de jogo da velha e verifica se o
# ganhador é “X”, “O” ou “Empate”. O tabuleiro é representado por uma matriz 3 × 3.
matriz = []
vencedor = "Empate"
x = 0
for y in range(1,4):
    matriz.append(input(f"Entre com os elementos da linha {y}: ").split())
while vencedor == "Empate" and x<3:
    if matriz[x] == "X":
        vencedor = "X"
    elif matriz[x] == "O":
        vencedor = "O"
    elif matriz[0][x] == "X" and matriz[1][x] == "X" and matriz[2][x] == "X":
        vencedor = "X"
    elif matriz[0][x] == "O" and matriz[1][x] == "O" and matriz[2][x] == "O":
        vencedor = "O"
    elif matriz[0][2] == "X" and matriz[1][1] == "X" and matriz[2][0] == "X":
        vencedor = "X"
    elif matriz[0][2] == "O" and matriz[1][1] == "O" and matriz[2][0] == "O":
        vencedor = "O"
    elif matriz[0][0] == "X" and matriz[1][1] == "X" and matriz[2][2] == "X":
        vencedor = "X"
    elif matriz[0][0] == "O" and matriz[1][1] == "O" and matriz[2][2] == "O":
        vencedor = "O"
    x+=1
print(f"{vencedor} é o vencedor")