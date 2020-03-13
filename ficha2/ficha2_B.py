import sys

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

def algoritmo(lista,valor):
    comp=len(lista)
    
    for i in range(comp):
        soma=0
        for j in range(i,comp):
            soma+=lista[j]
            if(soma==valor):
                return i

    return -1

def main():
    lista=in_box()
    #print(lista)
    for i in range(0,len(lista),2):
        valor=lista[i]
        sub_lista=lista[i+1]
        index=algoritmo(sub_lista,valor)
        if(index==-1):
            print("SUBSEQUENCIA NAO ENCONTRADA")
        else:
            print("SUBSEQUENCIA NA POSICAO "+ str(index+1))
 
    
    




if __name__=="__main__":
    main()