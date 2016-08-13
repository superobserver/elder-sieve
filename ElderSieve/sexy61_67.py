#!/usr/local/env python #python 2.7
#Integration leaves residue sequence A202113
import sys
import csv
import time
import subprocess

dump = open("composite1.csv", "w")
new_test = 40000


####################################################
#new 
#61, 303, 725, 1327, 2109
def dr7_ld1_61_91(x):
  y = 90*(x*x) - 28*x - 1 
  if y > new_test:
    return
  #print "49,89", y
  dump.write(str(y) + "\n")
  for n in range(1, new_test):
    new_y = y+((61+(90*(x-1)))*n) 
    new2_y = y+((91+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################

###################################################
#new
#16, 204, 572, 1120, 1848, 2756, 3844, 5112, 6560, 8188, 9996
def dr7_ld1_19_79(x):
  y = 90*(x*x) - 82*x + 8
  if y > new_test:
    return
  dump.write(str(y) + "\n") 
  for n in range (1, new_test):
    new_y = y+((19+(90*(x-1)))*n)
    new2_y = y+((79+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################

###################################################
#17, 187, 537, 1067, 1777, 2667, 3737, 4987, 6417, 8027
#new
def dr7_ld1_37_43(x):
  y = 90*(x*x) - 100*x + 27
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((37+(90*(x-1)))*n)
    new2_y = y+((43+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
##################################################

##################################################
#5, 175, 525, 1055, 1765, 2655, 3725, 4975, 6405, 8015, 9805
#new 
def dr7_ld1_7_73(x):
  y = 90*(x*x) - 100*x +  15
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((7+(90*(x-1)))*n)
    new2_y = y+((73+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################	  

###################################################
#8, 180, 532, 1064, 1776, 2668, 3740, 4992, 6424, 8036, 9828
#new
def dr7_ld1_11_71(x):
  y = 90*(x*x) - 98*x + 16  
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((11+(90*(x-1)))*n)
    new2_y = y+((71+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
####################################################

####################################################
#28, 236, 624, 1192, 1940, 2868, 3976, 5264, 6732, 8380
#new
def dr7_ld1_29_89(x):
  y = 90*(x*x) - 62*x
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((29+(90*(x-1)))*n) 
    new2_y = y+((89+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
######################################################

######################################################

#27, 217, 587, 1137, 1867, 2777, 3867, 5137, 6587, 8217
#new
def dr7_ld1_47_53(x):
  y = 90*(x*x) - 80*x + 17
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((47+(90*(x-1)))*n)
    new2_y = y+((53+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
#############################################################

##############################################################

#15, 205, 575, 1125, 1855, 2765, 3855, 5125, 6575, 8205
#new
def dr7_ld1_17_83(x):
  y = 90*(x*x) - 80*x + 5 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((17+(90*(x-1)))*n) 
    new2_y = y+((83+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
############################################################

########################################################
 
#9, 179, 529, 1059, 1769, 2659, 3729, 4979, 6409, 8019, 9809
#new
def dr7_ld1_13_67(x):
  y = 90*(x*x) - 100*x + 19 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((13+(90*(x-1)))*n)
    new2_y = y+((67+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
############################################################

########################################################

#10, 162, 494, 1006, 1698, 2570, 3622, 4854, 6266, 7858, 9630
#new
def dr7_ld1_31_31(x):
  y = 90*(x*x) - 118*x + 38
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((31+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")

########################################################

########################################################
#26, 214, 582, 1130, 1858, 2766, 3854, 5122, 6570, 8198
#new
def dr7_ld1_49_49(x):
  y = 90*(x*x) - 82*x + 18
  if y > new_test:
    return
  #print y, "49,49"
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((49+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")

######################################################

#####################################################

#19, 209, 579, 1129, 1859, 2769, 3859, 5129, 6579, 8209
#new
def dr7_ld1_23_77(x):
  y = 90*(x*x) - 80*x + 9
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((23+(90*(x-1)))*n)
    new2_y = y+((77+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
   
#########################################################

#####################################################

#18, 190, 542, 1074, 1786, 2678, 3750, 5002, 6434, 8046, 9838
#new
def dr7_ld1_41_41(x):
  y = 90*(x*x) - 98*x + 26
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((41+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
   
######################################################### 

#####################################################

#38, 246, 634, 1202, 1950, 2878, 3986, 5274, 6742, 8390
#new
def dr7_ld1_59_59(x):
  y = 90*(x*x) - 62*x + 10
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((59+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
   
######################################################### 


####################################################
#new 
#67, 315, 743, 1351, 2139, 3107, 4255, 5583
def dr4_ld7_67_91(x):
  y = 90*(x*x) - 22*x - 1 
  if y > new_test:
    return
  #print "67,91", y
  dump.write(str(y) + "\n")
  for n in range(1, new_test):
    new_y = y+((67+(90*(x-1)))*n) 
    new2_y = y+((91+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################


###################################################
#new
#2, 124, 426, 908, 1570, 2412, 3434, 4636
def dr4_ld7_13_19(x):
  y = 90*(x*x) - 148*x + 60
  if y > new_test:
    return
  dump.write(str(y) + "\n") 
  for n in range (1, new_test):
    new_y = y+((13+(90*(x-1)))*n)
    new2_y = y+((19+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################


###################################################
#12, 170, 508, 1026, 1724, 2602, 3660, 4898
#new
def dr4_ld7_31_37(x):
  y = 90*(x*x) - 112*x + 34
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((31+(90*(x-1)))*n)
    new2_y = y+((37+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
##################################################


##################################################
#39, 251, 643, 1215, 1967, 2899, 4011, 5303
#new 
def dr4_ld7_49_73(x):
  y = 90*(x*x) - 58*x + 7 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((49+(90*(x-1)))*n)
    new2_y = y+((73+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################	  

###################################################
#5, 153, 481, 989, 1677, 2545, 3593, 4821, 6229
#new
def dr4_ld7_11_47(x):
  y = 90*(x*x) - 122*x + 37  
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((11+(90*(x-1)))*n)
    new2_y = y+((47+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
####################################################


####################################################
#26, 228, 610, 1172, 1914, 2836, 3938, 5220, 6682
#new
def dr4_ld7_29_83(x):
  y = 90*(x*x) - 68*x + 4
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((29+(90*(x-1)))*n) 
    new2_y = y+((83+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
######################################################


######################################################

#7, 155, 483, 991, 1679, 2547, 3595, 4823, 6231
#new
def dr4_ld7_17_41(x):
  y = 90*(x*x) - 122*x + 39
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((17+(90*(x-1)))*n)
    new2_y = y+((41+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
#############################################################

##############################################################

#34, 236, 618, 1180, 1922, 2844, 3946, 5228, 6690
#new
def dr4_ld7_53_59(x):
  y = 90*(x*x) - 68*x + 12
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((53+(90*(x-1)))*n) 
    new2_y = y+((59+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
############################################################

########################################################
 
#60, 298, 716, 1314, 2092, 3050, 4188, 5506, 7004
#new
def dr4_ld7_71_77(x):
  y = 90*(x*x) - 32*x + 2
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((71+(90*(x-1)))*n)
    new2_y = y+((77+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
############################################################

########################################################

#4, 162, 500, 1018, 1716, 2594, 3652, 4890, 6308, 7906
#new
def dr4_ld7_7_61(x):
  y = 90*(x*x) - 112*x + 26 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((7+(90*(x-1)))*n) 
    new2_y = y+((61+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
########################################################

########################################################
#37, 249, 641, 1213, 1965, 2897, 4009, 5301, 6773, 8425
#new
def dr4_ld7_43_79(x):
  y = 90*(x*x) - 58*x + 5
  if y > new_test:
    return
  #print y, "43,79"
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((43+(90*(x-1)))*n)
    new2_y = y+((79+(90*(x-1)))*n) 
    #print new_y, "43"
    #print new2_y, "79"
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
######################################################

#####################################################

#22, 224, 606, 1168, 1910, 2832, 3934, 5216, 6678, 8320
#new
def dr4_ld7_23_89(x):
  y = 90*(x*x) - 68*x
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((23+(90*(x-1)))*n)
    new2_y = y+((89+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
   
#########################################################

for x in xrange(1, 100): 
 
    dr7_ld1_61_91(x)#
    dr7_ld1_19_79(x)#
    dr7_ld1_37_43(x)#
    dr7_ld1_7_73(x)#
    dr7_ld1_11_71(x)#
    dr7_ld1_29_89(x)#
    dr7_ld1_47_53(x)#
    dr7_ld1_17_83(x)#
    dr7_ld1_13_67(x) #
    dr7_ld1_31_31(x)#
    dr7_ld1_49_49(x)#
    dr7_ld1_23_77(x)#
    dr7_ld1_41_41(x)
    dr7_ld1_59_59(x)    
 
    dr4_ld7_67_91(x)#
    dr4_ld7_13_19(x) #
    dr4_ld7_31_37(x) #
    dr4_ld7_49_73(x) #
    dr4_ld7_11_47(x)#
    dr4_ld7_29_83(x) #
    dr4_ld7_17_41(x)#
    dr4_ld7_53_59(x) #
    dr4_ld7_71_77(x) #
    dr4_ld7_7_61(x)#
    dr4_ld7_43_79(x)#
    dr4_ld7_23_89(x) #
	
   

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









