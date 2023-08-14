def entrada(): #21:30
    ent = input()
    if(ent == 'f'): return ent
    if (len(ent)!=5):
        print("Input inválido")
        return False
    
    for i in range(len(ent)): #Verificando se a entrada tem somente numeros
        if (i==2): continue
        elif (not ent[i].isnumeric()): 
            print("Input inválido")
            return False
    
    if ( int(ent[:2]) < 25 and int(ent[3:])<61 and ent[2]==":"): return ent
    else: return False

def calculo(entrada):

    hora = int(entrada[:2])%12
    min = int(entrada[3:])%60

    ang_hora = hora*30 #A cada hora, o ponteiro da hora anda 30° (360/12)
    ang_min = min*6 #A cada minuto, o ponteiro do minuto anda 6° (360/60)

    dif_ang = abs(ang_hora - ang_min)
    if(dif_ang >180):  dif_ang = 360 - dif_ang
    print("O menor ângulo é de ",dif_ang,"°",sep='')

def Main():
    while(1):
        ent = entrada()
        if (ent == "f"):
            print("Fim...")
            break

        elif (ent == False):
            continue

        else:
            calculo(ent)

Main()