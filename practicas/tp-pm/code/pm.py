def reduceLen(cadena):
    newCadena=""
    i=0
    l=len(cadena)-1
    while i<l:
        if not cadena[i]==cadena[i+1]:
            newCadena+=cadena[i]
            i+=1
        else:
            i+=2
            if i>=l:
                newCadena+=cadena[l]
    return newCadena

def isContained(pattern,cadena):
    i=0
    for c in cadena:
        if c==pattern[i]:
            if i==len(pattern)-1:
                return True
            else:
                i+=1
    return False
def isPatternContained(patter:str,cadena:str,comodin:str):
    partes=patter.split(comodin)
    indAnt=0
    for part in partes:
        ind=cadena[indAnt:].find(part)
        if ind==-1:
            return False
        else:
            indAnt+=ind+len(part)
    return True
def rabinKarp(cad1:str,cad2:str):
    m=len(cad1)#Patron P
    n=len(cad2)#Cadena T
    hashP=0
    hashT=0
    for i in range(len(cad1)):
        e=m-i-1
        hashP+=ord(cad1[i])*pow(128,e)
    for i in range(len(cad1)):
        hashT+=ord(cad2[i])*pow(128,m-i-1)
    fhash=lambda hAnt,a,b,l: 128*(hAnt-pow(128,l)*ord(a))+ord(b)
    for i in range(len(cad2)-len(cad1)):
        subC=cad2[i:i+m]
        if hashT==hashP:
            if cad1==subC:
                return True
        else:
            hashT=fhash(hashT,cad2[i],cad2[i+m],m-1)
    return False
def kmp(p:str,t:str):
    
    for i in range(len(p)):
        subC=p[0:i]
    return
def calPI(p:str):
    pi=[0 for i in range(len(p))]
    pi[0]=0
    
    return
if __name__=="__main__":
    print(reduceLen("caaadennaee"))
    print(reduceLen("aaabccddd"))
    print(isContained("amarillo","aaafffmmmarillzzzllhooo"))
    print(isContained("amarillo","aaafffmmmarilzzzhooo"))
    print(isContained("amarillo","aaaaillllfffzzzhrmmmooo"))
    print(isPatternContained("abtbatc","cabccbacbacab","t"))
    print(rabinKarp("cadd","abracadabra"))