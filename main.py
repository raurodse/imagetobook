#!/usr/bin/env python
import sys
import os
import argparse
'''Inch = 25.4
cantidad , unidades = sys.argv[1].split(" ")

if ( unidades == "PixelsPerInch"):
  print ((float(cantidad) / Inch)*210)
else:
  print ((float(cantidad) / 10)*210)
'''
'''a = (os.listdir(sys.argv[1]))
paginas = int(sys.argv[2]) * 4
a.sort()
contador = int(len(a) / paginas)
print(contador)
for i in range(0,contador+1):
	lista = []
	minimo = (i * paginas)
	maximo = minimo + paginas
	if maximo > len(a):
		maximo = len(a)
	miniarray = a[minimo:maximo]
	if len(miniarray) != paginas:
		for aux in range(0,paginas-len(miniarray)):
			miniarray.append("")
	mitad = int(paginas / 2 )
	for indice in range(0,mitad):
		if indice % 2 == 0:
			lista.append(miniarray[len(miniarray) - indice - 1])
			lista.append(miniarray[indice])
		else:
			lista.append(miniarray[indice])
			lista.append(miniarray[len(miniarray) - indice - 1])
	print (lista)
'''	
parser = argparse.ArgumentParser(prog="imagetobook",description="This a tool for convert images in book for print")
parser.add_argument('--orientation',nargs=1,help="Orientation for read book",choices=('oriental','occidental'),default="occidental",required=True)
parser.add_argument('--dimension',nargs=1,help="Dimensions of paper",default="a4")
args = parser.parse_args()