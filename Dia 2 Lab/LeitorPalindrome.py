# Alunos: Guilherme Martins Rangel e João Pedro Balaciano | Turma: A1 | Matéria: Programação I
# Programa que lê um número inteiro de 5 dígitos e indica se ele é um palíndromo.
# Um número palíndromo se lido da esquerda para a direita ou da direita para a esquerda possui o mesmo valor.
# Variável que recebe o número de 5 digitos
numero = int(input("Entre com um número inteiro de 5 digitos: "))
# Condição para verificar se o número é palíndromo ou não
if (numero//10000 == numero%10) and ((numero%10000)//1000) ==(numero%100)//10:
    print("O número é palíndromo")
else :
    print("Não é palíndromo")