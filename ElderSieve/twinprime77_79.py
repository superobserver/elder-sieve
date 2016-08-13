#!/usr/local/env python #python 2.7
#Integration leaves residue sequence A201822
import sys
import csv
import time
import subprocess

dump = open("composite1.csv", "w")
new_test = 40000

####################################################
#new 
#79, 339, 779, 1399, 2199, 3179, 4339, 5679, 7199, 8899
def dr7_ld9_79_91(x):
  y = 90*(x*x) - 10*x - 1 
  #print "7w,91", y
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range(1, new_test):
    new_y = y+((79+(90*(x-1)))*n) 
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
#12, 182, 532, 1062, 1772, 2662, 3732, 4982, 6412, 8022, 9812
def dr7_ld9_19_61(x):
  y = 90*(x*x) - 100*x + 22
  dump.write(str(y) + "\n") 
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((19+(90*(x-1)))*n)
    new2_y = y+((61+(90*(x-1)))*n)   
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
###################################################

###################################################
#2, 136, 450, 944, 1618, 2472, 3506, 4720, 6114, 7688, 9442
#new
def dr7_ld9_7_37(x):
  y = 90*(x*x) - 136*x + 48
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((7+(90*(x-1)))*n)
    new2_y = y+((37+(90*(x-1)))*n)   
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
##################################################

##################################################
#34, 240, 626, 1192, 1938, 2864, 3970, 5256, 6722, 8368
#new 
def dr7_ld9_43_73(x):
  y = 90*(x*x) - 64*x + 8
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((43+(90*(x-1)))*n)
    new2_y = y+((73+(90*(x-1)))*n)   
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
###################################################	  

###################################################
#10, 200, 570, 1120, 1850, 2760, 3850, 5120, 6570, 8200
#new
def dr7_ld9_11_89(x):
  y = 90*(x*x) - 80*x  
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((11+(90*(x-1)))*n)
    new2_y = y+((89+(90*(x-1)))*n) 
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
####################################################

####################################################
#22, 212, 582, 1132, 1862, 2772, 3862, 5132, 6582, 8212
#new
def dr7_ld9_29_71(x):
  y = 90*(x*x) - 80*x + 12
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((29+(90*(x-1)))*n) 
    new2_y = y+((71+(90*(x-1)))*n) 
    dump.write(str(new_y) + "\n")  
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
######################################################

######################################################

#8, 162, 496, 1010, 1704, 2578, 3632, 4866, 6280, 7874, 9648
#new
def dr7_ld9_17_47(x):
  y = 90*(x*x) - 116*x + 34
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((17+(90*(x-1)))*n)
    new2_y = y+((47+(90*(x-1)))*n)  
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
#############################################################

##############################################################

#48, 274, 680, 1266, 2032, 2978, 4104, 5410, 6896, 8562
#new
def dr7_ld9_53_83(x):
  y = 90*(x*x) - 44*x + 2 
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((53+(90*(x-1)))*n) 
    new2_y = y+((83+(90*(x-1)))*n)
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
############################################################

########################################################
 
#1, 117, 413, 889, 1545, 2381, 3397, 4593, 5969, 7525, 9261
#new
def dr7_ld9_13_13(x):
  y = 90*(x*x) - 154*x + 65 
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((13+(90*(x-1)))*n)
    #new2_y = y+((13+(90*(x-1)))*n)  
    dump.write(str(new_y) + "\n")   
    #dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
############################################################

########################################################

#16, 186, 536, 1066, 1776, 2666, 3736, 4986, 6416, 8026, 9816
#new
def dr7_ld9_31_49(x):
  y = 90*(x*x) - 100*x + 26
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((31+(90*(x-1)))*n) 
    new2_y = y+((49+(90*(x-1)))*n)  
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
########################################################

########################################################
#49, 273, 677, 1261, 2025, 2969, 4093, 5397, 6881, 8545
#new
def dr7_ld9_67_67(x):
  y = 90*(x*x) - 46*x + 5
  #print y, "67,67"
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((67+(90*(x-1)))*n)
    #new2_y = y+((67+(90*(x-1)))*n) 
    #print new_y, "67"
    #print new2_y, "67"
    dump.write(str(new_y) + "\n")  
    #dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
######################################################

#####################################################

#5, 141, 457, 953, 1629, 2485, 3521, 4737, 6133, 7709, 9465
#new
def dr7_ld9_23_23(x):
  y = 90*(x*x) - 134*x + 49
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((23+(90*(x-1)))*n)
    #new2_y = y+((23+(90*(x-1)))*n)   
    dump.write(str(new_y) + "\n")  
    #dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
   
#########################################################

#####################################################

#26, 216, 586, 1136, 1866, 2776, 3866, 5136, 6586, 8216, 10026
#new
def dr7_ld9_41_59(x):
  y = 90*(x*x) - 80*x + 16
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((41+(90*(x-1)))*n)
    new2_y = y+((59+(90*(x-1)))*n)   
    dump.write(str(new_y) + "\n")  
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
   
#########################################################

#####################################################

#65, 309, 733, 1337, 2121, 3085, 4229, 5553, 7057, 8741
#new
def dr7_ld9_77_77(x):
  y = 90*(x*x) - 26*x + 1
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((77+(90*(x-1)))*n)
    #new2_y = y+((59+(90*(x-1)))*n)   
    dump.write(str(new_y) + "\n")  
    #dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
   
#########################################################



####################################################
#new 
#77, 335, 773, 1391, 2189, 3167, 4325, 5663, 7181, 8879
def dr5_ld7_77_91(x):
  y = 90*(x*x) - 12*x - 1 
  #print "49,89", y
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range(1, new_test):
    new_y = y+((77+(90*(x-1)))*n) 
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
#4, 136, 448, 940, 1612, 2464, 3496, 4708, 6100, 7672, 9424
def dr5_ld7_19_23(x):
  y = 90*(x*x) - 138*x + 52
  dump.write(str(y) + "\n") 
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((19+(90*(x-1)))*n)
    new2_y = y+((23+(90*(x-1)))*n)   
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
###################################################

###################################################
#16, 184, 532, 1060, 1768, 2656, 3724, 4972, 6400, 8008, 9796
#new
def dr5_ld7_37_41(x):
  y = 90*(x*x) - 102*x + 28
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((37+(90*(x-1)))*n)
    new2_y = y+((41+(90*(x-1)))*n)   
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
##################################################

##################################################
#47, 269, 671, 1253, 2015, 2957, 4079, 5381, 6863, 8525
#new 
def dr5_ld7_59_73(x):
  y = 90*(x*x) - 48*x + 5 
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((59+(90*(x-1)))*n)
    new2_y = y+((73+(90*(x-1)))*n)   
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
###################################################	  

###################################################
#0, 108, 396, 864, 1512, 2340, 3348, 4536, 5904, 7452, 9180
#new
def dr5_ld7_7_11(x):
  y = 90*(x*x) - 162*x + 72  
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((7+(90*(x-1)))*n)
    new2_y = y+((11+(90*(x-1)))*n) 
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
####################################################

####################################################
#13, 175, 517, 1039, 1741, 2623, 3685, 4927, 6349, 7951, 9733
#new
def dr5_ld7_29_43(x):
  y = 90*(x*x) - 108*x + 31
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((29+(90*(x-1)))*n) 
    new2_y = y+((43+(90*(x-1)))*n) 
    dump.write(str(new_y) + "\n")  
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
######################################################

######################################################

#31, 229, 607, 1165, 1903, 2821, 3919, 5197, 6655, 8293
#new
def dr5_ld7_47_61(x):
  y = 90*(x*x) - 72*x + 13
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((47+(90*(x-1)))*n)
    new2_y = y+((61+(90*(x-1)))*n)  
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
#############################################################

##############################################################

#72, 324, 756, 1368, 2160, 3132, 4284, 5616, 7128, 8820
#new
def dr5_ld7_79_83(x):
  y = 90*(x*x) - 18*x 
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((79+(90*(x-1)))*n) 
    new2_y = y+((83+(90*(x-1)))*n)
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
############################################################

########################################################
 
#12, 204, 576, 1128, 1860, 2772, 3864, 5136, 6588, 8220
#new
def dr5_ld7_13_89(x):
  y = 90*(x*x) - 78*x 
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((13+(90*(x-1)))*n)
    new2_y = y+((89+(90*(x-1)))*n)  
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
############################################################

########################################################

#5, 143, 461, 959, 1637, 2495, 3533, 4751, 6149, 7727, 9485
#new
def dr5_ld7_17_31(x):
  y = 90*(x*x) - 132*x + 47 
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((17+(90*(x-1)))*n) 
    new2_y = y+((31+(90*(x-1)))*n)  
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
########################################################

########################################################
#28, 220, 592, 1144, 1876, 2788, 3880, 5152, 6604, 8236
#new
def dr5_ld7_49_53(x):
  y = 90*(x*x) - 78*x + 16
  #print y, "49,53"
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((49+(90*(x-1)))*n)
    new2_y = y+((53+(90*(x-1)))*n) 
    #print new_y, "49"
    #print new2_y, "53"
    dump.write(str(new_y) + "\n")  
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
######################################################

#####################################################

#52, 280, 688, 1276, 2044, 2992, 4120, 5428, 6916, 8584
#new
def dr5_ld7_67_71(x):
  y = 90*(x*x) - 42*x + 4
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((67+(90*(x-1)))*n)
    new2_y = y+((71+(90*(x-1)))*n)   
    dump.write(str(new_y) + "\n")  
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
   
#########################################################

   
for x in xrange(1, 100): 
 
    dr5_ld7_77_91(x)#
    dr5_ld7_19_23(x)#
    dr5_ld7_37_41(x) #
    dr5_ld7_59_73(x)#
    dr5_ld7_7_11(x)#
    dr5_ld7_29_43(x)#
    dr5_ld7_47_61(x)#
    dr5_ld7_79_83(x)#
    dr5_ld7_13_89(x) #
    dr5_ld7_17_31(x)#
    dr5_ld7_49_53(x)#
    dr5_ld7_67_71(x)#

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










