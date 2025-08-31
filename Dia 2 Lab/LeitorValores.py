# Alunos: Guilherme Martins Rangel e João Pedro Balaciano | Turma: A1 | Matéria: Programação I
# Programa que lê 4 valores inteiros A,B,C e D.
A = int(input("Entre com o valor de A: "))
B = int(input("Entre com o valor de B: "))
C = int(input("Entre com o valor de C: "))
D = int(input("Entre com o valor de D: "))

# Se B for maior que C e D for maior que A, e a soma de C e D for maior que a soma de A e B
# e se C e D, ambos, forem positivos e se a variável A for par escrever a mensagem "Valores aceitos", senão escrever "Valores não aceitos".
if (B>C and D>A and C+D>A+B and C>0 and D>0 and A%2==0):
    print("Valores aceitos")
else :
    print("Valores não aceitos")