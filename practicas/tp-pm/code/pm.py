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

if __name__=="__main__":
    print(reduceLen("caaadennaee"))
    print(reduceLen("aaabccddd"))
    print(isContained("amarillo","aaafffmmmarillzzzllhooo"))
    print(isContained("amarillo","aaafffmmmarilzzzhooo"))
    print(isContained("amarillo","aaaaillllfffzzzhrmmmooo"))
    
