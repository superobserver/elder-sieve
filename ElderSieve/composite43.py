#!/usr/local/env python #python 2.7
#Integration leaves residue sequence A202105
import sys
import csv
import time
import subprocess

dump = open("composite1.csv", "w")
new_test = 40000



####################################################
#new 
#43, 267, 671, 1255, 2019, 2963, 4087, 5391, 6875, 8539
def dr7_ld3_43_91(x):
  y = 90*(x*x) - 46*x - 1 
  if y > new_test:
    return
  #print "49,89", y
  dump.write(str(y) + "\n")
  for n in range(1, new_test):
    new_y = y+((43+(90*(x-1)))*n) 
    new2_y = y+((91+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################

###################################################
#new
#1, 117, 413, 889, 1545, 2381, 3397, 4593, 5969, 7525, 9261
def dr7_ld3_7_19(x):
  y = 90*(x*x) - 154*x + 65
  if y > new_test:
    return
  dump.write(str(y) + "\n") 
  for n in range (1, new_test):
    new_y = y+((7+(90*(x-1)))*n)
    new2_y = y+((19+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################

###################################################
#32, 238, 624, 1190, 1936, 2862, 3968, 5254, 6720, 8366
#new
def dr7_ld3_37_79(x):
  y = 90*(x*x) - 64*x + 6
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((37+(90*(x-1)))*n)
    new2_y = y+((79+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
##################################################

##################################################
#49, 273, 677, 1261, 2025, 2969, 4093, 5397, 6881, 8545
#new 
def dr7_ld3_61_73(x):
  y = 90*(x*x) - 46*x + 5
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((61+(90*(x-1)))*n)
    new2_y = y+((73+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################	  

###################################################
#6, 160, 494, 1008, 1702, 2576, 3630, 4864, 6278, 7872, 9646
#new
def dr7_ld3_11_53(x):
  y = 90*(x*x) - 116*x + 32  
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((11+(90*(x-1)))*n)
    new2_y = y+((53+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
####################################################

####################################################
#5, 141, 457, 953, 1629, 2485, 3521, 4737, 6133, 7709, 9465
#new
def dr7_ld3_17_29(x):
  y = 90*(x*x) - 134*x + 49
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((17+(90*(x-1)))*n) 
    new2_y = y+((29+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
######################################################

######################################################

#46, 272, 678, 1264, 2030, 2976, 4102, 5408, 6894, 8560, 10406
#new
def dr7_ld3_47_89(x):
  y = 90*(x*x) - 44*x 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((47+(90*(x-1)))*n)
    new2_y = y+((89+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
#############################################################

##############################################################

#65, 309, 733, 1337, 2121, 3085, 4229, 5553, 7057, 8741, 10605
#new
def dr7_ld3_71_83(x):
  y = 90*(x*x) - 26*x + 1 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((71+(90*(x-1)))*n) 
    new2_y = y+((83+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
############################################################

########################################################
 
#4, 138, 452, 946, 1620, 2474, 3508, 4722, 6116, 7690
#new
def dr7_ld3_13_31(x):
  y = 90*(x*x) - 136*x + 50 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((13+(90*(x-1)))*n)
    new2_y = y+((31+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
############################################################

########################################################

#36, 242, 628, 1194, 1940, 2866, 3972, 5258, 6724, 8370, 10196
#new
def dr7_ld3_49_67(x):
  y = 90*(x*x) - 64*x + 10
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((49+(90*(x-1)))*n) 
    new2_y = y+((67+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
########################################################

########################################################
#10, 164, 498, 1012, 1706, 2580, 3634, 4868, 6282, 7876, 9650
#new
def dr7_ld3_23_41(x):
  y = 90*(x*x) - 116*x + 36
  if y > new_test:
    return
  #print y, "49,49"
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((23+(90*(x-1)))*n)
    new2_y = y+((41+(90*(x-1)))*n) 
    #print new_y, "23"
    #print new2_y, "41"
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
######################################################

#####################################################

#50, 276, 682, 1268, 2034, 2980, 4106, 5412, 6898, 8564, 10410
#new
def dr7_ld3_59_77(x):
  y = 90*(x*x) - 44*x + 4
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((59+(90*(x-1)))*n)
    new2_y = y+((77+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
   
#########################################################


for x in xrange(1, 100): 
 
    dr7_ld3_43_91(x)#
    dr7_ld3_7_19(x)#
    dr7_ld3_37_79(x)#
    dr7_ld3_61_73(x)#
    dr7_ld3_11_53(x)#
    dr7_ld3_17_29(x)#
    dr7_ld3_47_89(x)#
    dr7_ld3_71_83(x)#
    dr7_ld3_13_31(x)#
    dr7_ld3_49_67(x)#
    dr7_ld3_23_41(x)#
    dr7_ld3_59_77(x)#
   
    

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









