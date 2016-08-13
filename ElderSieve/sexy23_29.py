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


####################################################
#new 
#29, 239, 629, 1199, 1949, 2879, 3989, 5279, 6749, 8399
def dr2_ld9_29_91(x):
  y = 90*(x*x) - 60*x - 1 
  if y > new_test:
    return
  #print "47,91", y
  dump.write(str(y) + "\n")
  for n in range(1, new_test):
    new_y = y+((29+(90*(x-1)))*n) 
    new2_y = y+((91+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################


###################################################
#new
#2, 122, 422, 902, 1562, 2402, 3422, 4622, 6002, 7562, 9302
def dr2_ld9_11_19(x):
  y = 90*(x*x) - 150*x + 62
  if y > new_test:
    return
  dump.write(str(y) + "\n") 
  for n in range (1, new_test):
    new_y = y+((11+(90*(x-1)))*n)
    new2_y = y+((19+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################


###################################################
#19, 193, 547, 1081, 1795, 2689, 3763, 5017, 6451, 8065, 9859
#new
def dr2_ld9_37_47(x):
  y = 90*(x*x) - 96*x + 25
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((37+(90*(x-1)))*n)
    new2_y = y+((47+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
##################################################


##################################################
#67, 313, 739, 1345, 2131, 3097, 4243, 5569, 7075, 8761, 10627
#new 
def dr2_ld9_73_83(x):
  y = 90*(x*x) - 24*x + 1 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((73+(90*(x-1)))*n)
    new2_y = y+((83+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################	  


###################################################
#3, 129, 435, 921, 1587, 2433, 3459, 4665, 6051
#new
def dr2_ld9_13_23(x):
  y = 90*(x*x) - 144*x + 57  
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((13+(90*(x-1)))*n)
    new2_y = y+((23+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
####################################################


####################################################
#20, 200, 560, 1100, 1820, 2720, 3800, 5060, 6500, 8120
#new
def dr2_ld9_31_59(x):
  y = 90*(x*x) - 90*x + 20
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((31+(90*(x-1)))*n) 
    new2_y = y+((59+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
######################################################


######################################################

#22, 202, 562, 1102, 1822, 2722, 3802, 5062, 6502
#new
def dr2_ld9_41_49(x):
  y = 90*(x*x) - 90*x + 22
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((41+(90*(x-1)))*n)
    new2_y = y+((49+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
#############################################################


##############################################################

#57, 291, 705, 1299, 2073, 3027, 4161, 5475, 6969, 8643
#new
def dr2_ld9_67_77(x):
  y = 90*(x*x) - 36*x + 3
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((67+(90*(x-1)))*n) 
    new2_y = y+((77+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
############################################################


########################################################
 
#1, 115, 409, 883, 1537, 2371, 3385, 4579, 5953, 7507, 9241
#new
def dr2_ld9_7_17(x):
  y = 90*(x*x) - 156*x + 67
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((7+(90*(x-1)))*n)
    new2_y = y+((17+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
############################################################

########################################################

#25, 211, 577, 1123, 1849, 2755, 3841, 5107, 6553, 8179
#new
def dr2_ld9_43_53(x):
  y = 90*(x*x) - 84*x + 19 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((43+(90*(x-1)))*n) 
    new2_y = y+((53+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
########################################################


########################################################
#60, 300, 720, 1320, 2100, 3060, 4200, 5520, 7020, 8700
#new
def dr2_ld9_61_89(x):
  y = 90*(x*x) - 30*x 
  if y > new_test:
    return
  #print y, "61,89"
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((61+(90*(x-1)))*n)
    new2_y = y+((89+(90*(x-1)))*n) 
    #print new_y, "61"
    #print new2_y, "89"
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
######################################################

#####################################################

#62, 302, 722, 1322, 2102, 3062, 4202, 5522
#new
def dr2_ld9_71_79(x):
  y = 90*(x*x) - 30*x + 2  
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((71+(90*(x-1)))*n)
    new2_y = y+((79+(90*(x-1)))*n)   
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

    dr2_ld9_29_91(x) #
    dr2_ld9_11_19(x) #
    dr2_ld9_37_47(x) #
    dr2_ld9_73_83(x) #
    dr2_ld9_13_23(x)#
    dr2_ld9_31_59(x) #
    dr2_ld9_41_49(x)#
    dr2_ld9_67_77(x) #
    dr2_ld9_7_17(x) #
    dr2_ld9_43_53(x)#
    dr2_ld9_61_89(x) #
    dr2_ld9_71_79(x) #
    

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
            print ("{} is sexy prime".format(i))


execfile("ElderSieve.py")









