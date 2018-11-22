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

list = []

#Creating file, reading, writing, listing and deleting elements of the file
#for creater(), reader() and writer(val) just reading python doc https://docs.python.org/3.6/library/csv.html#csv.reader
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
def delete(): #soluce https://stackoverflow.com/a/45294821
  with open('list.csv', 'r+') as h:
    csv_rM = h.readlines()
    h.seek(0)
    for row in csv_rM:
      h.truncate()


#Operations of values in the file
#How I convert my list to int :
#-s
def max():
  maxVal_list = 
  reader()
  max_val = max(maxVal_list)

def min():
  minVal_list = 
  reader()
  min_val = min(minVal_list)  

def average():
  aveVal_list = 
  reader()
  ave_val = sum(aveVal_list) / len(aveVal_list)

def sum():
  sumVal_list = 
  reader()
  sum_val = sum(sumVal_list)


#sorting the values in the file
#-t
def asc():
  asc_list = 
  reader()
  asc_list.sort()
  writer(asc_list)

#-d
def desc():
  desc_list = 
  reader()
  desc_list.sort(reverse = True)
  writer(desc_list)


#args parsing
parser = argparse.ArgumentParser(description='Simple operations on a list of int stored in a csv file')
parser.add_argument('-l', action='store_true', help='show the list')
parser.add_argument('-a', nargs='+',help='add elements in the list')
parser.add_argument('-c', action='store_true', help='delete all elements of the list')
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
  print ('The file is created, open ./list.csv')
  reader()
  for n in args.a:
    addCsv(n)
    writer(list)
  print('Elements in the file are created')
elif args.l:
  showList()
  print(list)
elif args.c:
  delete()
  print('Elements in the file are deleted')

#convert list to str
elif args.s:
  max()
  print('The maximum value of the list is : ' + max_val)
  if args.max:
    max()
    print('The maximum value of the list is : ' + max_val)
  elif args.min:
    print('The minimum value of the list is : ' + min_val)
  elif args.moy:
    print('The average value of the list is : ' + ave_val)
  elif args.sum:
    print('The sum of values of the list is : ' + sum_val)

elif args.t:
  asc()
  print ('Elements in the file are sorted in ASC')
elif args.desc:
  desc()
  print ('Elements in the file are sorted in DESC')