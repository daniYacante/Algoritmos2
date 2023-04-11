def sonPermutaciones(cad1:str,cad2:str):
    listCad1=[c for c in cad1]
    listCad2=[c for c in cad2]
    listCad1.sort()
    listCad2.sort()
    if len(listCad1)==len(listCad2):
        print(funcHash(listCad1))
        print(funcHash(listCad2))
    else:
        return False
    return

def funcHash(key:list):
    suma=0
    for i in range(len(key)):
        suma+=ord(key[i])*pow(10,i*2)
    return suma


sonPermutaciones("hola","algo")