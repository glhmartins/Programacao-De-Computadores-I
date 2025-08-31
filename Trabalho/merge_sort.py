aleatorio50 = [2627, 180, 2935, 1725, 8062, 8303, 7608, 6102, 2694, 7629, 7247, 4262, 6314, 3419, 2368, 9878, 6247, 8812, 5118, 9591, 9442, 2140, 3331, 2933, 7285, 5472, 1075, 7845, 4028, 6343, 9220, 1017, 2479, 7949, 4497, 1440, 2261, 3180, 8109, 6142, 4921, 4377, 785, 7782, 9468, 2273, 1972, 3053, 5237, 1388]
def merge_sort(lista, inicio = 0, fim = None):
    if fim is None:
        fim = len(lista)
    if (fim-inicio)>1:
        meio = (fim-inicio)//2
        merge_sort(lista,inicio,meio)
        merge_sort(lista,meio,fim)
        merge(lista, inicio, meio, fim)
def merge(lista, inicio, meio, fim):
    esquerda_lista = lista[inicio:meio]
    direita_lista = lista[meio:fim]
    topo_esquerda, topo_direita = 0, 0
    for x in range(inicio, fim):
        if topo_esquerda>=(len(esquerda_lista)):
            lista[x] = direita_lista[topo_direita]
            topo_direita +=1
        elif topo_direita>=(len(direita_lista)):
            lista[x] = esquerda_lista[topo_esquerda]
            topo_esquerda+=1
        elif esquerda_lista[topo_esquerda] < direita_lista[topo_direita]:
            lista[x] = esquerda_lista[topo_esquerda]
            topo_esquerda+=1
        else:
            lista[x] = direita_lista[topo_direita]
            topo_direita += 1
print(merge_sort(aleatorio50))