#!/usr/local/env python #python 2.7
#Integration leaves residue sequence A202114
import sys
import csv
import time
import subprocess

dump = open("composite1.csv", "w")
new_test = 40000



####################################################
#new 
#53, 287, 701, 1295, 2069, 3023, 4157, 5471, 6965, 8639
def dr8_ld3_53_91(x):
  y = 90*(x*x) - 36*x - 1 
  if y > new_test:
    return
  #print "71,91", y
  dump.write(str(y) + "\n")
  for n in range(1, new_test):
    new_y = y+((53+(90*(x-1)))*n) 
    new2_y = y+((91+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################

###################################################
#new
#3, 129, 435, 921, 1587, 2433, 3459, 4665, 6051, 7617, 9363
def dr8_ld3_17_19(x):
  y = 90*(x*x) - 144*x + 57
  if y > new_test:
    return
  dump.write(str(y) + "\n") 
  for n in range (1, new_test):
    new_y = y+((17+(90*(x-1)))*n)
    new2_y = y+((19+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################

###################################################
#36, 252, 648, 1224, 1980, 2916, 4032, 5328, 6804, 8460
#new
def dr8_ld3_37_89(x):
  y = 90*(x*x) - 54*x
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((37+(90*(x-1)))*n)
    new2_y = y+((89+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
##################################################

##################################################
#57, 291, 705, 1299, 2073, 3027, 4161, 5475, 6969, 8643
#new 
def dr8_ld3_71_73(x):
  y = 90*(x*x) - 36*x + 3
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((71+(90*(x-1)))*n)
    new2_y = y+((73+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################	  

###################################################
#1, 115, 409, 883, 1537, 2371, 3385, 4579, 5953, 7507, 9241
#new
def dr8_ld3_11_13(x):
  y = 90*(x*x) - 156*x + 67  
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((11+(90*(x-1)))*n)
    new2_y = y+((13+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
####################################################

####################################################
#21, 207, 573, 1119, 1845, 2751, 3837, 5103, 6549, 8175, 9981
#new
def dr8_ld3_29_67(x):
  y = 90*(x*x) - 84*x + 15
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((29+(90*(x-1)))*n) 
    new2_y = y+((67+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
######################################################

######################################################

#25, 211, 577, 1123, 1849, 2755, 3841, 5107, 6553, 8179, 9985
#new
def dr8_ld3_47_49(x):
  y = 90*(x*x) - 84*x + 19
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((47+(90*(x-1)))*n)
    new2_y = y+((49+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
#############################################################

##############################################################

#28, 232, 616, 1180, 1924, 2848, 3952, 5236, 6700, 8344, 10168
#new
def dr8_ld3_31_83(x):
  y = 90*(x*x) - 66*x + 4 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((31+(90*(x-1)))*n) 
    new2_y = y+((83+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
############################################################

########################################################
 
#15, 189, 543, 1077, 1791, 2685, 3759, 5013, 6447, 8061, 9855
#new
def dr8_ld3_23_61(x):
  y = 90*(x*x) - 96*x + 21 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((23+(90*(x-1)))*n)
    new2_y = y+((61+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
############################################################

########################################################

#19, 193, 547, 1081, 1795, 2689, 3763, 5017, 6451, 8065, 9859
#new
def dr8_ld3_41_43(x):
  y = 90*(x*x) - 96*x + 25
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((41+(90*(x-1)))*n) 
    new2_y = y+((43+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
########################################################

########################################################
#4, 160, 496, 1012, 1708, 2584, 3640, 4876, 6292, 7888, 9664
#new
def dr8_ld3_7_59(x):
  y = 90*(x*x) - 114*x + 28
  if y > new_test:
    return
  #print y, "7,59"
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((7+(90*(x-1)))*n)
    new2_y = y+((59+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
######################################################

#####################################################

#67, 313, 739, 1345, 2131, 3097, 4243, 5569, 7075, 8761, 10627
#new
def dr8_ld3_77_79(x):
  y = 90*(x*x) - 24*x + 1
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((77+(90*(x-1)))*n)
    new2_y = y+((79+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
#########################################################

for x in xrange(1, 100): 
 
    dr8_ld3_53_91(x)#  
    dr8_ld3_17_19(x)# 
    dr8_ld3_37_89(x)# 
    dr8_ld3_71_73(x)# 
    dr8_ld3_11_13(x)# 
    dr8_ld3_29_67(x)# 
    dr8_ld3_47_49(x)# 
    dr8_ld3_31_83(x)# 
    dr8_ld3_23_61(x)# 
    dr8_ld3_41_43(x)# 
    dr8_ld3_7_59(x)# 
    dr8_ld3_77_79(x)# 

    

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










