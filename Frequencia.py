def entrada():
    ent = input()

    if (ent == "f"): return ent
    for i in range(len(ent)):
        if(not ent[i].isnumeric()):
            return False
    
    return ent

def Main():

    contador = {}
    while(1):
        ent = entrada()
        if(ent == False):
            continue
        elif(ent=="f"):
            break
        else:
            try:
                contador[ent] = contador.get(ent) + 1 
            except TypeError:
                contador[ent] = 1

    for i in contador.keys():
        if (contador.get(i)==1): print("O número",i,"apareceu",1,"vez")
        else:print("O número",i,"apareceu",contador.get(i),"vezes")
    print("Fim...")
Main()