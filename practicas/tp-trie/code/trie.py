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

def __searchMatch(nl:List[TrieNode],element:str):
	nodo=__searchInList(nl,element)
	if nodo!=None:
		if len(element)>1:
			if nodo.children!=None:
				return __searchMatch(nodo.children,element[1:])
			else:
				return False
		elif nodo.isEndOfWord:
			return True
		else:
			return False
	else:
		return False

def search(T:Trie,element:str):
	if T.root!=None:
		resp= __searchMatch(T.root,element)
		return resp
	else:
		return False

def __del(nl:List[TrieNode],element:str):
	nodo=__searchInList(nl,element)
	if nodo!=None:
		if len(element)>1:
			if nodo.children!=None:
				resp=__del(nodo.children,element[1:])
				if resp=="del":
					if nodo.isEndOfWord:
						return True
					else:
						nl.remove(nodo)
						return "del"
				else:
					return resp
			else:
				return False
		elif nodo.isEndOfWord:
			if nodo.children!=None:
				nodo.isEndOfWord=False
				return True
			else:
				nl.remove(nodo)
				return "del"
		else:
			return False
	else:
		return False


def delete(T:Trie,element:str):
	if T.root!=None:
		resp=__del(T.root,element)
		if resp=="del":
			return True
		else:
			return resp
	else:
		return False

def __findCommon(nl:List[TrieNode]):
	if len(nl)>1:
		return ""
	elif nl[0].children==None:
		return None
	else:
		resp=__findCommon(nl[0].children)
		if resp!=None:
			resp=nl[0].key+resp
		return resp

def __findPrefix(nl:List[Trie],prefix):
	nodo=__searchInList(nl,prefix)
	if nodo!=None:
		if len(prefix)>1:
			if nodo.children!=None:
				return __findPrefix(nodo.children,prefix[1:])
			else:
				return None
		elif nodo.children!=None:
			return __findCommon(nodo.children)
		else:
			return None
	else:
		return None


def autoCompletar(T:Trie,cadena:str):
	if T.root!=None:
		resp=__findPrefix(T.root,cadena)
		if resp==None:
			return ""
		else:
			return resp
	else:
		return False