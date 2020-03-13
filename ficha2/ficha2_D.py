import sys
import random
import time

def in_box():
    imp=input()
    main_lista=[]
    while(imp!="0 0"):
        imp=imp.split()
        n_sequencia=int(imp[0])
        valor=int(imp[1])
        
        lista=[]
        for i in range(n_sequencia):
            lista.append(int(input()))
        main_lista.append(valor)
        main_lista.append(lista)
        imp=input()
    return main_lista

def algoritmo_D(lista,valor):
    comp=len(lista)
    
    soma=0
    i=0
    j=0
    while(soma!=valor and i<comp):
        while(soma<valor and j<comp):
            soma+=lista[j]
            if(soma==valor):
                return i
            j+=1
        soma=soma-lista[i]
        i+=1
    if(soma==valor):
        return i

    return -1

def algoritmo_A(lista,valor):
    comp=len(lista)
    
    for i in range(comp):
        for j in range(i,comp):
            soma=0
            for z in range(i,j+1):
                soma+=lista[z]
            if(soma==valor):
                return i
        
    return -1

def algoritmo_B(lista,valor):
    comp=len(lista)
    
    for i in range(comp):
        soma=0
        for j in range(i,comp):
            soma+=lista[j]
            if(soma==valor):
                return i

    return -1

def algoritmo_C(lista,valor):
    comp=len(lista)
    
    for i in range(comp):
        soma=0
        j=i
        while(soma<valor and j<comp):
            soma+=lista[j]
            if(soma==valor):
                return i
            j+=1

    return -1

def main():
    for i in range(5,10):
        print("TAMANHO "+str(10**i))
        lista=[random.randrange(1,1000,1) for i in range(10**i)]
        valor=random.randrange(1,1000,1)
        """
        inicio=time.time()
        index=algoritmo_A(lista,valor)
        fim=time.time()
        duracao=str(fim-inicio)
        print("Algoritmo A - "+duracao)
        
        
        inicio=time.time()
        index=algoritmo_B(lista,valor)
        fim=time.time()
        duracao=str(fim-inicio)
        print("Algoritmo B - "+duracao)

        inicio=time.time()
        index=algoritmo_C(lista,valor)
        fim=time.time()
        duracao=str(fim-inicio)
        print("Algoritmo C - "+duracao)"""
        
        inicio=time.time()
        
        index=algoritmo_D(lista,valor)
        fim=time.time()
        duracao=str(fim-inicio)
        print("Algoritmo D - "+duracao)

    
 

if __name__=="__main__":
    main()