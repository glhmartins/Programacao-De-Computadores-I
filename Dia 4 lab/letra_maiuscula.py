# Aluno: Guilherme Martins Rangel | Turma: A1 | Matéria: Programação I
# programa que lê uma frase do usuário e coloca a primeira letra de
# cada palavra em maiúscula e o restante das letras da palavra em minúsculas.

frase = input("Entre com uma frase: ").strip().lower()
frase_modificada = ""

for x in range(len(frase)):
    if frase[x] == frase[0] or frase[x-1] == " ":
        frase_modificada = frase_modificada + frase[x].upper()
    else:
        frase_modificada = frase_modificada + frase[x]

print(frase_modificada)