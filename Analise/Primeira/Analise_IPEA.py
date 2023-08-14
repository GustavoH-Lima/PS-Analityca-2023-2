import pandas as pd
import statistics

def Compara_adiciona(dicio,k,i): #Função que se a cidade não estiver no dicionário, adiciona ela , caso já esteja, adiciona o novo valor.
       if (k[i][0] in dicio.keys()): 
              dicio[k[i][0]].append(int(k[i][2])) #Colocando os valores no array
              
       else:
              dicio[k[i][0]]=[int(k[i][2])] #Se a chave não estiver no dicionário, cria ela
       return dicio

def Estatisticas(dicio,valores,vez): #Função que faz as estatíticas Desvio Padrão /Média
       for i in dicio.keys(): 
              Desvio=statistics.stdev(dicio.get(i))
              media =statistics.mean(dicio.get(i))
              if (i in valores.keys()): 
                     valores[i].append((vez,Desvio,media)) #Colocando os valores no array
              
              else:
                     valores[i]=[(vez,Desvio,media)]    #Se os valores não estiverem presentes, cria eles
       return valores

def analisando(vez,valores,valores_publico):
       use =["name_muni","mode",vez]

       dados=pd.read_csv("aop_access_publictransport_2019_v2.csv",usecols=use)
       k=dados.to_numpy()
       
       dicio={} #Dicionario para carros
       dicio_p={} #Dicionario para Transporte Público

       for i in range(0,len(k),2): #Somando de 2 em 2 pra pegar somente os horários de pico
              if(k[i][1]=="car"):
                     dicio=Compara_adiciona(dicio,k,i)  

              else:
                     dicio_p=Compara_adiciona(dicio_p,k,i)

       valores=Estatisticas(dicio,valores,vez)
       valores_publico=Estatisticas(dicio_p,valores_publico,vez)


       return valores,valores_publico

def escrevendo_csv(valores,dados,nome): #Função pra sumarizar os dados em um CSV e não precisar rodar o código que demora ~1m 45s pra ser executado quando for construir as tabelas
       p = open(nome,"w+")
       p.write("Municipios")
       for i in dados:
              p.write(","+i)
       p.write("\n")


       for i in valores.keys():
              p.write("\""+i+"_DesvioPadrao\"")
              for j in valores.get(i):
                     p.write(",\""+str(round(j[1],2))+"\"") #Escrevendo o desvio padrão
              p.write('\n'+"\""+i+"_Media\"")
              for j in valores.get(i):
                     p.write(",\""+str(round(j[2],2))+"\"") # Escrevendo a média
              p.write("\n")
       p.close()

valores_carro={} #carro
valores_publico={} #transporte público
use = [ "CMATT15","CMATT30","CMATT60","CMATT90","CMATT120"
       ,"CMAST15","CMAST30","CMAST60","CMAST90","CMAST120"
       ,"CMAET15","CMAET30","CMAET60","CMAET90","CMAET120"
       ,"CMAMT15","CMAMT30","CMAMT60","CMAMT90","CMAMT120"
       ,"CMACT15","CMACT30","CMACT60","CMACT90","CMACT120"]


for i in use:
       valores_carro,valores_publico=analisando(i,valores_carro,valores_publico)

escrevendo_csv(valores_carro,use,"Sumario_Carros.csv")
escrevendo_csv(valores_publico,use,"Sumario_Publico.csv")