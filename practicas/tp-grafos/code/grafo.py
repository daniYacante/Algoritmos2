class grafo():
	def fhash(self,key,i):
		m=self.m
		h1=lambda key: key
		h2=lambda key: 1+(key%(m-1))
		return (h1(key)+i*h2(key))%m

	def __init__(self,nVertices:list) -> None:
		self.nodos=[None for n in nVertices]
		self.m=len(nVertices)
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

	def addArista(self,arista:tuple):
		x,y=arista
		xEn=False
		yEn=False
		for i in range(self.m):
			posx=self.fhash(x,i)
			if self.nodos[posx].value==x:
				xEn=True
				break
		for j in range(self.m):
			posy=self.fhash(y,j)
			if self.nodos[posy].value==y:
				yEn=True
				break
		if not xEn:
			print(f"Vértice {x} no encontrado")
		else:
			if self.nodos[posx].vecinos != None:
				self.nodos[posx].vecinos.append(y)
			else:
				self.nodos[posx].vecinos=[y]
		if not yEn:
			print(f"Vértice {y} no encontrado")
		else:
			if self.nodos[posy].vecinos != None:
				self.nodos[posy].vecinos.append(x)
			else:
				self.nodos[posy].vecinos=[x]
		


class grafNodo():
	def __init__(self,value) -> None:
		self.value=value
		self.vecinos=None

def createGraph(vertices, aristas):
	graph=grafo(vertices)
	for ar in aristas:
		graph.addArista(ar)
	print(graph)



createGraph([1,2,5,3,8,7],[(1,2),(5,3),(5,8)])