def escadinha(tam_lista, lista):
    quantidade = 1
    if tam_lista == 1 or tam_lista == 2:
        quantidade = quantidade
    else:
        difAtual = lista[0] - lista[1]
        for indice in range(1, tam_lista - 1):
            difNova = lista[indice] - lista[indice + 1]
            if difAtual != difNova:
                difAtual = difNova
                quantidade += 1
    return quantidade
print(escadinha(5,[11,-106,-223,-340,-457]))