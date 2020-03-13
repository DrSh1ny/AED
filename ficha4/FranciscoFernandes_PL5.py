

separadores=[",",";","."]

lista=[]

inp=input()

if(inp=="TEXTO"):
    linha=input()
    while(linha!="FIM."):
        linha=linha.lower()
        for elem in separadores:
            linha=linha.replace(elem," ")
        linha=linha.split()
        lista.append(linha)
        linha=input()
    print("GUARDADO.")



inp=input()
while(inp):
    inp=inp.split()

    if(inp[0]=="LINHAS"):
        palavra=inp[1]
        countLinhas=[]
        for i in range(len(lista)):
            if(palavra in lista[i]):
                countLinhas.append(i)
        if(len(countLinhas)>0):
            for i in countLinhas:
                print(i,end=" ")
            print("")
        else:
            print("-1")

    if(inp[0]=="ASSOC"):
        palavra=inp[1]
        numLinha=inp[2]
        
        if(palavra in lista[int(numLinha)]):
            print("ENCONTRADA.")
        else:
            print("NAO ENCONTRADA.")
    inp=input()
    