# Alunos: Guilherme Martins Rangel | Turma: A1 | Matéria: Programação I
# Programa que o usuário digita um número inteiro positivo e descobrimos a quantidade
# de divisores do número
question = input("Deseja entrar com um número(S/N)")
while question == "S":
    if question == "S":
        numero = int(input("Entre com o número: "))
        number = 1
        divisores = 0
        while number <= numero:
            resultado = numero%number
            if resultado == 0:
                print(number)
                divisores+=1
            number+=1
        if divisores ==2:
            print("Número é primo")
        question = input("Deseja entrar com um número(S/N)")