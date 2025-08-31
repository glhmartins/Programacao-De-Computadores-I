# Aluno: Guilherme Martins Rangel / Turma: A1 / Matéria: Programação I
# Programa que lê o número do funcionário, as horas trabalhadas, o valor por hora trabalhada e cálculo do salário
numerofuncionario = input("Entre com o número do funcionário: ")
# Guarda o número do funcionário
horastrabalhadas = int(input("Entre com a quantidade de horas trabalhadas: "))
# Guarda as horas que o funcionário trabalhou
valorporhora = int(input("Entre com o valor da hora trabalhada: "))
# Guarda o valor que o funcionário ganha por hora trabalhada
salario = horastrabalhadas * valorporhora
# Cálculo que multiplica as horas trabalhadas pelo valor que o funcionário ganha por hora trabalhada
print("O funcionário de número" , numerofuncionario , "deve receber R$ " , salario)