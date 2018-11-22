#!/usr/bin/python3.6
############################################################################################################################
#                                                 CLEMENCON_Gabriel_kholle_1.py                                            #
#                     Ce programme fait de simples opérations sur une liste de nombres stocker dans un .csv                #
#                                This soft make simple operations on a list of int stored in a .csv                        #
#                                                         20/11/2018                                                       #
#                                                      Gabriel Clémençon                                                   #
############################################################################################################################

import argparse
import csv
import os

list = []

#Creating file, reading, writing, listing and deleting elements of the file
def creater():
  with open('list.csv', 'w') as e:
    csv.writer(e)
#-a
def reader():
  with open('list.csv', 'r') as f:
    csv_r = csv.reader(f)
    for row in csv_r:
      list.append(row)

def writer(val):
  with open('list.csv', 'w') as g:
    csv_w = csv.writer(g)
    csv_w.writerow(val)
def addCsv(add):
  list.append(add)

#-l
def showList():
  reader()

#-c
def delete():
  with open('list.csv', 'r+') as h:
    csv_rM = h.readlines()
    h.seek(0)
    for row in csv_rM:
      h.truncate()



#Operations of values in the file
#-s
# def max():
  

# def min():
  

# def average():



# def sum():



#sorting the values in the file
#-t
def asc():
  asc_list = a
  reader()
  asc_list.sort()
  writer(asc_list)

#-d
def desc():
  desc_list = a
  reader()
  desc_list.sort(reverse = True)
  writer(desc_list)

#args parsing
parser = argparse.ArgumentParser(description='Simple operations on a list of int stored in a csv file')
parser.add_argument('-l', action='store_true', help='show the list')
parser.add_argument('-a', nargs='+',help='add elements in the list')
parser.add_argument('-c', action='store_true', help='delete all elements of the list')#todo
parser.add_argument('-s', action='store_true', help='show the max/min/average or sum of the list') #todo
parser.add_argument ('--max', action='store_true', help='show the max value of the list') #todo
parser.add_argument ('--min', action='store_true', help='show the min value of the list') #todo
parser.add_argument ('--moy', action='store_true', help='show the average of the list') #todo
parser.add_argument ('--sum', action='store_true', help='show the sum of the list') #todo
parser.add_argument('-t', action='store_true', help='show the list in ASC order')
parser.add_argument('-d', '--desc', action='store_true', help='show the list in DESC order')
args = parser.parse_args()


#execute the method with the associate args
if args.a:
  creater()
  reader()
  for n in args.a:
    addCsv(n)
    writer(list)
  print('Done')
elif args.l:
  showList()
  print(list)
elif args.c:
  delete()
  print('Elements in the file are deleted')

elif args.s:
  if args.max:
    print('max')
  elif args.min:
    print('min')
  elif args.moy:
    print('moy')
  elif args.sum:
    print('sum')

elif args.t:
  asc()
  print ('Done')
elif args.desc:
  desc()
  print ('Done')