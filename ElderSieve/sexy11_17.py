#!/usr/local/env python #python 2.7
#Integration leaves residue sequence A201804
import sys
import csv
import time
import subprocess

dump = open("composite1.csv", "w")
new_test = 40000




####################################################
#new
# dr2_ld1_11_91(x) 
#11, 203, 575, 1127, 1859, 2771, 3863, 5135, 6587, 8219
def dr2_ld1_11_91(x):
  y = 90*(x*x) - 78*x - 1 
  if y > new_test:
      return
  #print "11,91", y
  dump.write(str(y) + "\n")
  for n in range(1, new_test):
    new_y = y+((11+(90*(x-1)))*n) 
    new2_y = y+((91+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################



###################################################

#6, 144, 462, 960, 1638, 2496, 3534, 4752, 6150
#new
def dr2_ld1_19_29(x):
  y = 90*(x*x) - 132*x + 48
  if y > new_test:
    return
  dump.write(str(y) + "\n") 
  for n in range (1, new_test):
    new_y = y+((19+(90*(x-1)))*n)
    new2_y = y+((29+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################


###################################################
#34, 244, 634, 1204, 1954, 2884, 3994, 5284
#new
def dr2_ld1_37_83(x):
  y = 90*(x*x) - 60*x + 4
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((37+(90*(x-1)))*n)
    new2_y = y+((83+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
##################################################

##################################################
#38, 248, 638, 1208, 1958, 2888, 3998, 5288, 6758
#new 
def dr2_ld1_47_73(x):
  y = 90*(x*x) - 60*x + 8 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((47+(90*(x-1)))*n)
    new2_y = y+((73+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################	  

###################################################
#11, 191, 551, 1091, 1811, 2711, 3791, 5051, 6491
#new
def dr2_ld1_13_77(x):
  y = 90*(x*x) - 90*x + 11  
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((13+(90*(x-1)))*n)
    new2_y = y+((77+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
####################################################

####################################################
#14, 176, 518, 1040, 1742, 2624, 3686, 4928, 6350
#new
def dr2_ld1_31_41(x):
  y = 90*(x*x) - 108*x + 32
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((31+(90*(x-1)))*n) 
    new2_y = y+((41+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
 ######################################################
 
 ######################################################

 
#32, 230, 608, 1166, 1904, 2822, 3920, 5198
#new
def dr2_ld1_49_59(x):
  y = 90*(x*x) - 72*x + 14
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((49+(90*(x-1)))*n)
    new2_y = y+((59+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
#############################################################

##############################################################

#17, 197, 557, 1097, 1817, 2717, 3797, 5057, 6497, 8117, 9917
#new
def dr2_ld1_23_67(x):
  y = 90*(x*x) - 90*x + 17
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((23+(90*(x-1)))*n) 
    new2_y = y+((67+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
############################################################

########################################################
 
#4, 154, 484, 994, 1684, 2554, 3604, 4834, 6244
#new
def dr2_ld1_7_53(x):
  y = 90*(x*x) - 120*x + 34
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((7+(90*(x-1)))*n)
    new2_y = y+((53+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
############################################################

########################################################

#8, 158, 488, 998, 1688, 2558, 3608, 4838, 6248, 7838,
#new
def dr2_ld1_17_43(x):
  y = 90*(x*x) - 120*x + 38 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((17+(90*(x-1)))*n) 
    new2_y = y+((43+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
########################################################

#48, 270, 672, 1254, 2016, 2958, 4080, 5382, 6864, 8526
#new
def dr2_ld1_61_71(x):
  y = 90*(x*x) - 48*x + 6 
  if y > new_test:
    return
  #print y, "7,67"
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((61+(90*(x-1)))*n)
    new2_y = y+((71+(90*(x-1)))*n) 
    #print new_y, "61"
    #print new2_y, "71"
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
######################################################

#####################################################

#78, 336, 774, 1392, 2190, 3168, 4326, 5664, 7182, 8880
#new
def dr2_ld1_79_89(x):
  y = 90*(x*x) - 12*x  
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((79+(90*(x-1)))*n)
    new2_y = y+((89+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
   
#########################################################

####################################################
#new 
#17, 215, 593, 1151, 1889, 2807, 3905, 5183, 6641, 8279, 10097
def dr8_ld7_17_91(x):
  y = 90*(x*x) - 72*x - 1 
  if y > new_test:
    return
  #print "17,91", y
  dump.write(str(y) + "\n")
  for n in range(1, new_test):
    new_y = y+((17+(90*(x-1)))*n)
    new2_y = y+((91+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################

###################################################
#new
#11, 173, 515, 1037, 1739, 2621, 3683, 4925, 6347, 7949, 9731
def dr8_ld7_19_53(x):
  y = 90*(x*x) - 108*x + 29
  if y > new_test:
    return
  dump.write(str(y) + "\n") 
  for n in range (1, new_test):
    new_y = y+((19+(90*(x-1)))*n)
    new2_y = y+((53+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################

###################################################
#29, 227, 605, 1163, 1901, 2819, 3917, 5195, 6653, 8291
#new
def dr8_ld7_37_71(x):
  y = 90*(x*x) - 72*x + 11
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((37+(90*(x-1)))*n)
    new2_y = y+((71+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
##################################################

##################################################
#72, 324, 756, 1368, 2160, 3132, 4284, 5616, 7128, 8820
#new 
def dr8_ld7_73_89(x):
  y = 90*(x*x) - 18*x 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((73+(90*(x-1)))*n)
    new2_y = y+((89+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################	  

###################################################
#8, 176, 524, 1052, 1760, 2648, 3716, 4964, 6392, 8000, 9788
#new
def dr8_ld7_11_67(x):
  y = 90*(x*x) - 102*x + 20  
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((11+(90*(x-1)))*n)
    new2_y = y+((67+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
####################################################

####################################################
#21, 207, 573, 1119, 1845, 2751, 3837, 5103, 6549, 8175, 9981
#new
def dr8_ld7_13_29(x):
  y = 90*(x*x) - 138*x + 52
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((13+(90*(x-1)))*n) 
    new2_y = y+((29+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
######################################################

######################################################

#16, 184, 532, 1060, 1768, 2656, 3724, 4972, 6400, 8008, 9796
#new
def dr8_ld7_31_47(x):
  y = 90*(x*x) - 102*x + 28
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((31+(90*(x-1)))*n)
    new2_y = y+((47+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
#############################################################

##############################################################

#45, 267, 669, 1251, 2013, 2955, 4077, 5379, 6861, 8523
#new
def dr8_ld7_49_83(x):
  y = 90*(x*x) - 48*x + 3 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((49+(90*(x-1)))*n) 
    new2_y = y+((83+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
############################################################

########################################################
 
#20, 212, 584, 1136, 1868, 2780, 3872, 5144, 6596, 8228, 10040
#new
def dr8_ld7_23_79(x):
  y = 90*(x*x) - 78*x + 8 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((23+(90*(x-1)))*n)
    new2_y = y+((79+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
############################################################

########################################################

#3, 141, 459, 957, 1635, 2493, 3531, 4749, 6147, 7725, 9483
#new
def dr8_ld7_7_41(x):
  y = 90*(x*x) - 132*x + 45
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((7+(90*(x-1)))*n) 
    new2_y = y+((41+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
########################################################

########################################################
#28, 220, 592, 1144, 1876, 2788, 3880, 5152, 6604, 8236, 10048
#new
def dr8_ld7_43_59(x):
  y = 90*(x*x) - 78*x + 16
  if y > new_test:
    return
  #print y, "7,59"
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((43+(90*(x-1)))*n)
    new2_y = y+((59+(90*(x-1)))*n) 
    #print new_y, "7"
    #print new2_y, "59"
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
######################################################

#####################################################

#52, 280, 688, 1276, 2044, 2992, 4120, 5428, 6916, 8584
#new
def dr8_ld7_61_77(x):
  y = 90*(x*x) - 42*x + 4
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((61+(90*(x-1)))*n)
    new2_y = y+((77+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
   
#########################################################
    
for x in xrange(1, 100): 
 
    dr2_ld1_11_91(x) #
    dr2_ld1_19_29(x)  #
    dr2_ld1_37_83(x) #
    dr2_ld1_47_73(x) #
    dr2_ld1_13_77(x) #
    dr2_ld1_31_41(x) #
    dr2_ld1_49_59(x) #
    dr2_ld1_23_67(x) #
    dr2_ld1_7_53(x) #
    dr2_ld1_17_43(x) #
    dr2_ld1_61_71(x) #
    dr2_ld1_79_89(x) #
	

    dr8_ld7_17_91(x)#  
    dr8_ld7_19_53(x)# 
    dr8_ld7_37_71(x)# 
    dr8_ld7_73_89(x)# 
    dr8_ld7_11_67(x)# 
    dr8_ld7_13_29(x)# 
    dr8_ld7_31_47(x)# 
    dr8_ld7_49_83(x)# 
    dr8_ld7_23_79(x)# 
    dr8_ld7_7_41(x)# 
    dr8_ld7_43_59(x)# 
    dr8_ld7_61_77(x)# 
    

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










