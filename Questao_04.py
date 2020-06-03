def garcom(bandejas, lista):
    copos_quebrados = 0
    for c in lista:
        latas = c[0]
        copos = c[1]
        if latas > copos:
            copos_quebrados += copos
    return copos_quebrados
print(garcom (4, [(10,6),(8,8),(5,1),(100,100)]))
