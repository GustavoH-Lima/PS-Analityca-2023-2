import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import statistics as st
def grafico_1(Indice_tratamento_coleta):#Esgoto tratado x Quantidade de múnicipios
    tam = len(Indice_tratamento_coleta)
    dicio = {"0.0":0,"0-10":0,'10-20':0,'20-30':0,'30-40':0,'40-50':0,
         '50-60':0,'60-70':0,'70-80':0,'80-90':0,'90-100':0,'100':0}
    for i in range(0,tam):
        valor = Indice_tratamento_coleta[i]

        if(valor==0): dicio['0.0']+=1
        elif(valor<=10):dicio['0-10']+=1
        elif(valor<=20):dicio['10-20']+=1
        elif(valor<=30):dicio['20-30']+=1
        elif(valor<=40):dicio['30-40']+=1
        elif(valor<=50):dicio['40-50']+=1
        elif(valor<=60):dicio['50-60']+=1
        elif(valor<=70):dicio['60-70']+=1
        elif(valor<=80):dicio['70-80']+=1
        elif(valor<=90):dicio['80-90']+=1
        elif(valor<100):dicio['90-100']+=1
        else:dicio['100']+=1

    x=[]
    y=[]
    for i in dicio.keys():
        x.append(i)
        y.append(dicio.get(i))

    plt.bar(x,y,color = "red")
    plt.xticks(x)
    plt.ylabel("Quantidade de municipios")
    plt.xlabel("Esgoto coletado e tratado (%)")
    plt.title("Quantidade de múnicipios que possuem tal (%) de esgoto tratado")
    plt.show()
    print(round((dicio.get('0.0') + dicio.get('0-10'))/tam*100,2),"%")

def formata(x):
    k=''
    for i in range(len(x)):
        if(x[i]!="."):k+=x[i]

    return k

def grafico_2(investimento,Populacao_2013,Indice_tratamento_coleta):#Relação invesmento/população x indice coletado
    x=[]
    for i in range(0,len(investimento)):   x.append(investimento[i]/Populacao_2013[i])
    plt.scatter(x,Indice_tratamento_coleta)
    plt.xlabel("Investimento por pessoa(R$)")
    plt.ylabel("Esgoto Tratado(%)")
    plt.title("Investimento x Esgoto tratado")
    plt.show()

def grafico_3(regioes,investimento,Indice_tratamento_coleta,uf): #Quanto cada região investe em tratamento / media de tratamento
    
    x=["Norte","Nordeste",'Centro-Oeste','Sudeste','Sul']
    y=[0,0,0,0,0]
    y2=[0,0,0,0,0]
    y2_qtd=[0,0,0,0,0]

    for i in range(0,len(uf)):
        regiao = uf[i]
        for j in regioes.keys():
            if (regiao in regioes.get(j)):
                y[int(j)]+=investimento[i]
                y2[int(j)]+=Indice_tratamento_coleta[i]
                y2_qtd[int(j)]+=1
    
    for i in range (len(y2_qtd)): #Fazendo a média
        y2[i]/=y2_qtd[i]

    plt.bar(x,y2)
    plt.xticks([0,1,2,3,4])
    plt.ylabel("Média(%)")
    plt.xlabel("Regiões")
    plt.title("Média de esgoto tratado por região")
    plt.show()
    
    plt.bar(x,y)
    plt.xticks([0,1,2,3,4])
    plt.ylabel("Investimento(R$)")
    plt.xlabel("Regiões")
    plt.title("Investimento em coleta e tratamento por região")
    plt.show()

def analise_futuro(Populacao_2013,Populacao_2035,vazao_sem_coleta,vazao_coletada_2013): #Analise da vazão de esgoto que será lançada sem tratamento em 2035
    total_2013 = 0
    total_2035 = 0 
    totalcoletado_2013=0 #Total de vazão sem coleta
    totalcoletado_2035=0
    for i in range(len(Populacao_2013)):
        pop=Populacao_2013[i]
        pop_f=Populacao_2035[i]
        vazao = vazao_sem_coleta[i]
        totalcoletado_2013+=vazao_coletada_2013[i]
        total_2013+=vazao
        indice=(vazao/pop) #Quanta Quantos litros por segundo sem tratamento e sem coleta são jogados por pessoa 
        total_2035 +=indice*pop_f
    totalcoletado_2035=totalcoletado_2013*pop_f/pop

    melhoria = round((totalcoletado_2035+total_2035)/totalcoletado_2035 *100,2)
    print("Vazão total coletada em 2013 e 2035: ",round(totalcoletado_2013,2),round(totalcoletado_2035,2))
    print("Vazao sem coleta e tratamento em 2013 e 2035: ",round(total_2013,2),round(total_2035,2))
    print("O quanto teriamos que coletar a mais para atender a ODS 6.2 em 2035: ",melhoria,"%",sep='')
    
def analise_estatistica(Indice_tratamento_coleta): #Desvio Padrão e Média
    media = st.mean(Indice_tratamento_coleta)
    desvio = st.stdev(Indice_tratamento_coleta)
    print('Média dos municípios:',round(media,2),
          '\nDesvio Padrão:',round(desvio,2))

dados = pd.read_csv("Esgoto_municipio.csv")
#0 = Norte, 1=Nordeste, 2=Centro-Oeste, 3=Sudeste, 4 = Sul
regioes={"0":["AC",'AP','AM','PA','RO','RR','TO'],
         "1":['AL','BA','CE','MA','PB','PE','PI','RN','SE'],
         "2":['DF','GO','MT','MS'],
         "3":['RJ','ES','MG','SP'],
         "4":['PR','RS','SC']}

k = dados.to_numpy()
Indice_tratamento_coleta=[]
investimento=[]
Populacao_2013=[]
Populacao_2035=[]
uf=[]
vazao_sem_coleta=[]
vazao_coletada_2013=[]
for i in range(len(k)):
        
        Indice_tratamento_coleta.append(float(k[i][10][:-1].replace(",",".")) + float(k[i][8][:-1].replace(",",".")))
        investimento.append(float(formata(k[i][36]).replace(",",".")))
        Populacao_2013.append(int(formata(k[i][3])))
        Populacao_2035.append(int(formata(k[i][4])))
        vazao_sem_coleta.append(float(formata(k[i][11]).replace(",",".")))
        vazao_coletada_2013.append(float(formata(k[i][13]).replace(",",".")) + float(formata(k[i][14]).replace(",","."))+float(formata(k[i][12]).replace(",",".")))
        uf.append(k[i][2])

grafico_1(Indice_tratamento_coleta)
grafico_2(investimento,Populacao_2013,Indice_tratamento_coleta)
grafico_3(regioes,investimento,Indice_tratamento_coleta,uf)
analise_futuro(Populacao_2013,Populacao_2035,vazao_sem_coleta,vazao_coletada_2013)
analise_estatistica(Indice_tratamento_coleta)
