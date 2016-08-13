#!/usr/local/env python #python 2.7
#Integration leaves residue sequence A202110
#CODE HAS ERROR, SHOWS THAT 43 IS NOT PRIME, BUT DOES NOT CANCEL IT IN SPREADSHEET. READ ERROR OF SOME KIND!!!
import sys
import csv
import time
import subprocess

dump = open("composite1.csv", "w")
new_test = 40000



####################################################
#new 
#7, 195, 563, 1111, 1839, 2747, 3835, 5103, 6551, 8179, 9987
def dr7_ld7_7_91(x):
  y = 90*(x*x) - 82*x - 1 
  if y > new_test:
    return
  #print "7w,91", y
  dump.write(str(y) + "\n")
  for n in range(1, new_test):
    new_y = y+((7+(90*(x-1)))*n) 
    new2_y = y+((91+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
    
   # else:
   #   pass
###################################################

###################################################
#new
#9, 161, 493, 1005, 1697, 2569, 3621, 4853, 6265, 7857, 9629
def dr7_ld7_19_43(x):
  y = 90*(x*x) - 118*x + 37
  if y > new_test:
    return
  dump.write(str(y) + "\n") 
  for n in range (1, new_test):
    new_y = y+((19+(90*(x-1)))*n)
    new2_y = y+((43+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")

###################################################

###################################################
#25, 213, 581, 1129, 1857, 2765, 3853, 5121, 6569, 8197, 10005
#new
def dr7_ld7_37_61(x):
  y = 90*(x*x) - 82*x + 17
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((37+(90*(x-1)))*n)
    new2_y = y+((61+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
##################################################

##################################################
#64, 306, 728, 1330, 2112, 3074, 4216, 5538, 7040, 8722, 10584
#new 
def dr7_ld7_73_79(x):
  y = 90*(x*x) - 28*x + 2
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((73+(90*(x-1)))*n)
    new2_y = y+((79+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################	  

###################################################
#2, 120, 418, 896, 1554, 2392, 3410, 4608, 5986, 7544, 9282
#new
def dr7_ld7_11_17(x):
  y = 90*(x*x) - 152*x + 64  
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((11+(90*(x-1)))*n)
    new2_y = y+((17+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
####################################################

####################################################
#17, 189, 541, 1073, 1785, 2677, 3749, 5001, 6433, 8045, 9837
#new
def dr7_ld7_29_53(x):
  y = 90*(x*x) - 98*x + 25
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((29+(90*(x-1)))*n) 
    new2_y = y+((53+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
######################################################

######################################################

#37, 245, 633, 1201, 1949, 2877, 3985, 5273, 6741, 8389
#new
def dr7_ld7_47_71(x):
  y = 90*(x*x) - 62*x + 9
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((47+(90*(x-1)))*n)
    new2_y = y+((71+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
#############################################################

##############################################################

#82, 344, 786, 1408, 2210, 3192, 4354, 5696, 7218, 8920
#new
def dr7_ld7_83_89(x):
  y = 90*(x*x) - 8*x 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((83+(90*(x-1)))*n) 
    new2_y = y+((89+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
############################################################

########################################################
 
#7, 159, 491, 1003, 1695, 2567, 3619, 4851, 6263, 7855, 9627
#new
def dr7_ld7_13_49(x):
  y = 90*(x*x) - 118*x + 35 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((13+(90*(x-1)))*n)
    new2_y = y+((49+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
############################################################

########################################################

#23, 211, 579, 1127, 1855, 2763, 3851, 5119, 6567, 8195
#new
def dr7_ld7_31_67(x):
  y = 90*(x*x) - 82*x + 15
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((31+(90*(x-1)))*n) 
    new2_y = y+((67+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
#############################################

########################################################
#15, 187, 539, 1071, 1783, 2675, 3747, 4999, 6431, 8043, 9835
#new
def dr7_ld7_23_59(x):
  y = 90*(x*x) - 98*x + 23
  if y > new_test:
    return
  #print y, "23,59"
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((23+(90*(x-1)))*n)
    new2_y = y+((59+(90*(x-1)))*n) 
    #print new_y, "23"
    #print new2_y, "59"
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
######################################################

#####################################################

#35, 243, 631, 1199, 1947, 2875, 3983, 5271, 6739, 8387
#new
def dr7_ld7_41_77(x):
  y = 90*(x*x) - 62*x + 7
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((41+(90*(x-1)))*n)
    new2_y = y+((77+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
   
#########################################################

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


for x in xrange(1, 100): 
 
    dr7_ld7_7_91(x)# checked
    dr7_ld7_19_43(x)#checked
    dr7_ld7_37_61(x)#checked
    dr7_ld7_73_79(x)#checked
    dr7_ld7_11_17(x)#checked
    dr7_ld7_29_53(x)#checked
    dr7_ld7_47_71(x)#checked
    dr7_ld7_83_89(x)#checked
    dr7_ld7_13_49(x)#checked
    dr7_ld7_31_67(x)#checked
    dr7_ld7_23_59(x)#checked
    dr7_ld7_41_77(x)#checked
   
 
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

#run this code to compare to http://oeis.org/A202110/b202110.txt
with open("composite2.csv") as f:
    rd=f.readlines()
    x=[t.strip("\n") for t in rd]
    for i in range(0, 37188):
        if str(i) not in x:
            print ("{} is cousin prime".format(i))

execfile("ElderSieve.py") 










