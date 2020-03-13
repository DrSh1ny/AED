def inserirPalavra(lista,palavra,linha):
    for i in lista:
        if(palavra==i[0]):
            i.append(linha)
            return lista
    lista.append([palavra,linha])
    return lista

def procurarPalavra(lista,palavra):
    for i in lista:
        if(palavra==i[0]):
            return i[1:len(i)]
    return [-1]



separadores=[",",";","."]
lista=[]



inp=input()
if(inp=="TEXTO"):
    linha=input()
    count=0
    while(linha!="FIM."):
        linha=linha.lower()
        for elem in separadores:
            linha=linha.replace(elem," ")
        linha=linha.split()
        
        for palavra in linha:
            if(count not in procurarPalavra(lista,palavra)):
                lista=inserirPalavra(lista,palavra,count)
        linha=input()
        count+=1
    print("GUARDADO.")

inp=input()
while(inp):
    inp=inp.split()

    if(inp[0]=="LINHAS"):
        palavra=inp[1]
        
        count=procurarPalavra(lista,palavra)
        for i in count:
            print(i,end=" ")
        print("")
    
    if(inp[0]=="ASSOC"):
        palavra=inp[1]
        numLinha=inp[2]
        
        count=procurarPalavra(lista,palavra)
        if(numLinha in count):
            print("ENCONTRADA.")
        else:
            print("NAO ENCONTRADA.")
    inp=input()