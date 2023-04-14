import dictionary
from math import sqrt,floor
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