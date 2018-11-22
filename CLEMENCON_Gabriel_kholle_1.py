#!/usr/bin/python3.6
###
# CLEMENCON_Gabriel_kholle_1.py
# Ce programme fait de simples opérations sur une liste de nombres stocker dans un .csv
# This soft make simple operations on a list of int stored in a .csv
# 20/11/2018
# Gabriel Clémençon
###

import argparse
import csv

#args parsing
parser = argparse.ArgumentParser(description='Simple operations on a list of int stored in a csv file')
parser.add_argument('-l', action=, help='show the list')#todo
parser.add_argument('-a', action=, nargs='+', type=int, help='add elements in the list')#todo
parser.add_argument('-c', action=, help='delete all elements of the list')#todo
parser.add_argument('-s', action=, help='show the max/min/average or sum of the list') #todo
parser.add_argument ('--max', action=, help='show the max value of the list')#todo
parser.add_argument ('--min', action=, help='show the min value of the list')#todo
parser.add_argument ('--moy', action=, help='show the average of the list')#todo
parser.add_argument ('--sum', action=, help='show the sum of the list')#todo
parser.add_argument('-t', action=, help='show the list in ASC order') #todo
parser.add_argument('-d', '--desc', action=, help='show the list in DESC order') #todo
args = parser.parse_args()


#exec the method from the right args
if args.a:
  print('elements created')
elif args.l:
  print('l')
elif args.c:
  print('c')
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
  print('t')
elif args.desc:
  print('desc')