class dictionary():
    # función hash H (k) = k mod 9 => la tabla tiene 9 posiciones
    tablaHash:list
    m=9
    def fHash(self,key) -> int:
        return key%self.m
    def __init__(self):
        self.tablaHash=[None for i in range(self.m)]
    def __str__(self) -> str:
        cadena=[]
        for nodo in self.tablaHash:
            if nodo!=None:
                for elm in nodo:
                    cadena.append("%s:%s"%(elm.key,elm.value)) 
        return "{%s}"%("; ".join(cadena))
class dictionaryElement():
    key=None
    value=None


def insert(D:dictionary,key:any,value:any):
    pos=D.fHash(key)
    newElm=dictionaryElement()
    newElm.key=key
    newElm.value=value
    if D.tablaHash[pos]==None:
        D.tablaHash[pos]=[newElm]
    else:
        D.tablaHash[pos].append(newElm)
    return D

def search(D:dictionary,key:any):
    pos=D.fHash(key)
    elmHash=D.tablaHash[pos]
    if elmHash!=None:
        for nodo in elmHash:
            if nodo.key==key:
                return nodo.value
        return None
    else:
        return None

def delete(D:dictionary,key:any):
    pos=D.fHash(key)
    elmHash=D.tablaHash[pos]
    if len(elmHash)==1:
        D.tablaHash[pos].clear()
    else:
        for nodo in elmHash:
            if nodo.key==key:
                elmHash.remove(nodo)
                break    
    return D