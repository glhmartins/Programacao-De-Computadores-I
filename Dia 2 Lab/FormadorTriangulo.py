# Alunos: Guilherme Martins Rangel e João Pedro Balaciano | Turma: A1 | Matéria: Programação I
# programa que lê as coordenadas de três pontos A, B e C num espaço
# 2D e indique se formam um triângulo, juntamente com o seu tipo (equilátero,isósceles e escaleno).
# Variáveis do triângulo

Ax = int(input("Entre com a coordenada X do ponto A: "))
Ay = int(input("Entre com a coordenada Y do ponto A: "))
Bx = int(input("Entre com a coordenada X do ponto B: "))
By = int(input("Entre com a coordenada Y do ponto B: "))
Cx = int(input("Entre com a coordenada X do ponto C: "))
Cy = int(input("Entre com a coordenada Y do ponto C: "))

# Comando que importa a biblioteca math
import math

# Calculando os lados do triângulo
DistaciaAB = math.sqrt((Bx-Ax)**2+(By-Ay)**2)
DistaciaAC = math.sqrt((Cx-Ax)**2+(Cy-Ay)**2)
DistaciaBC = math.sqrt((Cx-Bx)**2+(Cy-By)**2)

# Verificando se é possível formar um triângulo
if DistaciaAB + DistaciaBC > DistaciaAC and DistaciaBC + DistaciaAC > DistaciaAB and DistaciaAC + DistaciaAB > DistaciaBC:
    # Verificando se é um triângulo equilátero
    # Triângulo Equilátero: três lados iguais
    if DistaciaBC == DistaciaAB and DistaciaBC ==DistaciaAC and DistaciaAB == DistaciaAC:
        print("Equilátero")
    # Verificando se é um triângulo isósceles
    # Triângulo Isósceles: Dois lados iguais
    elif DistaciaAB == DistaciaBC or DistaciaAB == DistaciaAC or DistaciaBC == DistaciaAC :
        print("Isósceles")
    # Verificando se é um triângulo escaleno
    # Triângulo Escaleno: três lados diferentes
    else:
        print("Escaleno")
else:
    print("Não forma triângulo")