#!/usr/local/env python #python 2.7
#Integration leaves residue sequence A201820
import sys
import csv
import time
import subprocess

dump = open("composite1.csv", "w")
new_test = 40000



####################################################
#new 
#23, 227, 611, 1175, 1919, 2843, 3947, 5231, 6695, 8339
def dr5_ld3_23_91(x):
  y = 90*(x*x) - 66*x - 1 
  if y > new_test:
    return
  #print "49,89", y
  dump.write(str(y) + "\n")
  for n in range(1, new_test):
    new_y = y+((23+(90*(x-1)))*n) 
    new2_y = y+((91+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################

###################################################
#new
#16, 202, 568, 1114, 1840, 2746, 3832, 5096, 6544, 8170, 9976
def dr5_ld3_19_77(x):
  y = 90*(x*x) - 84*x + 10
  if y > new_test:
    return
  dump.write(str(y) + "\n") 
  for n in range (1, new_test):
    new_y = y+((19+(90*(x-1)))*n)
    new2_y = y+((77+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################

###################################################
#24, 210, 576, 1122, 1848, 2754, 3840, 5106, 6552, 8178, 9984
#new
def dr5_ld3_37_59(x):
  y = 90*(x*x) - 84*x + 18
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((37+(90*(x-1)))*n)
    new2_y = y+((59+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
##################################################

##################################################
#33, 237, 621, 1185, 1929, 2853, 3957, 5241, 6705, 8349
#new 
def dr5_ld3_41_73(x):
  y = 90*(x*x) - 66*x + 9 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((41+(90*(x-1)))*n)
    new2_y = y+((73+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################	  

###################################################
#5, 149, 473, 977, 1661, 2525, 3569, 4793, 6197, 7787, 9545
#new
def dr5_ld3_11_43(x):
  y = 90*(x*x) - 126*x + 41  
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((11+(90*(x-1)))*n)
    new2_y = y+((43+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
####################################################

####################################################
#2, 128, 434, 920, 1586, 2432, 3458, 4664, 6050, 7616, 9362
#new
def dr5_ld3_7_29(x):
  y = 90*(x*x) - 144*x + 56
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((7+(90*(x-1)))*n) 
    new2_y = y+((29+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
######################################################

######################################################

#41, 257, 653, 1229, 1985, 2921, 4037, 5333, 6809, 8465
#new
def dr5_ld3_47_79(x):
  y = 90*(x*x) - 54*x + 5
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((47+(90*(x-1)))*n)
    new2_y = y+((79+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
#############################################################

##############################################################

#56, 290, 704, 1298, 2072, 3026, 4160, 5474, 6968, 8642
#new
def dr5_ld3_61_83(x):
  y = 90*(x*x) - 36*x + 2
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((61+(90*(x-1)))*n) 
    new2_y = y+((83+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
############################################################

########################################################
 
#10, 184, 538, 1072, 1786, 2680, 3754, 5008, 6442, 8056, 9850
#new
def dr5_ld3_13_71(x):
  y = 90*(x*x) - 96*x + 16
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((13+(90*(x-1)))*n)
    new2_y = y+((71+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
############################################################

########################################################

#18, 192, 546, 1080, 1794, 2688, 3762, 5016, 6450, 8064, 9858
#new
def dr5_ld3_31_53(x):
  y = 90*(x*x) - 96*x + 24 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((31+(90*(x-1)))*n) 
    new2_y = y+((53+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
########################################################

########################################################
#9, 165, 501, 1017, 1713, 2589, 3645, 4881, 6297, 7893, 9669
#new
def dr5_ld3_17_49(x):
  y = 90*(x*x) - 114*x + 33
  if y > new_test:
    return
  #print y, "17,49"
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((17+(90*(x-1)))*n)
    new2_y = y+((49+(90*(x-1)))*n) 
    #print new_y, "17"
    #print new2_y, "49"
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
######################################################

#####################################################

#66, 312, 738, 1344, 2130, 3096, 4242, 5568, 7074, 8760
#new
def dr5_ld3_67_89(x):
  y = 90*(x*x) - 24*x
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((67+(90*(x-1)))*n)
    new2_y = y+((89+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
   
#########################################################

   
for x in xrange(1, 100): 
 
    dr5_ld3_23_91(x)#
    dr5_ld3_19_77(x)#
    dr5_ld3_37_59(x) #
    dr5_ld3_41_73(x)#
    dr5_ld3_11_43(x)#
    dr5_ld3_7_29(x)#
    dr5_ld3_47_79(x)#
    dr5_ld3_61_83(x) #
    dr5_ld3_13_71(x) #
    dr5_ld3_31_53(x)#
    dr5_ld3_17_49(x)#
    dr5_ld3_67_89(x)#

    
    

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









