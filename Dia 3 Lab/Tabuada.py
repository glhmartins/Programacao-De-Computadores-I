# Alunos: Guilherme Martins Rangel | Turma: A1 | Matéria: Programação I
# Programa que monta a tabuada de 1 a N (N é o número digitado pelo usuário)
numero = int(input("Entre com o número final da tabela de multiplicação:"))
print("A tabela de multiplicação de 1 a", numero)
for base in range (1,numero +1):
    for multiplicador in range (1,numero +1):
        tabuada = base * multiplicador
        print(base,"x",multiplicador,"=",tabuada)