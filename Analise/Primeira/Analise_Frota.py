import pandas as pd
def coleta():
    municipios = pd.read_csv("Sumario_Carros.csv",usecols=["Municipios"])
    validos = []
    for index, row in municipios.iterrows():
        muni = row[0][:row[0].find("_")].upper()
        if (muni not in validos):validos.append(muni)

    use=["MUNICIPIO","TIPO DE VEICULO",'QUANTIDADE']
    dados = pd.read_csv("Frota_2020.csv")
    i=0
    k = dados.to_numpy()

    infos={}
    while(i<len(k)):
        muni=k[i][1]
        if(muni not in validos): 
            i+=21
        else:
            if (muni == "BELEM" and k[i][0] != "PA" or muni == "CAMPO GRANDE" and k[i][0]!="MS"): #Existe outros belens e Campos grandes, por isso essa opção
                i+=21 #Esse jump é pra ir para o próximo municipio
                continue
            if(k[i][2]== "AUTOMOVEL" or k[i][2]=="ONIBUS" or k[i][2]=="MICRO-ONIBUS"):
                if (muni not in infos.keys()): infos[muni]= [(k[i][2],k[i][3])]
                else: infos[muni].append((k[i][2],k[i][3]))
            i+=1
    return infos

def escreve_csv(infos): #Colocando em um csv pois assim fica mais facil de coletar os dados depois
    p = open('Frota_resumida.csv','w+')

    p.write("MUNICIPIO,AUTOMOVEL,MICRO-ONIBUS,ONIBUS\n")
    for i in infos.keys():
        p.write("\""+i+"\","+"\""+str(infos[i][0][1])+"\",\""+str(infos[i][1][1])+"\",\""+str(infos[i][2][1])+"\"\n")

    p.close()
infos = coleta()
escreve_csv(infos)
