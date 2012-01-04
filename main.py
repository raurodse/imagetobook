#!/usr/bin/env python
import sys
import os
import argparse
import re
import subprocess

#
# Global vars
#
Inch = 25.4

#Function to get correct order to print pages
#Return Dict {
#                     blank: num of blank pages
#                     order: order pages to print
#                   }
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

#def get_order

def test(args):
    order_list_files = get_order(args.orientation[0],int(args.pages),os.listdir(args.path[0]))
    print ("\nRESUME\n*********")
    print ("Blank pages : " + str(order_list_files['blank']))
    print ("\nOrder list :")
    print ("*************")
    print(" ".join(order_list_files['order']))
#def test

def convert(args):
    order_list_files = get_order(args.orientation[0],int(args.pages),os.listdir(args.path[0]))
    namepaperformat = "format"+ args.dimension[0]
    formatfile = file("/home/kbut/imagetobook/dimensions",'r')
    dimensionsnumbers = ""
    for needle in formatfile.readlines():
        if re.search(namepaperformat,needle):
            aux =  needle.strip("\n").split("=")
            if len(aux) == 2:
                dimensionsnumbers = aux[1]
            else:
                dimensionsnumbers = ""
    if dimensionsnumbers == "":
        print "Dimension not supported"
        exit(1)
    x,y = dimensionsnumbers.split("x")
    xpixel = args.quiality[0] * (x / Inch)
    ypixel = args.quiality[0] * (y / Inch)

#def convert

def convertimage(name,x,y,quality,number):
    subprocess.Popen(["convert","-resize","x"+x,name,"resize"+number+".png"])
    subprocess.Popen(["convert","-density",quality,"resize"+number+".png","density"+number+".png"])
    subprocess.Popen(["convert","-rotate","-90<"+x,"density"+number+".png","rotate"+number+".png"])
    os.remove("resize"+number+".png")
    os.remove("density"+number+".png")
    return "rotate" + number+".png"
        
def joinimages(listnames,outputname):
    command = []
    command.append("convert")
    command.append("-append")
    for filename in listnames:
        command.append(filename)
    command.append(outputname)
    subprocess.Popen(command)
    

    
def main():
    parser = argparse.ArgumentParser(prog="imagetobook",description="This a tool for convert images in book for print")
    parser.add_argument('--orientation',nargs=1,help="Orientation for read book",choices=('oriental','occidental'),required=True)
    parser.add_argument('--dimension',nargs=1,help="Dimensions of paper",default=["a4"])
    parser.add_argument('--pages',metavar="N",help="number of pages per book",required=True)
    parser.add_argument('--quality',nargs=1,help="Quality of output document",default=["300"])
    parser.add_argument('action',nargs=1,help="Select action to do",choices=("test","convert"))
    parser.add_argument('path',nargs=1,help="Files path to convert")
    args = parser.parse_args()
    
    if args.action[0] == "test":
        test(args)
    elif args.action[0] == "convert":
        convert(args)



if __name__ == '__main__':
    main()



