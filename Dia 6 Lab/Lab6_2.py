# Aluno: Guilherme Martins Rangel
# programa que a partir de uma lista de inteiros que representam a
# quantidade em reais que uma única ação vale, retorna o lucro máximo que poderia
# ter sido obtido comprando ações no dia x e vendendo ações no dia y, onde y> x.
lista = input("Lista de valores = ").split()
lista_int = []
lucro = -1
for x in lista:
    lista_int.append(int(x))
for y in range(len(lista_int)-1):
    for z in range(1+y,len(lista_int)):
        possivel_lucro = lista_int[z] - lista_int[y]
        if possivel_lucro>lucro:
            lucro = possivel_lucro
if lucro>0:
    print(f"Lucro máximo é {lucro}")
else:
    print(f"Lucro máximo é {lucro}")