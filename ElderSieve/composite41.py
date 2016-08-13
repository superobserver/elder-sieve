#!/usr/local/env python #python 2.7
#Integration leaves residue sequence A202104
import sys
import csv
import time
import subprocess

dump = open("composite1.csv", "w")
new_test = 40000


####################################################
#new 
#48, 276, 684, 1272, 2040, 2988, 4116, 5424
def dr5_ld1_49_89(x):
  y = 90*(x*x) - 42*x 
  if y > new_test:
    return
  #print "49,89", y
  dump.write(str(y) + "\n")
  for n in range(1, new_test):
    new_y = y+((49+(90*(x-1)))*n) 
    new2_y = y+((89+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################


###################################################
#new
#41, 263, 665, 1247
def dr5_ld1_41_91(x):
  y = 90*(x*x) - 48*x - 1
  if y > new_test:
    return
  dump.write(str(y) + "\n") 
  for n in range (1, new_test):
    new_y = y+((41+(90*(x-1)))*n)
    new2_y = y+((91+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################

###################################################
#12, 180, 528, 1056, 1764, 2652, 3720
#new
def dr5_ld1_19_59(x):
  y = 90*(x*x) - 102*x + 24
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((19+(90*(x-1)))*n)
    new2_y = y+((59+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
##################################################

##################################################
#9, 159, 489, 999, 1689, 2559, 3609, 4839
#new 
def dr5_ld1_23_37(x):
  y = 90*(x*x) - 120*x + 39 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((23+(90*(x-1)))*n)
    new2_y = y+((37+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################	  

###################################################
#7, 169, 511, 1033, 1735, 2617, 3679
#new
def dr5_ld1_11_61(x):
  y = 90*(x*x) - 108*x + 25  
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((11+(90*(x-1)))*n)
    new2_y = y+((61+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
####################################################

####################################################
#25, 223, 601, 1159, 1897, 2815
#new
def dr5_ld1_29_79(x):
  y = 90*(x*x) - 72*x + 7
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((29+(90*(x-1)))*n) 
    new2_y = y+((79+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
######################################################

######################################################

#22, 202, 562, 1102, 1822, 2722, 3802, 5062
#new
def dr5_ld1_43_47(x):
  y = 90*(x*x) - 90*x + 22
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((43+(90*(x-1)))*n)
    new2_y = y+((47+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
#############################################################

##############################################################

#2, 122, 422, 902, 1562, 2402, 3422, 4622, 6002, 7562
#new
def dr5_ld1_13_17(x):
  y = 90*(x*x) - 150*x + 62
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((13+(90*(x-1)))*n) 
    new2_y = y+((17+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
############################################################

########################################################
 
#24, 216, 588, 1140, 1872, 2784, 3876, 5148
#new
def dr5_ld1_31_71(x):
  y = 90*(x*x) - 78*x + 12
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((31+(90*(x-1)))*n)
    new2_y = y+((71+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
############################################################

########################################################

#62, 302, 722, 1322, 2102, 3062, 4202, 5522, 7022, 8702, 10562
#new
def dr5_ld1_73_77(x):
  y = 90*(x*x) - 30*x + 2 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((73+(90*(x-1)))*n) 
    new2_y = y+((77+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
########################################################

########################################################
#39, 249, 639, 1209, 1959, 2889, 3999, 5289, 6759
#new
def dr5_ld1_53_67(x):
  y = 90*(x*x) - 60*x + 9
  if y > new_test:
    return
  #print y, "53,67"
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((53+(90*(x-1)))*n)
    new2_y = y+((67+(90*(x-1)))*n) 
    #print new_y, "53"
    #print new2_y, "67"
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
######################################################

#####################################################

#6, 186, 546, 1086, 1806, 2706, 3786, 5046
#new
def dr5_ld1_7_83(x):
  y = 90*(x*x) - 90*x + 6
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((7+(90*(x-1)))*n)
    new2_y = y+((83+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
   
#########################################################

   
for x in xrange(1, 100): 
 
    dr5_ld1_49_89(x)#
    dr5_ld1_41_91(x) #
    dr5_ld1_19_59(x) #
    dr5_ld1_23_37(x)#
    dr5_ld1_11_61(x)#
    dr5_ld1_29_79(x)#
    dr5_ld1_43_47(x)#
    dr5_ld1_13_17(x) #
    dr5_ld1_31_71(x) #
    dr5_ld1_73_77(x)#
    dr5_ld1_53_67(x)#
    dr5_ld1_7_83(x)#

    
    

def bash_command(cmd):
    subprocess.Popen(cmd, shell=True)
bash_command('sort -n composite1.csv -o composite2.csv')
time.sleep(0.2) #make sure subprocess has finished

z=1000
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

#run this code to compare to http://oeis.org/A201804/b201804.txt
with open("composite2.csv") as f:
    rd=f.readlines()
    x=[t.strip("\n") for t in rd]
    for i in range(0, 37188):
        if str(i) not in x:
            print ("{} is prime".format(i))


execfile("ElderSieve.py")









