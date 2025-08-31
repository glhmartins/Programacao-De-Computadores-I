# Aluno: Guilherme Martins Rangel
# Função que recebe uma lista de três números (não ordenados) e retorna True se os números
# constituírem uma tripla pitagórica primitiva, caso contrário False.
def pitas_primitivo(x,y,z):
    lista = [x,y,z]
    C = max(lista)
    A = min(lista)
    lista.remove(C)
    lista.remove(A)
    B = lista[0]
    condition = False
    if (A**2) + (B**2) == C**2:
        divisoresA = []
        divisoresB = []
        divisoresC = []
        divisoresAB = 0
        divisoresAC = 0
        divisoresBC = 0
        # Usei if em todas as condicionais pois caso eu usasse elif e o if fosse verdadeiro o elif era ignorado
        for i in range(1,C+1):
            if A%i == 0 and i<=A:
                divisoresA.append(i)
            if B%i == 0 and i<=B:
                divisoresB.append(i)
            if C%i == 0:
                divisoresC.append(i)
        for l in divisoresA:
            if l in divisoresB:
                divisoresAB+=1
            if l in divisoresC:
                divisoresAC+=1
        for m in divisoresB:
            if m in divisoresC:
                divisoresBC+=1
        if divisoresAB==1 and divisoresAC==1 and divisoresBC ==1:
            condition = True
    return condition