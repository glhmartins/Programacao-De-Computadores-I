# Aluno: Guilherme Martins Rangel / Turma: A1 / Matéria: Programação I
# Programa onde o usuário informa um valor em centavos e é exibido a menor quantidade de moedas que formam tal valor
MoedasCentavos = int(input("Entre com o valor em centavos: "))
# Guarda o valor em centavos digitado pelo usuário
# Moeda é a variável de péssimo nome usada para guardar quantas moedas tem de cada
# Resto é a variável usada para guardar o resto da divisão da moeda anterior
Moeda1real = MoedasCentavos//100
Resto1real = MoedasCentavos%100
Moeda50centavos = Resto1real//50
Resto50centavos = Resto1real%50
Moeda25centavos = Resto50centavos//25
Resto25centavos = Resto50centavos%25
Moeda10centavos = Resto25centavos//10
Resto10centavos = Resto25centavos%10
Moeda5centavos = Resto10centavos//5
Resto5centavos = Resto10centavos%5
Moeda1centavos = Resto5centavos
print("Para o valor " + str(MoedasCentavos) + " centavos, a menor quantidade de moedas é: ")
print(str(Moeda1real) + " moeda(s) de 1 real ")
print(str(Moeda50centavos) + " moeda(s) de 50 centavos")
print(str(Moeda25centavos) + " moeda(s) de 25 centavos")
print(str(Moeda10centavos) + " moeda(s) de 10 centavos")
print(str(Moeda5centavos) + " moeda(s) de 5 centavos e")
print(str(Moeda1centavos) + " moeda(s) de 1 centavos.")