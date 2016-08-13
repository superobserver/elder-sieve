#!/usr/local/env python #python 2.7
#Integration leaves residue sequence A202129
import sys
import csv
import time
import subprocess

dump = open("composite1.csv", "w")
new_test = 40000

def dr1_ld1_73_91(x):
  y = 90*(x*x) - 16*x - 1 
  #print "73,91", y
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range(1, new_test):
    new_y = y+((73+(90*(x-1)))*n)
    new2_y = y+((91+(90*(x-1)))*n)
    #print new_y, "73"
    #print new2_y, "91"  
    dump.write(str(new_y) + "\n")
    dump.write(str(new2_y) + "\n")
    if new_y > new_test: 
      return
    else:
      pass


def dr1_ld1_19_37(x):
  y = 90*(x*x) - 124*x + 41 
  dump.write(str(y) + "\n") 
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+ ((19+(90*(x-1)))*n)
    new2_y = y+ ((37+(90*(x-1)))*n)
    dump.write(str(new_y) + "\n")
    dump.write(str(new2_y) + "\n")
    if new_y > new_test: 
      return
    else:
      pass


def dr1_ld1_11_23(x):
  y = 90*(x*x) - 146*x + 58
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((11+(90*(x-1)))*n)
    new2_y = y+((23+(90*(x-1)))*n) 
    dump.write(str(new_y) + "\n")  
    dump.write(str(new2_y) + "\n")    
    if new_y > new_test: 
      return
    else:
      pass



def dr1_ld1_29_77(x):
  y = 90*(x*x) - 74*x + 8
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((29+(90*(x-1)))*n)
    new2_y = y+((77+(90*(x-1)))*n)   
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass


def dr1_ld1_47_59(x):
  y = 90*(x*x) - 74*x + 14
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((47+(90*(x-1)))*n)
    new2_y = y+((59+(90*(x-1)))*n) 
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass


def dr1_ld1_41_83(x):
  y = 90*(x*x) - 56*x + 3
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((41+(90*(x-1)))*n) 
    new2_y = y+((83+(90*(x-1)))*n) 
    dump.write(str(new_y) + "\n")  
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass



def dr1_ld1_13_61(x):
  y = 90*(x*x) - 106*x + 24
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((13+(90*(x-1)))*n)
    new2_y = y+((61+(90*(x-1)))*n)  
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass


def dr1_ld1_31_43(x):
  y = 90*(x*x) - 106*x + 30
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((31+(90*(x-1)))*n) 
    new2_y = y+((43+(90*(x-1)))*n)
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass


def dr1_ld1_7_49(x):
  y = 90*(x*x) - 124*x + 37
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((7+(90*(x-1)))*n)
    new2_y = y+((49+(90*(x-1)))*n)  
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass



def dr1_ld1_67_79(x):
  y = 90*(x*x) - 34*x + 2
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((67+(90*(x-1)))*n) 
    new2_y = y+((79+(90*(x-1)))*n)  
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass


def dr1_ld1_17_89(x):
  y = 90*(x*x) - 74*x 
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((17+(90*(x-1)))*n)
    new2_y = y+((89+(90*(x-1)))*n) 
    dump.write(str(new_y) + "\n")  
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass

def dr1_ld1_53_71(x):
  y = 90*(x*x) - 56*x + 7
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((53+(90*(x-1)))*n)
    new2_y = y+((71+(90*(x-1)))*n)   
    dump.write(str(new_y) + "\n")  
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass


####################################################
#new 
#71, 323, 755, 1367, 2159, 3131, 4283, 5615, 7127, 8819
def dr8_ld1_71_91(x):
  y = 90*(x*x) - 18*x - 1 
  #print "71,91", y
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range(1, new_test):
    new_y = y+((71+(90*(x-1)))*n) 
    new2_y = y+((91+(90*(x-1)))*n) 
    dump.write(str(new_y) + "\n")
    dump.write(str(new2_y) + "\n")
    if new_y > new_test: 
      return
    else:
      pass
###################################################

###################################################
#new
#18, 216, 594, 1152, 1890, 2808, 3906, 5184, 6642, 8280, 10098
def dr8_ld1_19_89(x):
  y = 90*(x*x) - 72*x 
  dump.write(str(y) + "\n") 
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((19+(90*(x-1)))*n)
    new2_y = y+((89+(90*(x-1)))*n)   
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
###################################################

###################################################
#21, 201, 561, 1101, 1821, 2721, 3801, 5061, 6501, 8121, 9921
#new
def dr8_ld1_37_53(x):
  y = 90*(x*x) - 90*x + 21
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((37+(90*(x-1)))*n)
    new2_y = y+((53+(90*(x-1)))*n)   
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
##################################################

##################################################
#13, 193, 553, 1093, 1813, 2713, 3793, 5053, 6493, 8113, 9913
#new 
def dr8_ld1_17_73(x):
  y = 90*(x*x) - 90*x + 13
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((17+(90*(x-1)))*n)
    new2_y = y+((73+(90*(x-1)))*n)   
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
###################################################	  

###################################################
#13, 135, 447, 939, 1611, 2463, 3495, 4707, 6099, 7671, 9423
#new
def dr8_ld1_11_31(x):
  y = 90*(x*x) - 138*x + 51  
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((11+(90*(x-1)))*n)
    new2_y = y+((31+(90*(x-1)))*n) 
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
####################################################

####################################################
#15, 183, 531, 1059, 1767, 2655, 3723, 4971, 6399, 8007, 9795
#new
def dr8_ld1_29_49(x):
  y = 90*(x*x) - 102*x + 27
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((29+(90*(x-1)))*n) 
    new2_y = y+((49+(90*(x-1)))*n) 
    dump.write(str(new_y) + "\n")  
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
######################################################

######################################################

#6, 156, 486, 996, 1686, 2556, 3606, 4836, 6246, 7836, 9606
#new
def dr8_ld1_13_47(x):
  y = 90*(x*x) - 120*x + 36
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((13+(90*(x-1)))*n)
    new2_y = y+((47+(90*(x-1)))*n)  
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
#############################################################

##############################################################

#61, 301, 721, 1321, 2101, 3061, 4201, 5521, 7021, 8701
#new
def dr8_ld1_67_83(x):
  y = 90*(x*x) - 30*x + 1 
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((67+(90*(x-1)))*n) 
    new2_y = y+((83+(90*(x-1)))*n)
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
############################################################

########################################################
 
#1, 121, 421, 901, 1561, 2401, 3421, 4621, 6001, 7561, 9301
#new
def dr8_ld1_7_23(x):
  y = 90*(x*x) - 150*x + 61 
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((7+(90*(x-1)))*n)
    new2_y = y+((23+(90*(x-1)))*n)  
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
############################################################

########################################################

#27, 219, 591, 1143, 1875, 2787, 3879, 5151, 6603, 8235, 10047
#new
def dr8_ld1_41_61(x):
  y = 90*(x*x) - 78*x + 15
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((41+(90*(x-1)))*n) 
    new2_y = y+((61+(90*(x-1)))*n)  
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
########################################################

########################################################
#51, 279, 687, 1275, 2043, 2991, 4119, 5427, 6915, 8583
#new
def dr8_ld1_59_79(x):
  y = 90*(x*x) - 42*x + 3
  #print y, "59,79"
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((59+(90*(x-1)))*n)
    new2_y = y+((79+(90*(x-1)))*n) 
    #print new_y, "59"
    #print new2_y, "79"
    dump.write(str(new_y) + "\n")  
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
######################################################

#####################################################

#36, 246, 636, 1206, 1956, 2886, 3996, 5286, 6756, 8406
#new
def dr8_ld1_43_77(x):
  y = 90*(x*x) - 60*x + 6
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((43+(90*(x-1)))*n)
    new2_y = y+((77+(90*(x-1)))*n)   
    dump.write(str(new_y) + "\n")  
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
   
#########################################################

for x in xrange(1, 100): 
 
    dr8_ld1_71_91(x)#  
    dr8_ld1_19_89(x)# 
    dr8_ld1_37_53(x)# 
    dr8_ld1_17_73(x)# 
    dr8_ld1_11_31(x)# 
    dr8_ld1_29_49(x)# 
    dr8_ld1_13_47(x)# 
    dr8_ld1_67_83(x)# 
    dr8_ld1_7_23(x)# 
    dr8_ld1_41_61(x)# 
    dr8_ld1_59_79(x)# 
    dr8_ld1_43_77(x)# 

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
            print ("{} is twin prime".format(i))


execfile("ElderSieve.py")









