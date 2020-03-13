import sys
import random
import time
import matplotlib.pyplot as plt
import datetime

def print_Array(lista,endFormat):
	for i in lista:
		print(i,end=endFormat)
	print("")

def in_box():
    a=int(input())
    lista=input()
    lista=lista.split()
    lista = list(map(int, lista)) 
    if(len(lista)==a):    
        return lista
    else:
        return -1


def algoritmo_1(lista):
    metade=len(lista)/2
    for i in range(len(lista)):
        count=0
        for j in range(len(lista)):
            if(lista[j]==lista[i]):
                count+=1
        if(count>metade):
            return lista[i]
    return -1

def algoritmo_2(lista):
    metade=len(lista)/2
    chave=0
    for i in range(0,4):
        mask=2**i
        count=0
        for j in range(len(lista)):
            resultado=lista[j]&mask
            if(resultado==mask):
                count+=1
        if(count>metade):
            chave+=mask
        mask=mask*2 #dumb, already defined at beggining
    return chave

def verificar(lista,chave):
    count=0
    metade=len(lista)/2
    for i in range(len(lista)):
        if(lista[i]==chave):
            count+=1
    if(count>metade):
        return chave
    else:
        return -1


listaA=[]
listaB=[]
fich=open("C:/Users/Francisco Fernandes/Desktop/AED/ficha3/alg1.txt","w")

for i in range(0,10000,200):
    
    
    data=[random.randint(1,30) for j in range(i)]
    
    startA=datetime.datetime.now()
    chave=algoritmo_1(data)
    chave=verificar(data,chave)
    endA=datetime.datetime.now()

    duracaoA=endA-startA
    tempo=(duracaoA.seconds)*1000+(duracaoA.microseconds)/1000
    fich.write(str(i)+" "+str(tempo)+"\n")
    print(i)
    listaA.append(tempo)

fich.close()
plt.plot(listaA,".")
plt.show()

