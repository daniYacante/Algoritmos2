import dictionary
from math import sqrt,floor
from random import randint
"""
Ejercicio 3
"""
print("Ejercicio 3")
def fhash(key):
    a=(sqrt(5)-1)/2
    m=1000
    return floor(m*(key*a-floor(key*a)))
print([fhash(x) for x in [61,62,63,64,65]])

"""
Ejercicio 4
"""
print("Ejercicio 4")
def sonPermutaciones(cad1:str,cad2:str):
    listCad1=[c for c in cad1]
    listCad2=[c for c in cad2]
    listCad1.sort()
    listCad2.sort()
    if len(listCad1)==len(listCad2):
        key1=strToKey(listCad1)
        key2=strToKey(listCad2)
        if key1==key2:
            return True
        else:
            return False
    else:
        return False

def strToKey(key:list):
    suma=0
    for i in range(len(key)):
        suma+=ord(key[i])*pow(128,i)
    return suma

print(sonPermutaciones("hola","aloh"))
print(sonPermutaciones("casa","aloh"))

"""
Ejercicio 5
"""
print("Ejercicio 5")
def isSet(l:list):
    conjunto=dictionary.dictionary()
    for item in l:
        if dictionary.search(conjunto,item)==None:
            dictionary.insert(conjunto,item,item)
        else:
            return False
    return True

print(isSet([1,5,12,1,2]))
print(isSet([1,5,12,3,2]))

"""
Ejercicio 6
"""
print("Ejercicio 6")
def zipHash(codigo:str):
    if len(codigo)<9:
        m=1013
        a=(sqrt(5)-1)/2
        funcHash=lambda key: floor(m*(key*a-floor(key*a)))
        c1=codigo[0]
        c2=codigo[1:5]
        c3=codigo[5:]
        key=strToKey(c1)+int(c2)+strToKey(c3)
        pos=funcHash(key)
        print(pos)
        return pos

    else:
        return None
zipHash("A9514BFJ")

"""
Ejercicio 7
"""

"""
Ejercicio 8
"""

def findString(pattern:str, string:str):
    keyPattern=strToKey([c for c in pattern])
    n=len(pattern)
    m=len(string)
    for i in range(m-n+1):
        keyStringCut=strToKey(string[i:i+n])
        if keyPattern==keyStringCut:
            if pattern==string[i:i+n]:
                return i
    return None 



findString("cada","abradacadabra")

"""
Ejercicio 9
Complejidad:
    Insertar elementos de T en la tabla: O(n), insertar es O(1)
    Buscar los elementos de S en la tabla: O(m), calculo de key O(1), búsqueda en la posición indicada O(n/m)
    Total: O(n+m)

"""

def checkSubSet(setS:list,setT:list):
    setS=set(setS)
    setT=set(setT)
    hashTable=[None for i in range(len(setT))]
    m=len(hashTable)
    a=(sqrt(5)-1)/2
    funcHash= lambda key: floor(m*(key*a-floor(key*a)))
    for elem in setT:
        pos=funcHash(elem)
        if hashTable[pos]==None:
            hashTable[pos]=[elem]
        else:
            hashTable[pos].append(elem)
    # print(hashTable)
    for elem in setS:
        HC=False
        pos=funcHash(elem)
        if hashTable[pos]!=None:
            for val in hashTable[pos]:
                if val==elem:
                    HC=True
            if not HC:
                return False
        else:
            return False
        return True
    
print("Random S y T")
s1=[randint(1,50) for i in range(5)]
s2=[randint(1,50) for i in range(10)]
print("S: ",s1,"\nT:",s2)
print(checkSubSet(s1,s2))
print("S y T a mano")
s1=[9,11,5,3,1]
s2=[8,4,3,1,2,9,11,5,21,27]
print("S: ",s1,"\nT:",s2)
print(checkSubSet(s1,s2))
"""
Ejercicio 10
"""
print("Ejercicio 10")
def ej10():
    keys=[10,22,31,4,15,28,17,88,59]
    print("Keys:\n",keys)
    m=11
    c1=1
    c2=3
    h1=lambda key: key
    h2=lambda key: 1+(key%(m-1))
    fHashLin=lambda key: key%m
    fHashCuad=lambda key,i: (key+c1*i+c2*pow(i,2))%m
    fHashHash=lambda key,i: (h1(key)+i*h2(key))%m
    tHashLin=[None for i in range(m)]
    tHashCuad=[None for i in range(m)]
    tHashHash=[None for i in range(m)]

    for i in range(len(keys)):
        for j in range(m):
            pos=fHashLin(keys[i]+j)
            if tHashLin[pos]==None:
                tHashLin[pos]=keys[i]
                break
            else:
                continue
        for j in range(m):
            pos=fHashCuad(keys[i],j)
            if tHashCuad[pos]==None:
                tHashCuad[pos]=keys[i]
                break
            else:
                continue
        for j in range(m):
            pos=fHashHash(keys[i],j)
            if tHashHash[pos]==None:
                tHashHash[pos]=keys[i]
                break
            else:
                continue
    print("Linear\n",tHashLin)
    print("Cuadrática\n",tHashCuad)
    print("Doble Hash\n",tHashHash)

ej10()