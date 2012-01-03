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
def get_order(orientation,pages,list_files):
    list_files.sort()
    ordered_list = {"blank":0,"order":[]}
    order = 1
    if orientation == "oriental":
        order = 0
    counter = int(len(list_files) / pages)
    for i in range(0,counter + 1):
        min_index = ( i * pages )
        max_index = (min_index + pages)
        if max_index > len(list_files):
            max_index = len(list_files)
        part_of_list = list_files[min_index:max_index]
        if len(part_of_list) != pages:
            for aux in range(0,pages-len(part_of_list)):
                part_of_list.append("")
                ordered_list["blank"] += 1
        middle = int(pages / 2)
        for j in range(0,middle):
            if j % 2 == order:
                ordered_list["order"].append(part_of_list[pages - j - 1])
                ordered_list["order"].append(part_of_list[j])
            else:
                ordered_list["order"].append(part_of_list[j])
                ordered_list["order"].append(part_of_list[pages - j - 1])
    return ordered_list

def main():
    parser = argparse.ArgumentParser(prog="imagetobook",description="This a tool for convert images in book for print")
    parser.add_argument('--orientation',nargs=1,help="Orientation for read book",choices=('oriental','occidental'),required=True)
    parser.add_argument('--dimension',nargs=1,help="Dimensions of paper",default="a4")
    parser.add_argument('--pages',metavar="N",help="number of pages per book",required=True)
    parser.add_argument('--quality',nargs=1,help="Quality of output document",default="300")
    parser.add_argument('action',nargs=1,help="Select action to do",choices={"test","convert"})
    parser.add_argument('path',nargs=1,help="Files path to convert")
    args = parser.parse_args()
    
    if args.action[0] == "test":
        order_list_files = get_order(args.orientation[0],int(args.pages),os.listdir(args.path[0]))
        print ("\nRESUME\n*********")
        print ("Blank pages : " + str(order_list_files['blank']))
        print ("\nOrder list :")
        print ("*************")
        print(" ".join(order_list_files['order']))
    elif args.action[0] == "convert":
        order_list_files = get_order(args.orientation[0],int(args.pages),os.listdir(args.path[0]))
        



if __name__ == '__main__':
    main()



