from math import ceil
def entrada(): #576.73
    ent = input()

    if (ent[-3]!='.'):  return False
       
    for i in range(len(ent)): #Verificando se a entrada tem somente numeros
        if (i==len(ent)-3): continue
        elif (not ent[i].isnumeric()): return False
    
    return float(ent)

def calculadora(v):

    Notas = [100.0,50.0,20.0,10.0,5.0,2.0]
    Moedas = [1.0,0.5,0.25,0.10,0.05,0.01]
    
    print("NOTAS:")
    for i in Notas:
        print(int(v//i),"nota(s) de R$ {:.2f}".format(i))
        v = v%i

    print("MOEDAS:")
    for i in Moedas:
        print(int(round((v/i),2)),"moeda(s) de R$ {:.2f}".format(i))
        v=v%i



def Main():
        v =  entrada()
        if(v==False):
            print("Input inválido")   
        else: calculadora(v)

Main()