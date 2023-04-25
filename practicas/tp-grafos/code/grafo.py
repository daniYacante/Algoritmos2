from random import randint
class grafo():
	def fhash(self,key,i):
		m=self.m
		h1=lambda key: key
		h2=lambda key: 1+(key%(m-1))
		return (h1(key)+i*h2(key))%m

	def __init__(self,nVertices:list) -> None:
		self.nodos=[None for n in nVertices]
		self.m=len(nVertices)
		self.vistos=[]
		for v in nVertices:
			IN=False
			for i in range(self.m):
				pos=self.fhash(v,i)
				if self.nodos[pos]==None:
					self.nodos[pos]=grafNodo(v)
					IN=True
					break
			if not IN:
				print(f"Vértice {v} sin insertar")
	
	def __str__(self) -> str:
		cad=""
		for n in self.nodos:
			cad+=str(n.value)+"->"
			if n.vecinos!=None:
				cad+=", ".join(str(vec) for vec in n.vecinos)
			cad+="\n"
		return cad
	def _getPos(self,key):
		enc=False
		for i in range(self.m):
			pos=self.fhash(key,i)
			if self.nodos[pos].value==key:
				enc=True
				break
		if not enc:
			# print(f"Vértice {x} no encontrado")
			return None
		else:
			return pos
	def addArista(self,arista:tuple):
		x,y=arista
		posx=self._getPos(x)
		posy=self._getPos(y)
		if posx!=None:
			if self.nodos[posx].vecinos != None:
				self.nodos[posx].vecinos.append(y)
			else:
				self.nodos[posx].vecinos=[y]
		if posy!=None:
			if self.nodos[posy].vecinos != None:
				self.nodos[posy].vecinos.append(x)
			else:
				self.nodos[posy].vecinos=[x]
		


class grafNodo():
	def __init__(self,value) -> None:
		self.value=value
		self.vecinos=None
		self.visto=None

def createGraph(vertices, aristas):
	graph=grafo(vertices)
	for ar in aristas:
		graph.addArista(ar)
	return graph

def existPath(grafo:grafo,v1, v2):
	posV1=grafo._getPos(v1)
	if posV1!=None and not (grafo.nodos[posV1].value in grafo.vistos):
		vec=grafo.nodos[posV1].vecinos
		grafo.vistos.append(grafo.nodos[posV1].value)
		if vec!=None:
			for v in vec:
				if v==v2:
					grafo.vistos.clear()
					return True
			for v in vec:
				resp=existPath(grafo,v,v2)
				if resp:
					return resp
		return False
def isConnected(grafo:grafo):
	nodos=grafo.nodos
	for i in range(len(nodos)):
		for j in range(len(nodos)):
			if i!=j:
				if not existPath(grafo,grafo.nodos[i].value,grafo.nodos[j].value):
					grafo.vistos.clear()
					return False
	return True

def detectCycles(grafo:grafo,v,va):
	pos=grafo._getPos(v)
	if pos!=None:
		if not (grafo.nodos[pos].value in grafo.vistos):
			vec=grafo.nodos[pos].vecinos
			grafo.vistos.append(grafo.nodos[pos].value)
			if vec!=None:
				for vn in vec:
					if vn!=va:
						resp=detectCycles(grafo,vn,v)
						if resp!=None:
							grafo.vistos.clear()
							return resp
				return False
			else:
				return None
		else:
			return True
def isTree(grafo:grafo):
	return not detectCycles(grafo,grafo.nodos[randint(1,len(grafo.nodos))].value,None) and isConnected(grafo)
		
grafo=createGraph([1,2,3,4,5,6,7],[(1,2),(1,3),(2,3),(2,4),(5,4),(6,4),(6,7)])
print(existPath(grafo,5,7))
print(grafo)

print("Esta conectado?: ",isConnected(grafo))
print("Hay ciclos? : ", detectCycles(grafo,4,None))
print("Es Arbol? : ",isTree(grafo))