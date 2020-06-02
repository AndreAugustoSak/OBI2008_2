import lista06 as L06

def teste_avioes_de_papel():
    try:
        falhou = False
        if L06.avioes_de_papel (10,100,10) != True : falhou = True
        if L06.avioes_de_papel (10,90,10)  != False : falhou = True
        if L06.avioes_de_papel (5,40,2)  != True : falhou = True
        if falhou:
            print('Funcao avioes_de_papel NÃO está OK')
            return(0)
        else:
            print('Funcao avioes_de_papel está OK')
            return(2.0)
    except AttributeError as inst:
        print (inst)
        return(0)

def teste_numero_envelopes():
    try:
        falhou = False
        if L06.numero_envelopes([5,3,6,2]) != 2 : falhou = True
        if L06.numero_envelopes([10,5,21,3,0,11]) != 0 : falhou = True
        if falhou:
            print('Funcao numero_envelopes NÃO está OK')
            return(0)
        else:
            print('Funcao numero_envelopes está OK')
            return(2.0)
    except AttributeError as inst:
        print (inst)
        return(0)

def teste_overflow():
    try:
        falhou = False
        if L06.overflow(10,'5 + 5') != True : falhou = True
        if L06.overflow(44,'23 * 2') != False : falhou = True
        if L06.overflow(323500,'42 * 35') != True : falhou = True
        if falhou:
            print('Funcao overflow NÃO está OK')
            return(0)
        else:
            print('Funcao overflow está OK')
            return(2.0)
    except AttributeError as inst:
        print (inst)
        return(0)

def teste_garcom():
    try:
        falhou = False
        if L06.garcom (3, [(10,5),(6,8),(3,3)]) != 5 : falhou = True
        if L06.garcom (4, [(10,6),(8,8),(5,1),(100,100)]) != 7 : falhou = True
        if falhou:
            print('Funcao garcom NÃO está OK')
            return(0)
        else:
            print('Funcao garcom está OK')
            return(2.0)
    except AttributeError as inst:
        print (inst)
        return(0)

def teste_sedex():
    try:
        falhou = False
        if L06.sedex(3,2,3,5) != False : falhou = True
        if L06.sedex(5,5,5,5) != True : falhou = True
        if L06.sedex(9,15,9,10) != True : falhou = True
        if falhou:
            print('Funcao sedex NÃO está OK')
            return(0)
        else:
            print('Funcao sedex está OK')
            return(2.0)
    except AttributeError as inst:
        print (inst)
        return(0)

def teste_escadinha():
    try:
        falhou = False
        if L06.escadinha(8,[1,1,1,3,5,4,8,12]) != 4 : falhou = True
        if L06.escadinha(1,[112]) != 1 : falhou = True
        if L06.escadinha(5,[11,-106,-223,-340,-457]) != 1 : falhou = True
        if falhou:
            print('Funcao escadinha NÃO está OK')
            return(0)
        else:
            print('Funcao escadinha está OK')
            return(2.0)
    except AttributeError as inst:
        print (inst)
        return(0)

def nota_da_prova():
  nota =  teste_avioes_de_papel()
  nota += teste_numero_envelopes()
  nota += teste_overflow()
  nota += teste_garcom()
  nota += teste_sedex()
  nota += teste_escadinha()
  print("Seu somatorio de pontos:",nota)

#nota_da_prova()
