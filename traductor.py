#!/usr/bin/env python
import sys
import os
#Inch = 25.4
'''cantidad= sys.argv[1]
print (float(cantidad) 4)

'''
fichero = file("/home/kbut/orden",'a')
a = (os.listdir(sys.argv[1]))
paginas = int(sys.argv[2]) * 4
a.sort()
contador = len(a) / paginas
lista = []
for i in range(0,contador+1):
	minimo = (i * paginas)
	maximo = minimo + paginas
	if maximo > len(a):
		maximo = len(a)
	miniarray = a[minimo:maximo]
	if len(miniarray) != paginas:
		for aux in range(0,paginas-len(miniarray)):
			miniarray.append("vacio.png")
	mitad = (paginas / 2 )
	for indice in range(0,mitad):
		if indice % 2 == 0:
			lista.append(miniarray[len(miniarray) - indice - 1])
			lista.append(miniarray[indice])
		else:
			lista.append(miniarray[indice])
			lista.append(miniarray[len(miniarray) - indice - 1])
for elemento in lista:
	fichero.write(elemento+"\n")
	
