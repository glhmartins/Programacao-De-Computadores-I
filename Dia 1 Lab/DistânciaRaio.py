# Aluno: Guilherme Martins Rangel / Turma: A1 / Matéria: Programação I
# Programa que calcula a distância em quilômetros que o raio caiu baseado no tempo que leva até o trovão ser escutado
# Assuma que velocidade do som é 340m/s
VelocidadeSom = 340
TempoTrovão = float(input("Entre com o tempo em segundos: "))
# Guarda o tempo em segundos que levou entre a visualização do raio e escutar o trovão
DistanciaRaio = (VelocidadeSom * TempoTrovão)/1000
# Calcula a distância que o raio caiu em quilometros
print(DistanciaRaio, "Km")