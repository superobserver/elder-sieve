#!/usr/local/env python #python 2.7
#Integration leaves residue sequence A195993

import sys
import csv
import time
import subprocess

dump = open("composite1.csv", "w")
new_test = 40000


def dr1_ld1_73_91(x):
  y = 90*(x*x) - 16*x - 1 
  if y > new_test:
    return
  #print "73,91", y
  dump.write(str(y) + "\n")
  for n in range(1, new_test):
    new_y = y+((73+(90*(x-1)))*n)
    new2_y = y+((91+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")


def dr1_ld1_19_37(x):
  y = 90*(x*x) - 124*x + 41 
  if y > new_test:
    return
  dump.write(str(y) + "\n") 
  for n in range (1, new_test):
    new_y = y+ ((19+(90*(x-1)))*n)
    new2_y = y+ ((37+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")


def dr1_ld1_11_23(x):
  y = 90*(x*x) - 146*x + 58
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((11+(90*(x-1)))*n)
    new2_y = y+((23+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")



def dr1_ld1_29_77(x):
  y = 90*(x*x) - 74*x + 8
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((29+(90*(x-1)))*n)
    new2_y = y+((77+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")


def dr1_ld1_47_59(x):
  y = 90*(x*x) - 74*x + 14
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((47+(90*(x-1)))*n)
    new2_y = y+((59+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")


def dr1_ld1_41_83(x):
  y = 90*(x*x) - 56*x + 3
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((41+(90*(x-1)))*n) 
    new2_y = y+((83+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")



def dr1_ld1_13_61(x):
  y = 90*(x*x) - 106*x + 24
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((13+(90*(x-1)))*n)
    new2_y = y+((61+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")


def dr1_ld1_31_43(x):
  y = 90*(x*x) - 106*x + 30
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((31+(90*(x-1)))*n) 
    new2_y = y+((43+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")


def dr1_ld1_7_49(x):
  y = 90*(x*x) - 124*x + 37
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((7+(90*(x-1)))*n)
    new2_y = y+((49+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")



def dr1_ld1_67_79(x):
  y = 90*(x*x) - 34*x + 2
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((67+(90*(x-1)))*n) 
    new2_y = y+((79+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")


def dr1_ld1_17_89(x):
  y = 90*(x*x) - 74*x 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((17+(90*(x-1)))*n)
    new2_y = y+((89+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")

def dr1_ld1_53_71(x):
  y = 90*(x*x) - 56*x + 7
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((53+(90*(x-1)))*n)
    new2_y = y+((71+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")


####################################################
#new 
#79, 339, 779, 1399, 2199, 3179, 4339, 5679, 7199, 8899
def dr7_ld9_79_91(x):
  y = 90*(x*x) - 10*x - 1 
  if y > new_test:
    return
  #print "7w,91", y
  dump.write(str(y) + "\n")
  for n in range(1, new_test):
    new_y = y+((79+(90*(x-1)))*n) 
    new2_y = y+((91+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################

###################################################
#new
#12, 182, 532, 1062, 1772, 2662, 3732, 4982, 6412, 8022, 9812
def dr7_ld9_19_61(x):
  y = 90*(x*x) - 100*x + 22
  if y > new_test:
    return
  dump.write(str(y) + "\n") 
  for n in range (1, new_test):
    new_y = y+((19+(90*(x-1)))*n)
    new2_y = y+((61+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################

###################################################
#2, 136, 450, 944, 1618, 2472, 3506, 4720, 6114, 7688, 9442
#new
def dr7_ld9_7_37(x):
  y = 90*(x*x) - 136*x + 48
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((7+(90*(x-1)))*n)
    new2_y = y+((37+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
##################################################

##################################################
#34, 240, 626, 1192, 1938, 2864, 3970, 5256, 6722, 8368
#new 
def dr7_ld9_43_73(x):
  y = 90*(x*x) - 64*x + 8
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((43+(90*(x-1)))*n)
    new2_y = y+((73+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################	  

###################################################
#10, 200, 570, 1120, 1850, 2760, 3850, 5120, 6570, 8200
#new
def dr7_ld9_11_89(x):
  y = 90*(x*x) - 80*x  
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((11+(90*(x-1)))*n)
    new2_y = y+((89+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
####################################################

####################################################
#22, 212, 582, 1132, 1862, 2772, 3862, 5132, 6582, 8212
#new
def dr7_ld9_29_71(x):
  y = 90*(x*x) - 80*x + 12
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((29+(90*(x-1)))*n) 
    new2_y = y+((71+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
######################################################

######################################################

#8, 162, 496, 1010, 1704, 2578, 3632, 4866, 6280, 7874, 9648
#new
def dr7_ld9_17_47(x):
  y = 90*(x*x) - 116*x + 34
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((17+(90*(x-1)))*n)
    new2_y = y+((47+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
#############################################################

##############################################################

#48, 274, 680, 1266, 2032, 2978, 4104, 5410, 6896, 8562
#new
def dr7_ld9_53_83(x):
  y = 90*(x*x) - 44*x + 2 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((53+(90*(x-1)))*n) 
    new2_y = y+((83+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
############################################################

########################################################
 
#1, 117, 413, 889, 1545, 2381, 3397, 4593, 5969, 7525, 9261
#new
def dr7_ld9_13_13(x):
  y = 90*(x*x) - 154*x + 65 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((13+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")

############################################################

########################################################

#16, 186, 536, 1066, 1776, 2666, 3736, 4986, 6416, 8026, 9816
#new
def dr7_ld9_31_49(x):
  y = 90*(x*x) - 100*x + 26
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((31+(90*(x-1)))*n) 
    new2_y = y+((49+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
########################################################

########################################################
#49, 273, 677, 1261, 2025, 2969, 4093, 5397, 6881, 8545
#new
def dr7_ld9_67_67(x):
  y = 90*(x*x) - 46*x + 5
  if y > new_test:
    return
  #print y, "67,67"
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((67+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")

######################################################

#####################################################

#5, 141, 457, 953, 1629, 2485, 3521, 4737, 6133, 7709, 9465
#new
def dr7_ld9_23_23(x):
  y = 90*(x*x) - 134*x + 49
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((23+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
   
#########################################################

#####################################################

#26, 216, 586, 1136, 1866, 2776, 3866, 5136, 6586, 8216, 10026
#new
def dr7_ld9_41_59(x):
  y = 90*(x*x) - 80*x + 16
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((41+(90*(x-1)))*n)
    new2_y = y+((59+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
   
#########################################################

#####################################################

#65, 309, 733, 1337, 2121, 3085, 4229, 5553, 7057, 8741
#new
def dr7_ld9_77_77(x):
  y = 90*(x*x) - 26*x + 1
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((77+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
   
#########################################################


for x in xrange(1, 202): 
    dr1_ld1_11_23(x) #2
    dr1_ld1_7_49(x)  #3
    dr1_ld1_19_37(x) #7
    dr1_ld1_13_61(x) #8
    dr1_ld1_31_43(x) #14 
    dr1_ld1_17_89(x) #16 
    dr1_ld1_29_77(x) #24
    dr1_ld1_47_59(x) #30 
    dr1_ld1_41_83(x) #37 
    dr1_ld1_53_71(x) #41 
    dr1_ld1_67_79(x) #58 
    dr1_ld1_73_91(x) #73

 
    dr7_ld9_79_91(x)#  
    dr7_ld9_19_61(x)# 
    dr7_ld9_7_37(x)# 
    dr7_ld9_43_73(x)# 
    dr7_ld9_11_89(x)# 
    dr7_ld9_29_71(x)# 
    dr7_ld9_17_47(x)# 
    dr7_ld9_53_83(x)# 
    dr7_ld9_13_13(x)# 
    dr7_ld9_31_49(x)# 
    dr7_ld9_67_67(x)# 
    dr7_ld9_23_23(x)# 
    dr7_ld9_41_59(x)#
    dr7_ld9_77_77(x)#

def bash_command(cmd):
    subprocess.Popen(cmd, shell=True)
bash_command('sort -n composite1.csv -o composite2.csv')
time.sleep(1.2) #make sure subprocess has finished

z=200
f=open("composite2.csv")
for i in range(z):
  line=f.next().strip()
  print line
  #print "not prime", line
f.close()

proceed = raw_input("shall we proceed to print the next 10,000 primes?")
if proceed == "yes":
  pass
if proceed == "no":
  execfile("ElderSieve.py")
  quit("goodbye")

#run this code to compare to https://oeis.org/A181732/b181732.txt
with open("composite2.csv") as f:
    rd=f.readlines()
    x=[t.strip("\n") for t in rd]
    for i in range(0, 37188):
        if str(i) not in x:
            print ("{} is sexy prime".format(i))

execfile("ElderSieve.py")

