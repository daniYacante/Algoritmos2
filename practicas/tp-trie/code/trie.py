from typing import List
class Trie:
	root=None

class TrieNode:
	parent=None
	children=None
	key=None
	isEndOfWord=False

def __showTrie(nl:List[TrieNode],cadenas:list,palabra:str):
	for node in nl:
		if node.isEndOfWord:
			cadenas.append(palabra+node.key)
		if node.children!=None:
			__showTrie(node.children,cadenas,palabra+node.key)
	return
def showTrieContent(T:Trie):
	if T.root!=None:
		content=[]
		__showTrie(T.root,content,"")
		return content
	else:
		return None

def __insert(lista:list,element:str):
	nodo=__searchInList(lista,element)
	if nodo!=None:
		if len(element)>1:
			if nodo.children==None:
				nodo.children=[]
			__insert(nodo.children,element[1:])
		else:
			nodo.isEndOfWord=True
	else:
		newNode=TrieNode()
		newNode.key=element[0]
		if len(element)!=1:
			newNode.children=[]
			__insert(newNode.children,element[1:])
		else:
			newNode.isEndOfWord=True
		lista.append(newNode)
		return

def __searchInList(lista:List[TrieNode],element:str):
	for nodo in lista:
		if nodo.key==element[0]:
			return nodo
	return None

def insert(T:Trie,element:str):
	if T.root==None:
		T.root=[]
	__insert(T.root,element)
	return

def search(T:Trie,element:str):
	return

def delete(T:Trie,element:str):
	return

A=Trie()
insert(A,"holo")
insert(A,"hola")
insert(A,"holanda")
insert(A,"hipopotamo")
insert(A,"pez")
print(showTrieContent(A))