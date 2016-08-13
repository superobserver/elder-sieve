#!/usr/local/env python #python 2.7
#Integration leaves residue sequence A201819
import sys
import csv
import time
import subprocess

dump = open("composite1.csv", "w")
new_test = 40000


####################################################
#new 
#31, 243, 635, 1207, 1959, 2891, 4003, 5295, 6787, 8419
def dr4_ld1_31_91(x):
  y = 90*(x*x) - 58*x - 1 
  if y > new_test:
    return
  #print "13,91", y
  dump.write(str(y) + "\n")
  for n in range(1, new_test):
    new_y = y+((31+(90*(x-1)))*n) 
    new2_y = y+((91+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################


###################################################
#new
#10, 168, 506, 1024, 1722, 2600, 3658, 4896
def dr4_ld1_19_49(x):
  y = 90*(x*x) - 112*x + 32
  if y > new_test:
    return
  dump.write(str(y) + "\n") 
  for n in range (1, new_test):
    new_y = y+((19+(90*(x-1)))*n)
    new2_y = y+((49+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################

###################################################
#5, 145, 465, 965, 1645, 2505, 3545, 4765, 6165, 7745
#new
def dr4_ld1_13_37(x):
  y = 90*(x*x) - 130*x + 45
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((13+(90*(x-1)))*n)
    new2_y = y+((37+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
##################################################

##################################################
#54, 284, 694, 1284, 2054, 3004, 4134, 5444, 6934, 8604
#new 
def dr4_ld1_67_73(x):
  y = 90*(x*x) - 40*x + 4 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((67+(90*(x-1)))*n)
    new2_y = y+((73+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################	  

###################################################
#1, 113, 405, 877, 1529, 2361, 3373, 4565, 5937, 7489
#new
def dr4_ld1_11_11(x):
  y = 90*(x*x) - 158*x + 69  
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((11+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")

####################################################

####################################################
#9, 157, 485, 993, 1681, 2549, 3597, 4825, 6233, 7821
#new
def dr4_ld1_29_29(x):
  y = 90*(x*x) - 122*x + 41
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((29+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
######################################################

######################################################

#43, 263, 663, 1243, 2003, 2943, 4063, 5363, 6843
#new
def dr4_ld1_47_83(x):
  y = 90*(x*x) - 50*x + 3
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((47+(90*(x-1)))*n)
    new2_y = y+((83+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
#############################################################

##############################################################

#4, 134, 444, 934, 1604, 2454, 3484, 4694, 6084, 7654
#new
def dr4_ld1_17_23(x):
  y = 90*(x*x) - 140*x + 54
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((17+(90*(x-1)))*n) 
    new2_y = y+((23+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
############################################################

########################################################
 
#32, 234, 616, 1178, 1920, 2842, 3944, 5226, 6688
#new
def dr4_ld1_41_71(x):
  y = 90*(x*x) - 68*x + 10
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((41+(90*(x-1)))*n)
    new2_y = y+((71+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
############################################################

########################################################

#58, 296, 714, 1312, 2090, 3048, 4186, 5504, 7002, 8680
#new
def dr4_ld1_59_89(x):
  y = 90*(x*x) - 32*x 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((59+(90*(x-1)))*n) 
    new2_y = y+((89+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
########################################################

########################################################
#45, 265, 665, 1245, 2005, 2945, 4065, 5365, 6845, 8505
#new
def dr4_ld1_53_77(x):
  y = 90*(x*x) - 50*x + 5
  if y > new_test:
    return
  #print y, "7,79"
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((53+(90*(x-1)))*n)
    new2_y = y+((77+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
######################################################

#####################################################

#3, 143, 463, 963, 1643, 2503, 3543, 4763, 6163, 7743
#new
def dr4_ld1_7_43(x):
  y = 90*(x*x) - 130*x + 43  
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((7+(90*(x-1)))*n)
    new2_y = y+((43+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
   
#########################################################

#####################################################

#41, 253, 645, 1217, 1969, 2901, 4013, 5305, 6777
#new
def dr4_ld1_61_61(x):
  y = 90*(x*x) - 58*x + 9  
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((61+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
   
#########################################################

#####################################################

#69, 317, 745, 1353, 2141, 3109, 4257, 5585, 7093
#new
def dr4_ld1_79_79(x):
  y = 90*(x*x) - 22*x + 1  
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((79+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
   
#########################################################
    
for x in xrange(1, 100): 
 
    dr4_ld1_31_91(x)#
    dr4_ld1_19_49(x) #
    dr4_ld1_13_37(x) #
    dr4_ld1_67_73(x)#
    dr4_ld1_11_11(x)#
    dr4_ld1_29_29(x) #
    dr4_ld1_47_83(x)#
    dr4_ld1_17_23(x)#
    dr4_ld1_41_71(x)#
    dr4_ld1_59_89(x)#
    dr4_ld1_53_77(x)#
    dr4_ld1_7_43(x) #
    dr4_ld1_61_61(x)#
    dr4_ld1_79_79(x)#	

    
    

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








