
class AVLTree:
	root=None

class AVLNode:
	parent=None
	leftnode=None
	rightnode=None
	value=None
	key=None
	bf=None
"""
Ambas funciones rotate funcionan de una forma análoga a la otra
Primero se obtienen las referencias a los nodos hijos(derecho o izquierdo)
como asi también las del nodo padre.
Se desvincula el nodo hijo con el cual se va a hacer el intercambio
Vemos si el nuevo nodo raíz tiene un hijo del lado que se hará el intercambio y
de ser asi se lo coloca como hijo del nodo raíz anterior.
Luego se actualizan las referencias correspondientes de parentesco, tanto del nodo padre
como del nodo que hemos movido
"""
def rotateLeft(tree:AVLTree,avlnode:AVLNode):
	nodoActual=avlnode
	hijoDer=nodoActual.rightnode
	padre=nodoActual.parent
	nodoActual.rightnode=None
	if hijoDer.leftnode!=None:
		nodoActual.rightnode=hijoDer.leftnode
	hijoDer.leftnode=nodoActual
	if padre!=None:
		if padre.rightnode==nodoActual:
			padre.rightnode=hijoDer
		else:
			padre.leftnode=hijoDer
	elif tree.root==avlnode:
		tree.root=hijoDer
	hijoDer.parent=nodoActual.parent
	nodoActual.parent=hijoDer
	return tree.root


def rotateRight(tree:AVLTree,avlnode:AVLNode):
	nodoActual=avlnode
	hijoIzq=nodoActual.leftnode
	padre=nodoActual.parent
	nodoActual.leftnode=None
	if hijoIzq.rightnode!=None:
		nodoActual.leftnode=hijoIzq.rightnode
	hijoIzq.rightnode=nodoActual
	if padre!=None:
		if padre.rightnode==nodoActual:
			padre.rightnode=hijoIzq
		else:
			padre.leftnode=hijoIzq
	elif tree.root==avlnode:
		tree.root=hijoIzq
	hijoIzq.parent=nodoActual.parent
	nodoActual.parent=hijoIzq
	return tree.root
"""
La función calculateBalance es un wrapper de la función __calcularAltura que recorre el árbol
desde las hojas hacia la raíz calculando siempre el bf como también retornando el valor mas grande
de las alturas de los hijos de cada nodo, es decir si un nodo tiene a su izquierda una rama de altura 3
y a su derecha una de altura 1, calcula el bf como 3-1=2 y regresa la suma entre 1 y el mayor de 3 y 1...
Es decir retornara 4, el valor de 1 se suma ya que al subir un nivel tenemos una arista mas del árbol.
"""
def calculateBalance(tree:AVLTree):
	__calcularAltura(tree.root)
	return

def __calcularAltura(avlnode:AVLNode):
	if avlnode.leftnode==None and avlnode.rightnode==None:
		avlnode.bf=0
		return 1
	elif avlnode.leftnode==None:
		hd=__calcularAltura(avlnode.rightnode)
		avlnode.bf=0-hd
		return 1+hd
	elif avlnode.rightnode==None:
		hi=__calcularAltura(avlnode.leftnode)
		avlnode.bf=hi-0
		return 1+hi
	else:
		hi=__calcularAltura(avlnode.leftnode)
		hd=__calcularAltura(avlnode.rightnode)
		avlnode.bf=hi-hd
		return 1+max(hd,hi)
	return
"""
La función de reBalance primero manda a actualizar/calcular los bf's del árbol
y mediante la función __recorreInOrder se obtiene una lista con los nodos del árbol
Para cada nodo se comprueba si el bf esta fuera de los limites para que sea un árbol balanceado
Y de ser asi, comprueba que no se tenga un caso especial, de ser asi primero se hace el giro
contrario al que se deberia hacer, y luego el que corresponde
"""
def reBalance(tree:AVLTree):
	nodosArbol=[]
	calculateBalance(tree)
	__recorreInOrder(tree.root,nodosArbol)
	for nodo in nodosArbol:
		if nodo.bf<-1:
			if nodo.rightnode.bf>0:
				rotateRight(tree,nodo.rightnode)
			rotateLeft(tree,nodo)
		elif nodo.bf>1:
			if nodo.leftnode.bf<0:
				rotateLeft(tree,nodo.leftnode)
			rotateRight(tree,nodo)
	calculateBalance(tree)
	return tree

def __recorreInOrder(avlnode:AVLNode,l:list):
	if avlnode.leftnode!=None:								#para hacer el recorrido InOrder primero trato de llegar
		__recorreInOrder(avlnode.leftnode,l)				#al ultimo nodo a la izq, luego se agrega el nodo en el que se esta
	l.append(avlnode)										#y trata de ir hacia la derecha
	if avlnode.rightnode!=None:
		__recorreInOrder(avlnode.rightnode,l)
	return

def traverseInOrder(tree:AVLTree) :
	listaInOrder=[]											#Creamos la lista a regresar con los nodos ordenados
	if tree.root!=None:										#si el árbol no esta vacío llamamos a la función recursiva
		__recorreInOrder(tree.root,listaInOrder)			#doy vuelta el sentido de los nodos, ya que el que se agrega primero
		for i in range(len(listaInOrder)):					#es el ultimo en la lista
			listaInOrder[i]=listaInOrder[i].value
		return listaInOrder
	else:
		return None

def __recorrePostOrder(avlnode:AVLNode,l:list):
	if avlnode.leftnode!=None:								#Para recorrer en PostOrder, primero tratamos de llegar a las hojas de un nodo
		__recorrePostOrder(avlnode.leftnode,l)				#Se agregan las hojas, y luego el nodo padre.
	if avlnode.rightnode!=None:
		__recorrePostOrder(avlnode.rightnode,l)
	l.append(avlnode)
	return

def traverseInPostOrder(tree:AVLTree):
	listaPostOrder=[]										#Creamos la lista a regresar con los nodos ordenados
	if tree.root!=None:										#si el árbol no esta vacío llamamos a la función recursiva
		__recorrePostOrder(tree.root,listaPostOrder)		#doy vuelta el sentido de los nodos, ya que el que se agrega primero
		for i in range(len(listaPostOrder)):				#es el ultimo en la lista
			listaPostOrder[i]=listaPostOrder[i].value
		return listaPostOrder
	else:
		return None

def __recorrePreOrder(avlnode:AVLNode,l:list):
	l.append(avlnode)										#Para recorrer en preorder, primero agregamos el nodo en el que estamos
	if avlnode.leftnode!=None:								#y luego pasamos a sus hojas
		__recorrePreOrder(avlnode.leftnode,l)
	if avlnode.rightnode!=None:
		__recorrePreOrder(avlnode.rightnode,l)
	return

def traverseInPreOrder(tree:AVLTree):
	listaPreOrder=[]										#Creamos la lista a regresar con los nodos ordenados
	if tree.root!=None:										#si el árbol no esta vacío llamamos a la función recursiva
		__recorrePreOrder(tree.root,listaPreOrder)			#doy vuelta el sentido de los nodos, ya que el que se agrega primero
		for i in range(len(listaPreOrder)):					#es el ultimo en la lista
			listaPreOrder[i]=listaPreOrder[i].value
		return listaPreOrder
	else:
		return None

def __recorreSearch(avlnode:AVLNode, elem):
	if avlnode.value==elem:									#evaluamos el valor del nodo en el que estamos, con el elemento a
		return avlnode.key									#encontrar, esto seria nuestro caso base.
	else:													#si no es el nodo, se crea una variable en la cual se almacenara 
		resp=None											#el valor de key si se encuentra el nodo o en caso contrario
		if avlnode.leftnode!=None:							#se quedara con none.
			resp=__recorreSearch(avlnode.leftnode,elem)		#si el nodo tiene nodos hijo, se llama a la función recursiva 
		if resp!=None:										#si el nodo se ha encontrado, no se sigue buscando y regresa el valor de resp
			return resp										#si no se ha encontrado, se busca por la otra rama.
		if avlnode.rightnode!=None:							#Y tanto si lo encuentra como si no, va a regresar el valor de resp
			resp=__recorreSearch(avlnode.rightnode,elem)
		return resp
			
def search(tree:AVLTree,elem):
	if tree.root!=None:										#si el árbol no esta vacío llamamos a la función recursiva
		return __recorreSearch(tree.root,elem)
	else:
		return None

def __recorreInsert(avlnode:AVLNode,nod:AVLNode):
	if nod.key==avlnode.key:								#Al insertar un nodo primero verificamos que no haya key's duplicadas
		return None
	elif nod.key<avlnode.key:								#si la key del nodo a insertar es menor a la del nodo actual
		if avlnode.leftnode==None:							#y el nodo actual no tiene elemento en su rama izquierda
			nod.parent=avlnode								#se inserta el nodo a la izquierda
			avlnode.leftnode=nod
			return nod.key
		else:												#sino, se llama de forma recursiva a la propia función, 
			return __recorreInsert(avlnode.leftnode,nod)	#con el nodo de la izq
	else:
		if avlnode.rightnode==None:							#si la key, no es ni igual ni menor, solo queda que es mayor, y se
			nod.parent=avlnode								#procede de forma similar al caso anterior.
			avlnode.rightnode=nod
			return nod.key
		else:
			return __recorreInsert(avlnode.rightnode,nod)

def insert(tree:AVLTree,elem, key):
	nodo=AVLNode()											#creo el nodo a insertar con su respectivo key y value
	nodo.value=elem
	nodo.key=key
	if tree.root==None:										#si el árbol esta vacío, el elemento a insertar queda como raíz del árbol
		tree.root=nodo										#sino, se llama a la función recursiva.
		return nodo.key
	else:
		res=__recorreInsert(tree.root,nodo)
		if res!=None:
			reBalance(tree)
		return res

def __recorreDelete(avlnode:AVLNode, elem):
	if avlnode.value==elem:											#Una vez que encuentro el nodo que tiene al elemento que busco eliminar
		if avlnode.leftnode==None and avlnode.rightnode==None:		#debo verificar 4 posibles casos, que el nodo no tenga nodos hijos, tenga
			if avlnode.parent.leftnode.value==elem:					#un solo hijo a la izq, que tenga un solo hijo a la der, o que tenga 
				avlnode.parent.leftnode=None						#nodos hijos a ambos lados
			else:													#Para los primeros 3 casos, corroboro a que lado del nodo padre se encuentra
				avlnode.parent.rightnode=None						#el nodo a eliminar y procedo a actualizar los vínculos
		elif avlnode.leftnode==None and avlnode.rightnode!=None:
			if avlnode.parent.leftnode.value==elem:
				avlnode.parent.leftnode=avlnode.rightnode
			else:
				avlnode.parent.rightnode=avlnode.rightnode
			avlnode.rightnode.parent=avlnode.parent
		elif avlnode.rightnode==None:
			if avlnode.parent.leftnode.value==elem:
				avlnode.parent.leftnode=avlnode.leftnode
			else:
				avlnode.parent.rightnode=avlnode.leftnode
			avlnode.leftnode.parent=avlnode.parent
		elif avlnode.leftnode!=None and avlnode.rightnode!=None:	#Para el caso de que el nodo a eliminar tenga hijos a ambos lados
			nodoAct=AVLNode()
			nodoTemp=AVLNode()
			nodoAct=avlnode.rightnode								#se buscara el menor de los mayores, asi que me muevo a la derecha
			NHF=True												#y en bucle busco el que sea el ultimo en tener componente a la izq
			while NHF:
				if nodoAct.leftnode==None:
					NHF=False
				else:
					nodoAct=nodoAct.leftnode
			nodoTemp=nodoAct.rightnode								#Se guarda en un nodo temporal la rama derecha del nodo que remplazara
			nodoAct.leftnode=avlnode.leftnode						#Al no existir nada mas chico, se copia la rama izquierda
			if avlnode.rightnode!=nodoAct:							#Se comprueba que el hijo a la derecha no sea el nodo que lo remplazara
				nodoAct.rightnode=avlnode.rightnode					#si no lo es, se copia la rama derecha
			nodoAct.parent.leftnode=None							#se desvincula el nodo del padre
			if nodoAct.leftnode!=None:								#se actualizan las referencias a los padres de las ramas si es que existen
				nodoAct.leftnode.parent=nodoAct
			if nodoAct.rightnode!=None:
				nodoAct.rightnode.parent=nodoAct
			nodoAct.parent=avlnode.parent							#se actualiza la propia referencia al padre
			if avlnode.parent.leftnode.value==elem:					#se ve de que parte es hijo el nodo a eliminar para actualizar referencias
				avlnode.parent.leftnode=nodoAct
			else:
				avlnode.parent.rightnode=nodoAct
			if nodoTemp!=None:										#si existe una rama derecha del nodo que remplazara
				print(nodoAct.value,"|",nodoTemp.value)				#se lo inserta en el árbol nuevamente
				__recorreInsert(nodoAct,nodoTemp)
		return avlnode.key
	else:															#si no es el nodo que se busca, se ve si tiene nodos hijos para seguir la búsqueda
		resp=None
		if avlnode.leftnode!=None:
			resp=__recorreDelete(avlnode.leftnode,elem)
		if resp!=None:
			return resp
		if avlnode.rightnode!=None:
			resp=__recorreDelete(avlnode.rightnode,elem)
		return resp

def delete(tree:AVLTree,elem):
	if tree.root!=None:												#Si el árbol no esta vacío, se llama a la función recursiva con el nodo raíz
		resp= __recorreDelete(tree.root,elem)						#como primer nodo
		if resp!=None:
			reBalance(tree)
		return resp
	else:
		return None

def recorreDelKey(avlnode:AVLNode,key):
	if avlnode.key==key:											#Una vez que encuentro el nodo que tiene la key que busco eliminar
		if avlnode.leftnode==None and avlnode.rightnode==None:		#debo verificar 4 posibles casos, que el nodo no tenga nodos hijos, tenga
			if avlnode.parent.key>key:								#un solo hijo a la izq, que tenga un solo hijo a la der, o que tenga 
				avlnode.parent.leftnode=None						#nodos hijos a ambos lados
			else:													#Para los primeros 3 casos, corroboro a que lado del nodo padre se encuentra
				avlnode.parent.rightnode=None						#el nodo a eliminar y procedo a actualizar los vínculos
		elif avlnode.leftnode==None and avlnode.rightnode!=None:
			if avlnode.parent.key>key:
				avlnode.parent.leftnode=avlnode.rightnode
			else:
				avlnode.parent.rightnode=avlnode.rightnode
			avlnode.rightnode.parent=avlnode.parent
		elif avlnode.rightnode==None:
			if avlnode.parent.key>key:
				avlnode.parent.leftnode=avlnode.leftnode
			else:
				avlnode.parent.rightnode=avlnode.leftnode
			avlnode.leftnode.parent=avlnode.parent
		elif avlnode.leftnode!=None and avlnode.rightnode!=None:	 #Para el caso de que el nodo a eliminar tenga hijos a ambos lados
			nodoAct=AVLNode()
			nodoTemp=AVLNode()
			nodoAct=avlnode.rightnode								#se buscara el menor de los mayores, asi que me muevo a la derecha
			NHF=True												#y en bucle busco el que sea el ultimo en tener componente a la izq
			while NHF:
				if nodoAct.leftnode==None:
					NHF=False
				else:
					nodoAct=nodoAct.leftnode
			nodoTemp=nodoAct.rightnode								#Se guarda en un nodo temporal la rama derecha del nodo que remplazara
			nodoAct.leftnode=avlnode.leftnode						#Al no existir nada mas chico, se copia la rama izquierda
			if avlnode.rightnode!=nodoAct:							#Se comprueba que el hijo a la derecha no sea el nodo que lo remplazara
				nodoAct.rightnode=avlnode.rightnode					#si no lo es, se copia la rama derecha
			nodoAct.parent.leftnode=None							#se desvincula el nodo del padre
			if nodoAct.leftnode!=None:								#se actualizan las referencias a los padres de las ramas si es que existen
				nodoAct.leftnode.parent=nodoAct
			if nodoAct.rightnode!=None:
				nodoAct.rightnode.parent=nodoAct
			nodoAct.parent=avlnode.parent							#se actualiza la propia referencia al padre
			if avlnode.parent.leftnode.key==key:					#se ve de que parte es hijo el nodo a eliminar para actualizar referencias
				avlnode.parent.leftnode=nodoAct
			else:
				avlnode.parent.rightnode=nodoAct
			if nodoTemp!=None:										#si existe una rama derecha del nodo que remplazara, 
				__recorreInsert(nodoAct,nodoTemp)					#se lo inserta en el árbol nuevamente
		return avlnode.key
	else:															#si no es el nodo que se busca, se ve si tiene nodos hijos para seguir la búsqueda
		resp=None
		if avlnode.key>key:
			if avlnode.leftnode!=None:
				resp=recorreDelKey(avlnode.leftnode,key)
			else:
				resp=None
		elif avlnode.key<key:
			if avlnode.rightnode!=None:
				resp=recorreDelKey(avlnode.rightnode,key)    
			else:
				resp=None  
		return resp

def deleteKey(tree:AVLTree,key):
	if tree.root!=None:											#Si el árbol no esta vacío, se llama a la función recursiva
		return recorreDelKey(tree.root,key)						#con el nodo raíz como primer nodo
	else:
		return None

def recorreAccess(avlnode:AVLNode,key):
	if avlnode.key==key:										#el caso base es cuando la key del nodo coincide con la key buscada
		return avlnode.value									#y se regresa lo que se encuentre en su campo value
	elif avlnode.key>key:										#si la key a buscar es menor a la key del nodo, paso el hijo de la 
		if avlnode.leftnode!=None:								#izquierda para continuar la búsqueda, si no tiene hijo a la izquierda
			return recorreAccess(avlnode.leftnode,key)			#se regresa none, ya que no hay nodo mas chico
		else:
			return None
	else:														#si la key no es ni igual ni menor, significa que es mayor
		if avlnode.rightnode!=None:								#por lo tanto si existe hijo a la derecha se pasa este a la función recursiva
			return recorreAccess(avlnode.rightnode,key)			#si no hay mas hijos a la derecha, significa que no hay otro mas grande y se 
		else:													#regresa none
			return None

def access(tree:AVLTree,key):
	if tree.root!=None:											#Si el árbol no esta vacío, se llama a la función recursiva
		return recorreAccess(tree.root,key)						#con el nodo raíz como primer nodo
	else:
		return None

def recorreUpdate(avlnode:AVLNode,elem,key):
	if avlnode.key==key:										#como caso base se tiene que la key buscada coincida con la key del nodo
		avlnode.value=elem										#de encontrarse se actualiza su campo value y regresa la key
		return avlnode.key
	elif avlnode.key>key:										#si la key a buscar es menor a la key del nodo, paso el hijo de la
		if avlnode.leftnode!=None:								#izquierda para continuar la búsqueda, si no tiene hijo a la izquierda
			return recorreUpdate(avlnode.leftnode,elem,key)		#se regresa none, ya que no hay nodo mas chico
		else:
			return None
	else:
		if avlnode.rightnode!=None:								#si la key no es ni igual ni menor, significa que es mayor
			return recorreUpdate(avlnode.rightnode,elem,key)	#por lo tanto si existe hijo a la derecha se pasa este a la función recursiva
		else:													#si no hay mas hijos a la derecha, significa que no hay otro mas grande y se
			return None											#regresa none

def update(tree:AVLTree,elem,key):
	if tree.root!=None:
		return recorreUpdate(tree.root,elem,key)
	else:
		return None