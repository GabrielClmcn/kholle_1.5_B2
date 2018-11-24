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
from statistics import mean

list = []


#-- methods --#
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
      for i in range(len(row)):
        list.append(row[i])

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
#How I convert my list to int : https://stackoverflow.com/a/7368914
#-s
def maxlist():
  reader()
  maxVal_list = [int(i) for i in list]
  return str(max(maxVal_list))

def minlist():
  reader()
  minVal_list = [int(i) for i in list]
  return str(min(minVal_list))  

def average():
  reader()
  aveVal_list = [int(i) for i in list]
  return str(mean(aveVal_list))

def somme():
  sumVal_list = [int(i) for i in list]
  reader()
  return str(sum(sumVal_list))


#sorting the values in the file
#-t
def asc():
  reader()
  asc_list = [int(i) for i in list]
  asc_list.sort()
  writer(asc_list)

#-d
def desc():
  reader()
  desc_list = [int(i) for i in list]
  desc_list.sort(reverse = True)
  writer(desc_list)


#args parsing
#just reading python doc https://docs.python.org/3.6/library/argparse.html#creating-a-parser
parser = argparse.ArgumentParser(description='Simple operations on a list of int stored in a csv file')
parser.add_argument('-l', action='store_true', help='show the list')
parser.add_argument('-a', nargs='+',help='add elements in the list')
parser.add_argument('-c', action='store_true', help='delete all elements of the list')
parser.add_argument('-t', action='store_true', help='show the list in ASC order')
parser.add_argument('-d', '--desc', action='store_true', help='show the list in DESC order')
subparsers = parser.add_argument_group(title='subcommands', description='commands who need the -s argument')
subparsers.add_argument('-s', action='store_true', help='do nothing')
subparsers.add_argument('--max', action='store_true', help='show the max value of the list')
subparsers.add_argument('--min', action='store_true', help='show the min value of the list')
subparsers.add_argument('--moy', action='store_true', help='show the average of the list')
subparsers.add_argument('--sum', action='store_true', help='show the sum of the list')
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
elif args.s:
  if args.max:
    maxlist()
    print('The maximum value of the list is : ' + maxlist())
  elif args.min:
    minlist()
    print('The minimum value of the list is : ' + minlist())
  elif args.moy:
    average()
    print('The average value of the list is : ' + average())
  elif args.sum:
    somme()
    print('The sum of values of the list is : ' + somme())
elif args.t:
  asc()
  print ('Elements in the file are sorted in ASC')
elif args.desc:
  desc()
  print ('Elements in the file are sorted in DESC')