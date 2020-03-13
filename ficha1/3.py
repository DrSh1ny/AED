import sys 

def delete_columm(matrix,index):
    aux=[]
    for i in range(len(matrix)):
        aux.append(matrix[i][index])
        del matrix[i][index]
    return matrix,aux

def delete_line(matrix,index):
    aux=matrix[index]
    del matrix[index]
    return matrix,aux

def insert_columm(matrix,index,aux):
    for i in range(len(matrix)):
        matrix[i].insert(index,aux[i])
    return matrix

def insert_line(matrix,index,aux):
    matrix.insert(index,aux)
    return matrix


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (j==len(matrix[i])-1):
                #print(str(matrix[i][j]),end="\n")
                sys.stdout.write(str(matrix[i][j])+ "\n")
            else:
                #print(str(matrix[i][j]),end=" ")
                sys.stdout.write(str(matrix[i][j])+ " ")

def append_in_heigth(matrixA,matrixB):
    for line in matrixB:
        matrixA.append(line)
    return matrixA

def append_in_length(matrixA,matrixB):
    for i in range(len(matrixA)):
        matrixA[i]=matrixA[i]+matrixB[i]
    return matrixA


def in_box():
    #a=input()
    a=sys.stdin.readline()
    a=a.split(" ")
    linhas=int(a[0])
    colunas=int(a[-1])
    if(colunas<=0 or linhas<=0):
        exit()

    matrix=[[0 for i in range(colunas)] for i in range(linhas)]
    for i in range(linhas):
        linha=sys.stdin.readline()
        linha=(linha.split(' '))
        for j in range(colunas):
            linha[j]=int(linha[j])
        for k in range(colunas):
            matrix[i][k]=linha[k]
    
    if(linhas==1 and colunas==1):
        print(matrix[0][0])
        exit()
    return matrix

def submatrix(matrix,start_line,end_line,start_columm,end_collum):
    sub=matrix[start_line:end_line]
    for i in range(len(sub)):
        sub[i]=sub[i][start_columm:end_collum]
    return sub

def core_sort_of(matrix):
    if(len(matrix)==0 or len(matrix[0])==0):
        return matrix
    metade_coluna=int(len(matrix[0])/2)
    metade_linha=int(len(matrix)/2)
    fim_linha=int(len(matrix))
    fim_coluna=int(len(matrix[0]))


    matrixA=submatrix(matrix,0,metade_linha,0, metade_coluna)
    matrixB=submatrix(matrix,0,metade_linha,metade_coluna,fim_coluna)
    matrixC=submatrix(matrix,metade_linha,fim_linha,0,metade_coluna)
    matrixD=submatrix(matrix,metade_linha,fim_linha,metade_coluna,fim_coluna)
    
    final1=append_in_heigth(matrixD,matrixB)
    final2=append_in_heigth(matrixC,matrixA)
    end=append_in_length(final1,final2)
    
    return end

def main():
    matrix=in_box()
    
    
    n_linhas=len(matrix)
    n_colunas=len(matrix[0])
    
    aux_linhas=0
    aux_colunas=0
    if(n_linhas%2!=0):
        matrix,aux_line=delete_line(matrix,int(n_linhas/2))
        aux_linhas=1
    if(n_colunas%2!=0):
        matrix,aux_columm=delete_columm(matrix,int(n_colunas/2))
        aux_colunas=1

    final=core_sort_of(matrix)
    
    if(aux_colunas==1):
        final=insert_columm(final,int(len(final[0])/2),aux_columm)
    if(aux_linhas==1):
        final=insert_line(final,int(len(final)/2),aux_line)
    
    print_matrix(final)


if __name__=="__main__":
    main()
        