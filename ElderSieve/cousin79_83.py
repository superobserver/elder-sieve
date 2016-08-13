#!/usr/local/env python #python 2.7
#Integration leaves residue sequence A202112
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

####################################################
#new 
#83, 347, 791, 1415, 2219, 3203, 4367, 5711, 7235, 8939
def dr2_ld3_83_91(x):
  y = 90*(x*x) - 6*x - 1 
  if y > new_test:
    return
  #print "11,91", y
  dump.write(str(y) + "\n")
  for n in range(1, new_test):
    new_y = y+((83+(90*(x-1)))*n) 
    new2_y = y+((91+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################



###################################################
#new
#9, 165, 501, 1017, 1713, 2589, 3645
def dr2_ld3_19_47(x):
  y = 90*(x*x) - 114*x + 33
  if y > new_test:
    return
  dump.write(str(y) + "\n") 
  for n in range (1, new_test):
    new_y = y+((19+(90*(x-1)))*n)
    new2_y = y+((47+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################


###################################################
#11, 167, 503, 1019, 1715, 2591, 3647, 4883, 6299, 7895
#new
def dr2_ld3_37_29(x):
  y = 90*(x*x) - 114*x + 35
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((29+(90*(x-1)))*n)
    new2_y = y+((37+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
##################################################


##################################################
#8, 182, 536, 1070, 1784, 2678, 3752, 5006, 6440, 8054, 9848
#new 
def dr2_ld3_11_73(x):
  y = 90*(x*x) - 96*x + 14 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((11+(90*(x-1)))*n)
    new2_y = y+((73+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################	  


###################################################
#5, 149, 473, 977, 1661, 2525, 3569, 4793, 6197
#new
def dr2_ld3_13_41(x):
  y = 90*(x*x) - 126*x + 41  
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((13+(90*(x-1)))*n)
    new2_y = y+((41+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
####################################################


####################################################
#7, 151, 475, 979, 1663, 2527, 3571, 4795, 6199
#new
def dr2_ld3_23_31(x):
  y = 90*(x*x) - 126*x + 43
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((23+(90*(x-1)))*n) 
    new2_y = y+((31+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
 ######################################################
 

 ######################################################

 
#41, 257, 653, 1229, 1985, 2921, 4037, 5333
#new
def dr2_ld3_49_77(x):
  y = 90*(x*x) - 54*x + 5
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((49+(90*(x-1)))*n)
    new2_y = y+((77+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
#############################################################

##############################################################

#43, 259, 655, 1231, 1987, 2923, 4039, 5335, 6811
#new
def dr2_ld3_59_67(x):
  y = 90*(x*x) - 54*x + 7
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((59+(90*(x-1)))*n) 
    new2_y = y+((67+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
############################################################


########################################################
 
#6, 192, 558, 1104, 1830, 2736, 3822, 5088, 6534, 8160
#new
def dr2_ld3_7_89(x):
  y = 90*(x*x) - 84*x 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((7+(90*(x-1)))*n)
    new2_y = y+((89+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
############################################################


########################################################

#33, 237, 621, 1185, 1929, 2853, 3957, 5241
#new
def dr2_ld3_43_71(x):
  y = 90*(x*x) - 66*x + 9 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((43+(90*(x-1)))*n) 
    new2_y = y+((71+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
########################################################


########################################################
#35, 239, 623, 1187, 1931, 2855, 3959, 5243, 6707
#new
def dr2_ld3_53_61(x):
  y = 90*(x*x) - 66*x + 11 
  if y > new_test:
    return
  #print y, "7,67"
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((53+(90*(x-1)))*n)
    new2_y = y+((61+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
######################################################

#####################################################

#14, 200, 566, 1112, 1838, 2744, 3830, 5096, 6542, 8168
#new
def dr2_ld3_17_79(x):
  y = 90*(x*x) - 84*x + 8  
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((17+(90*(x-1)))*n)
    new2_y = y+((79+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
   
#########################################################


for x in xrange(1, 100): 
 
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
    

    dr2_ld3_83_91(x) #
    dr2_ld3_19_47(x)  #
    dr2_ld3_37_29(x) #
    dr2_ld3_11_73(x) #
    dr2_ld3_13_41(x) #
    dr2_ld3_23_31(x) #
    dr2_ld3_49_77(x) #
    dr2_ld3_59_67(x) #
    dr2_ld3_7_89(x) #
    dr2_ld3_43_71(x) #
    dr2_ld3_53_61(x) #
    dr2_ld3_17_79(x) #



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
            print ("{} is cousin prime".format(i))

execfile("ElderSieve.py")










