def avioes_de_papel (compet, fls_total, fls_compet):
    if (fls_total / compet) >= fls_compet:
        return True
    else:
        return False
print(avioes_de_papel (5,40,2))