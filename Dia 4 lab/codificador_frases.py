# Aluno: Guilherme Martins Rangel | Turma: A1 | Matéria: Programação I
# programa que implementa a codificação de uma word com uma chave fornecida pelo usuário.
# A codificação é feita trocando cada caractere da word com seu caractere espelho da chave.
frase = input("Entre com a frase: ").strip().lower()
chave = input("Entre com a chave: ").strip().lower()
codigo = ""
frase_codificada = ""

if chave == "":
    chave = "abcdefghijklmnopqrstuvwxyz"

for x in range(len(chave) - 1, -1, -1):
    codigo = codigo + chave[x]

for y in frase:
    if y in chave:
        frase_codificada = frase_codificada + codigo[chave.find(y)]
    else:
        frase_codificada = frase_codificada + y

print(frase_codificada)