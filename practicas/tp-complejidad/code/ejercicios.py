"""
Ejercicio 4
Primero ordeno la lista con alguno de los métodos, aquí uso el método sort() para simplicidad.
Una vez ordenado calculo 2 indices necesarios, el del medio de la lista, y el del cuarto de la lista, ya que
del lado izquierdo tienen que quedar la mitad de los menores al de la mitad.
Luego lo que hago es simplemente intercambiar los elementos que están entre la mitad y el cuarto con la misma
cantidad de elementos del lado derecho.
"""

def ordenarMitad(A:list):
	Asorted=[]
	Asorted=A.copy()
	Asorted.sort()
	mid=round((len(Asorted)-1)/2)
	quad=round((mid)/2)
	for i in range(1,mid-quad+1):
		Asorted[mid-i], Asorted[mid+i] = Asorted[mid+i], Asorted[mid-i]
	return Asorted


"""
Ejercicio 5
Primero se ordena la lista, se puede hacer con cualquier método visto, aquí use el método sort()
por simplicidad del código. Por lo que la elección del método de ordenamiento tendrá impacto en el
orden de complejidad total.
Una vez ordenada la lista, me fijo si la suma de los elementos de los extremos son iguales al numero solicitado
Si es mayor, me muevo una posición hacia la izquierda del lado mayor, asi la suma siguiente tendría que ser menor
Si es menor, me muevo una posición hacia la derecha del lado menor, asi la suma siguiente tendría que ser mayor
Hasta llegar a que ambas posiciones son la misma y si se llega a ese punto es que no existe un par que de la suma.
"""
def ContieneSuma(A:list,n:int):
	Asorted=[]
	Asorted=A.copy()
	Asorted.sort()
	i=0
	d=len(Asorted)-1
	HS=False
	while i!=d:
		suma=Asorted[i]+Asorted[d]
		if suma==n:
			HS=True
			break
		elif suma<n:
			i+=1
		else:
			d-=1

	return HS


listaSinOrdenar=[5,8,3,6,9,20,-3,25,71]
resp=ContieneSuma(listaSinOrdenar,12)
print(resp)
print(ordenarMitad(listaSinOrdenar))