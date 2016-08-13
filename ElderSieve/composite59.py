#!/usr/local/env python #python 2.7
#Integration leaves residue sequence A202101
import sys
import csv
import time
import subprocess

dump = open("composite1.csv", "w")
new_test = 40000


####################################################
#new 
#59, 299, 719, 1319, 2099, 3059, 4199, 5519, 7019, 8699
def dr5_ld9_59_91(x):
  y = 90*(x*x) - 30*x - 1 
  if y > new_test:
    return
  #print "49,89", y
  dump.write(str(y) + "\n")
  for n in range(1, new_test):
    new_y = y+((59+(90*(x-1)))*n) 
    new2_y = y+((91+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################

###################################################
#new
#8, 158, 488, 998, 1688, 2558, 3608, 4838, 6248, 7838, 9608
def dr5_ld9_19_41(x):
  y = 90*(x*x) - 120*x + 38
  if y > new_test:
    return
  dump.write(str(y) + "\n") 
  for n in range (1, new_test):
    new_y = y+((19+(90*(x-1)))*n)
    new2_y = y+((41+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################

###################################################
#31, 235, 619, 1183, 1927, 2851, 3955, 5239, 6703, 8347
#new
def dr5_ld9_37_77(x):
  y = 90*(x*x) - 66*x + 7
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((37+(90*(x-1)))*n)
    new2_y = y+((77+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
##################################################

##################################################
#18, 204, 570, 1116, 1842, 2748, 3834, 5100, 6546, 8172
#new 
def dr5_ld9_23_73(x):
  y = 90*(x*x) - 84*x +  12
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((23+(90*(x-1)))*n)
    new2_y = y+((73+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################	  

###################################################
#9, 189, 549, 1089, 1809, 2709, 3789, 5049, 6489, 8109, 9909
#new
def dr5_ld9_11_79(x):
  y = 90*(x*x) - 90*x + 9  
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((11+(90*(x-1)))*n)
    new2_y = y+((79+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
####################################################

####################################################
#19, 199, 559, 1099, 1819, 2719, 3799, 5059, 6499, 8119, 9919
#new
def dr5_ld9_29_61(x):
  y = 90*(x*x) - 90*x + 19
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((29+(90*(x-1)))*n) 
    new2_y = y+((61+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
######################################################

######################################################

#3, 147, 471, 975, 1659, 2523, 3567, 4791, 6195, 7779, 9543
#new
def dr5_ld9_7_47(x):
  y = 90*(x*x) - 126*x + 39
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((7+(90*(x-1)))*n)
    new2_y = y+((47+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
#############################################################

##############################################################

#39, 255, 651, 1227, 1983, 2919, 4035, 5331, 6807, 8463
#new
def dr5_ld9_43_83(x):
  y = 90*(x*x) - 54*x + 3 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((43+(90*(x-1)))*n) 
    new2_y = y+((83+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
############################################################

########################################################
 
#7, 163, 499, 1015, 1711, 2587, 3643, 4879, 6295, 7891, 9667
#new
def dr5_ld9_13_53(x):
  y = 90*(x*x) - 114*x + 31 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((13+(90*(x-1)))*n)
    new2_y = y+((53+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
############################################################

########################################################

#30, 240, 630, 1200, 1950, 2880, 3990, 5280, 6750, 8400
#new
def dr5_ld9_31_89(x):
  y = 90*(x*x) - 60*x 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((31+(90*(x-1)))*n) 
    new2_y = y+((89+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
########################################################

########################################################
#38, 248, 638, 1208, 1958, 2888, 3998, 5288, 6758, 8408
#new
def dr5_ld9_49_71(x):
  y = 90*(x*x) - 60*x + 8
  if y > new_test:
    return
  #print y, "49,71"
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((49+(90*(x-1)))*n)
    new2_y = y+((71+(90*(x-1)))*n) 
    #print new_y, "49"
    #print new2_y, "71"
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
######################################################

#####################################################

#12, 186, 540, 1074, 1788, 2682, 3756, 5010, 6444
#new
def dr5_ld9_17_67(x):
  y = 90*(x*x) - 96*x + 18
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((17+(90*(x-1)))*n)
    new2_y = y+((67+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
   
#########################################################

   
for x in xrange(1, 100): 
 
    dr5_ld9_59_91(x)#
    dr5_ld9_19_41(x)#
    dr5_ld9_37_77(x)#
    dr5_ld9_23_73(x)#
    dr5_ld9_11_79(x)#
    dr5_ld9_29_61(x)#
    dr5_ld9_7_47(x)#
    dr5_ld9_43_83(x)#
    dr5_ld9_13_53(x) #
    dr5_ld9_31_89(x)#
    dr5_ld9_49_71(x)#
    dr5_ld9_17_67(x)#

    
    

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









