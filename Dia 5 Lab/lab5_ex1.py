# Aluno: Guilherme Martins Rangel
# programa que recebe uma lista com os elementos separados por espaço em branco, um determinado
# elemento e indica o número de vezes que o elemento aparece na lista.
elemento = input("Entre com uma lista: ").split()
quantidade_elemento = 0
busca = input("Entre com um elemento para se verificar o número de vezes que ele aparece na lista: ").strip()
for x in range(len(elemento)):
    if busca == elemento[x]:
        quantidade_elemento +=1
print("O elemento ", busca," aparece ",quantidade_elemento," vezes na lista")