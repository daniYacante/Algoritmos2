from typing import List
class Trie:
	root=None

class TrieNode:
	parent=None
	children=None
	key=None
	isEndOfWord=False


def __insert(lista:list,element:str):
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
insert(A,"hola")