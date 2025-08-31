# Aluno: Guilherme Martins Rangel
# programa que recebe o identificador de cada categoria de dados (representado por uma letra)
# e o valor de sua frequência dos dados. Este programa imprime um mapa para projetar um gráfico de pizza,
# indicando a frequência de cada dado transformada em graus.
dados = int(input("Entre com a quantidade de dados: "))
if dados>0:
    count = 1
    frequencia_dados = []
    frequencia_dados_int = []
    identificador_dados = []
    frequencia_soma = 0
    lista_para_print = []
    for i in range(dados):
        identificador_dados.append(input(f"Entre com o identificador do dado {count}: "))
        frequencia_dados.append(input(f"Entre com a frequência do dado {identificador_dados[i]}: "))
        count+=1
    for z in range(len(frequencia_dados)):
        frequencia_dados_int.append(int(frequencia_dados[z]))
    for x in range(len(frequencia_dados_int)):
        frequencia_soma += frequencia_dados_int[x]
    graus = 360/frequencia_soma
    print("Mapeamento:")
    for y in range(len(frequencia_dados)):
        if frequencia_dados_int[y]*graus == int(frequencia_dados_int[y]*graus):
            print(f'"{identificador_dados[y]}": {frequencia_dados_int[y] * graus:.0f}')
        else:
            print(f'"{identificador_dados[y]}": {frequencia_dados_int[y]*graus:.1f}')