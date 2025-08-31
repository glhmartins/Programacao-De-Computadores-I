# Aluno: Guilherme Martins Rangel
# programa que recebe uma lista com os elementos separados por espaço em branco,
# uma posição, retira o elemento na posição e imprime a lista com o elemento retirado.
elementos = input("Entre com os elementos da lista: ").split()
retirar = int(input("Entre com a posição do elemento a ser retirado: "))
lista_nova = elementos[:retirar] + elementos[retirar+1:]
lista_string = ""
for i in range(len(lista_nova)):
    lista_string += lista_nova[i] + " "
print("Lista: " + lista_string)