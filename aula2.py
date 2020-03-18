import matplotlib


class No():
    
    def __init__(self,palavra,indice):
        self.indices=[indice]
        self.palavra=palavra

        self.pai=None
        self.left=None 
        self.right=None 
        
        self.balanco=0
        self.alturaEsquerda=0
        self.alturaDireita=0

    def print(self):
        print(self.palavra,end=" ")
        print(str(self.indices)+" "+str(self.balanco)+" "+str(self.alturaEsquerda)+" "+str(self.alturaDireita))
        if(self.left):
            print("[E]",end=" ")
            self.left.print()
        if(self.right):
            print("[D]",end=" ")
            self.right.print()
    
    def addIndex(self,indice):
        if(indice not in self.indices):
            self.indices.append(indice)
    
    def find(self,palavra):
        if(palavra<self.palavra):
            if(self.left):
                chave=self.left.find(palavra)
            else:
                return None 

        elif(palavra>self.palavra):
            if(self.right):
                chave=self.right.find(palavra)
            else:
                return None
        elif(palavra==self.palavra):
            return self
        return chave
    
    def insert(self,novo):
        if(novo.palavra<self.palavra):
            if(self.left!=None):
                pai=self.left.insert(novo)
            else:
                self.left=novo
                return self
        if(novo.palavra>=self.palavra):
            if(self.right!=None):
                pai=self.right.insert(novo)
            else:
                self.right=novo
                return self
        return pai

    def reallyInsert(self,novo):
        pai=self.insert(novo)
        


raiz=No("Maca",1) 
novo=No("Pera",2)
novo1=No("Oliveira",2)

chave=raiz.insert(novo).palavra
raiz.insert(novo1)
raiz.print()
print(chave)

        
