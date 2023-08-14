import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def Analise(tem_onibus,carro,publico,indice,servico):
    Media_onibus=[]
    Media_carro=[]

    for i in range(len(carro)):
        if(carro[i][0] in tem_onibus):
            Media_carro.append(carro[i][indice])
    for i in range(len(publico)):
        if(publico[i][0] in tem_onibus):
            Media_onibus.append(publico[i][indice])

    barWidth = 0.1
    plt.figure(figsize=(10,20))

    r1=np.arange(len(Media_carro))
    r2=[x + barWidth for x in r1]

    plt.bar(r1,Media_carro,color = 'red',width=barWidth,label='Media Carro')
    plt.bar(r2,Media_onibus,color = 'green',width=barWidth,label='Media Transporte Público')

    plt.xlabel ("Municipios")
    plt.ylabel ("Média de "+servico+" acessiveis em até 15 minutos")
    plt.xticks([r+barWidth for r in range(len(Media_carro))],["Fortaleza",'São Paulo','Rio de Janeiro','Curitiba','Porto Alegre','Belo Horizonte','Recife','Goiania','Campinas'])
    plt.title ("Média de "+ servico + " acessiveis em até 15 minutos por município")
    plt.legend()
    plt.show()

def Analise_Frota(frota,tipo,carro=0):
    Quantidade_acessivel_15=[]
    tam_frota=[]
    for i in range(len(frota)):
        for j in range(0,len(tipo),2):
            if (frota[i][0] in tipo[j][0].upper()):
                Quantidade_acessivel_15.append(float(tipo[j][1]))
                if(carro==0):tam_frota.append(frota[i][1]/1000)
                else: tam_frota.append(frota[i][2]+frota[i][3]/1000)


    if (carro ==0):nome="carro"
    else:nome ="ônibus"
    plt.scatter(Quantidade_acessivel_15,tam_frota)
    plt.xlabel("Quantidade de empregos acessíveis em 15 minutos")
    plt.ylabel("Tamanho da frota")
    plt.title("Oportunidades de emprego em 15 minutos x Frota de "+ nome)
    plt.show()

dados_frota = pd.read_csv("Frota_resumida.csv")
dados_carro = pd.read_csv("Sumario_Carros.csv")
dados_publico = pd.read_csv("Sumario_Publico.csv")

carro = dados_carro.to_numpy()
publico = dados_publico.to_numpy()
frota = dados_frota.to_numpy()

tem_onibus=['Fortaleza_Media','Sao Paulo_Media','Rio de Janeiro_Media','Curitiba_Media',
            'Porto Alegre_Media','Belo Horizonte_Media','Recife_Media','Goiania_Media','Campinas_Media']

#Analise(tem_onibus,carro,publico,1,"empregos")
#Analise(tem_onibus,carro,publico,6,"Postos de saúde")
Analise_Frota(frota,carro,0)
Analise_Frota(frota,publico,1)