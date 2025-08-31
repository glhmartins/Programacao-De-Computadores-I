# Aluno: Guilherme Martins Rangel
# programa que recebe uma lista, um elemento e imprime a posição do elemento na lista.
elementos = input("Entre com os elementos da lista: ").split()
busca = input("Entre com o elemento a ser encontrado: ").strip()
for x in range(len(elementos)):
    if elementos[x] == busca:
        print("O elemento", busca," está na posição", x)