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
            print ("{} is sexy prime".format(i))

execfile("ElderSieve.py")










