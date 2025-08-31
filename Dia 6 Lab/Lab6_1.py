# Aluno: Guilherme Martins Rangel
# programa que dada uma lista de inteiros que representam a cor de cada
# meia, imprime quantos pares de meias com cores correspondentes existem.
meia = input("Lista de meias = ").split()
pares = 0
meias_vistas = []
for x in range(len(meia)):
    if meia[x] not in meias_vistas:
        pares += meia.count(meia[x])//2
        meias_vistas.append(meia[x])
print(f"{pares} pares")