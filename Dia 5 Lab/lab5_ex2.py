# Aluno: Guilherme Martins Rangel
# programa que recebe uma lista com os elementos separados por espaço em branco, um elemento,
# uma posição, insere o elemento na posição e imprime a lista com o elemento inserido.
elementos = input("Entre com os elementos da lista: ").split()
inserir = input("Entre com um elemento a ser inserido: ").split()
position = int(input("Entre com a posição para inserir o elemento: "))
lista_nova = elementos[0:position] + inserir + elementos[position:]
lista_string = ""
for i in range(len(lista_nova)):
    lista_string += lista_nova[i] + " "
print("Lista: " + lista_string)