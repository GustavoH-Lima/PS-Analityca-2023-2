def CriandoDicionario():
    t = {}
    t["a"] = 0
    t["b"] = 1
    t["c"] = 2
    t["d"] = 3
    t["e"] = 4
    t["f"] = 5
    t["g"] = 6
    t["h"] = 7
    return t

def entrada():
    dicio = CriandoDicionario()
    ent = input()
    if(ent == 'f'): return ent
    if (len(ent)!=5):
        print("Input inválido")
        return False
    
    A = ent[0] in dicio.keys() and ent[3] in dicio.keys() #Verificando se as linhas estão corretas
    B = ent[1].isnumeric() and ent[4].isnumeric() #Verificando se as colunas são números
    if(B):
        C = int(ent[1]) > 0 and int(ent[4]) > 0 #Verificando se as colunas são maiores que 0
        D = int(ent[1]) < 9 and int(ent[4]) < 9 #Verificando se as colunas são menores que 9
    else: C=D=False
    E = ent[2] == " " #Verificando o espaço no meio

    if(A and B and C and D and E):return ent
    else: 
        print("Input inválido")
        return False
    
def Verifica(ent):
    dicio = CriandoDicionario()
    dif_lin = abs(dicio.get(ent[0]) - dicio.get(ent[3]))
    dif_col = abs(int(ent[1]) - int(ent[4]))

    if (dif_col == 1 and dif_lin == 2 or dif_col==2 and dif_lin == 1): print("VÁLIDO")
    else: print("INVÁLIDO")
        
def Main():
    while(1):
        ent = entrada()
        if(ent == 'f'):
            print("Fim...")
            break
        elif(ent == False):
            continue
        else:
            Verifica(ent)

Main()