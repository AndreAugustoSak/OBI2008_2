def sedex(diam_bola, alt_caixa, larg_caixa, prof_caixa):
    if alt_caixa < diam_bola or larg_caixa < diam_bola or prof_caixa < diam_bola:
        return False
    else:
        return True
print(sedex(9,15,9,10))