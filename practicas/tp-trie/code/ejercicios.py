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

"""
Ejercicio 5
Mi enfoque fue el de llamar a la funcion que regresa todas las palabras en el Trie, hecho esto con ambos Trie, ordeno las listas en orden
alfabetico y comparo las mismas posiciones de las listas, si para la misma posicion tengo palabras distintas, los Trie no son iguales.
El costo seria el O de buscar todas las palabras en ambos Trie, mas el O de ordenarlas mas el O de comparar.
Buscar todas las palabras: O(m|E|)
Ordenar las listas: O(nlogn)
Comparar las listas: O(n)
"""
def sameDoc(T1:Trie,T2:Trie):
	palT1=showTrieContent(T1)
	palT2=showTrieContent(T2)
	palT1.sort()
	palT2.sort()
	if len(palT1)==len(palT2):
		for i in range(len(palT1)):
			if palT1[i]!=palT2[i]:
				return False
		return True
	else:
		return False
	
	return

C=Trie()
insert(C,"casorio")
insert(C,"casa")
insert(C,"manzana")
insert(C,"caserio")
insert(C,"casamiento")
"""
C es igual a B
"""

print(sameDoc(B,C))

D=Trie()
insert(D,"casa")
# insert(D,"caserio")
insert(D,"casamiento")
insert(D,"casorio")
insert(D,"manzana")
"""
D no es igual a B
"""
print(sameDoc(B,D))