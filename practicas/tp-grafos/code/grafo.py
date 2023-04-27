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
		self.noVistos=[]
		self.aristas=0
		self.componentes=0
		for v in nVertices:
			IN=False
			for i in range(self.m):
				pos=self.fhash(v,i)
				if self.nodos[pos]==None:
					self.nodos[pos]=grafNodo(v)
					self.noVistos.append(v)
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
	def getNumAristas(self):
		return self.aristas
	def getNumNodos(self):
		return self.m
	def addArista(self,arista:tuple):
		x,y=arista
		posx=self._getPos(x)
		posy=self._getPos(y)
		if posx!=None and posy!=None:
			self.aristas+=1
			if self.nodos[posx].vecinos != None:
				self.nodos[posx].vecinos.append(y)
			else:
				self.nodos[posx].vecinos=[y]
			if self.nodos[posy].vecinos != None:
				self.nodos[posy].vecinos.append(x)
			else:
				self.nodos[posy].vecinos=[x]
			return True
		else:
			return False
		


class grafNodo():
	def __init__(self,value) -> None:
		self.value=value
		self.vecinos=None

def createGraph(vertices:list, aristas:list):
	graph=grafo(vertices)
	for ar in aristas:
		if not graph.addArista(ar):
			print(f"Arista {ar} no valida")
	return graph

def existPath(graf:grafo,v1, v2):
	posV1=graf._getPos(v1)
	if posV1!=None and not (graf.nodos[posV1].value in graf.vistos):
		vec=graf.nodos[posV1].vecinos
		graf.vistos.append(graf.nodos[posV1].value)
		if vec!=None:
			for v in vec:
				if v==v2:
					graf.vistos.clear()
					return True
			for v in vec:
				resp=existPath(graf,v,v2)
				if resp:
					return resp
		return False
def isConnected(graf:grafo):
	nodos=graf.nodos
	for i in range(len(nodos)):
		for j in range(len(nodos)):
			if i!=j:
				if not existPath(graf,graf.nodos[i].value,graf.nodos[j].value):
					graf.vistos.clear()
					return False
	return True

def _cycles(graf:grafo,v,va,ciclos:set):
	pos=graf._getPos(v)
	if pos!=None:
		if not (graf.nodos[pos].value in graf.vistos):
			vec=graf.nodos[pos].vecinos
			graf.vistos.append(graf.nodos[pos].value)
			graf.noVistos.remove(graf.nodos[pos].value)
			if vec!=None:
				for vn in vec:
					if vn!=va:
						resp=_cycles(graf,vn,v,ciclos)
						if resp:
							# ciclos.append((v,vn))
							ciclos.add(tuple(sorted((vn,v))))
				return False
		else:
			return True

def detectCycles(graf:grafo):
	nodes=graf.noVistos.copy()
	loop=set()
	cont=0
	while graf.getNumNodos()>len(graf.vistos):
		posi=graf._getPos(graf.noVistos[randint(0,len(graf.noVistos)-1)])
		_cycles(graf,graf.nodos[posi].value,None,loop)
		cont+=1
	graf.componentes=cont
	graf.vistos.clear()
	graf.noVistos=nodes.copy()
	return loop
	
def isTree(graf:grafo):
	return len(detectCycles(graf))>0 and isConnected(graf) and (graf.getNumAristas()==graf.getNumNodos()-1)

def isComplete(graf:grafo):
	nNodes=len(graf.nodos)
	complete=False
	for nodo in graf.nodos:
		vecinos=nodo.vecinos
		if len(vecinos)==(nNodes-1) and not (nodo.value in vecinos):
			complete= True
		else:
			complete=False
	return complete
def convertTree(graf:grafo):
	return detectCycles(graf)
def countConnections(graf:grafo):
	if graf.componentes==0:
		detectCycles(graf)	
	return graf.componentes
grafo1=createGraph([1,2,3,4,5,6,7],[(1,2),(1,3),(2,3),(5,4),(6,7)])
print(existPath(grafo1,5,7))
print(grafo1)

print("Esta conectado?: ",isConnected(grafo1))
print("Hay ciclos? : ", detectCycles(grafo1))
print("Hay componentes conexas: ",grafo1.componentes)
print(grafo1.getNumAristas())
print("Es Arbol? : ",isTree(grafo1))
print("Esta completo? : ",isComplete(grafo1))

grafoCompleto=createGraph([1,2,3,4],[(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)])
print(grafoCompleto)
print(grafoCompleto.getNumAristas())
print("Esta completo? : ",isComplete(grafoCompleto))