from trie import *
from trie import __searchInList
"""
Prueba de funciones
"""
A=Trie()
insert(A,"holo")
insert(A,"hola")
insert(A,"holanda")
insert(A,"hipopotamo")
insert(A,"pez")
print(showTrieContent(A))
print("\"pe\" esta?: ",search(A,"pe"))
print("\"hola\" esta?: ",search(A,"hola"))
print("\"holanda\" esta?: ",search(A,"holanda"))
print("\"holonda\" esta?: ",search(A,"holonda"))
print("delete \"holanda\": ",delete(A,"holanda"))
print(showTrieContent(A))

"""
Ejercicio 4
Buscar palabras de longitud n que empiecen con un patron.
En principio planteo un algoritmo similar a search() para encontrar si el patron esta en el trie
luego en profundidad solo busco hasta n con una función similar a la de imprimir las palabras
"""
def __findWords(nl:List[TrieNode],cadenas:list,palabra:str,n):
	for node in nl:
		if node.isEndOfWord and n==0:
			cadenas.append(palabra+node.key)
		if node.children!=None and n>0:
			__findWords(node.children,cadenas,palabra+node.key,n-1)
	return

def __searchP(nl:List[TrieNode],pat:str,n):
	nodo=__searchInList(nl,pat)
	if nodo!=None:
		if len(pat)>1:
			if nodo.children!=None:
				return __searchP(nodo.children,pat[1:],n-1)
			else:
				return None
		elif nodo.children!=None:
			words=[]
			__findWords(nodo.children,words,"",n-1)
			return words
		else:
			return None
	else:
		return None

def searchP(T:Trie,pat:str,n:int):
    if T.root!=None:
        palabras=__searchP(T.root,pat,n-1)
        return [pat+w for w in palabras]
    else:
	    return None

B=Trie()
insert(B,"casa")
insert(B,"caserio")
insert(B,"casamiento")
insert(B,"casorio")
insert(B,"manzana")

print(showTrieContent(B))
print(searchP(B,"cas",7))