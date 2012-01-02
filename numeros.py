#!/usr/bin/env python
import sys
import os
Inch = 25.4
cantidad = sys.argv[1]

print (float(cantidad) * 4)

'''a = (os.listdir(sys.argv[1]))
paginas = int(sys.argv[2])
a.sort()
contador = len(a) / paginas
for i in range(0,contador):
	lista = []
	minimo = (i * paginas)
	maximo = minimo + paginas
	print a[minimo:maximo]
	
'''	
