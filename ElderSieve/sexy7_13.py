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
#13, 207, 581, 1135, 1869, 2783, 3877, 5151, 6605, 8239
def dr4_ld3_13_91(x):
  y = 90*(x*x) - 76*x - 1 
  if y > new_test:
    return
  #print "13,91", y
  dump.write(str(y) + "\n")
  for n in range(1, new_test):
    new_y = y+((13+(90*(x-1)))*n) 
    new2_y = y+((91+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################


###################################################
#new
#14, 190, 546, 1082, 1798, 2694, 3770, 5026, 6462, 8078
def dr4_ld3_19_67(x):
  y = 90*(x*x) - 94*x + 18
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((19+(90*(x-1)))*n)
    new2_y = y+((67+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################


###################################################
#20, 196, 552, 1088, 1804, 2700, 3776, 5032, 6468, 8084
#new
def dr4_ld3_37_49(x):
  y = 90*(x*x) - 94*x + 24
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((37+(90*(x-1)))*n)
    new2_y = y+((49+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
##################################################


##################################################
#25, 219, 593, 1147, 1881, 2795, 3889, 5163, 6617, 8251
#new 
def dr4_ld3_31_73(x):
  y = 90*(x*x) - 76*x + 11 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((31+(90*(x-1)))*n)
    new2_y = y+((73+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################	  


###################################################
#10, 194, 558, 1102, 1826, 2730, 3814, 5078, 6522, 8146, 9950
#new
def dr4_ld3_11_83(x):
  y = 90*(x*x) - 86*x + 6  
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((11+(90*(x-1)))*n)
    new2_y = y+((83+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
####################################################


####################################################
#15, 181, 527, 1053, 1759, 2645, 3711, 4957, 6383, 7989, 9775
#new
def dr4_ld3_29_47(x):
  y = 90*(x*x) - 104*x + 29
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((29+(90*(x-1)))*n) 
    new2_y = y+((47+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
######################################################


######################################################

#18, 202, 566, 1110, 1834, 2738, 3822, 5086, 6530, 8154, 9958
#new
def dr4_ld3_23_71(x):
  y = 90*(x*x) - 86*x + 14
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((23+(90*(x-1)))*n)
    new2_y = y+((71+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
#############################################################

##############################################################

#24, 208, 572, 1116, 1840, 2744, 3828, 5092, 6536, 8160, 9964
#new
def dr4_ld3_41_53(x):
  y = 90*(x*x) - 86*x + 20
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((41+(90*(x-1)))*n) 
    new2_y = y+((53+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
############################################################

########################################################
 
#11, 177, 523, 1049, 1755, 2641, 3707, 4953, 6379, 7985, 9771
#new
def dr4_ld3_17_59(x):
  y = 90*(x*x) - 104*x + 25
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((17+(90*(x-1)))*n)
    new2_y = y+((59+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
############################################################

########################################################

#76, 332, 768, 1384, 2180, 3156, 4312, 5648, 7164, 8860
#new
def dr4_ld3_77_89(x):
  y = 90*(x*x) - 14*x 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((77+(90*(x-1)))*n) 
    new2_y = y+((89+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
########################################################


########################################################
#6, 182, 538, 1074, 1790, 2686, 3762
#new
def dr4_ld3_7_79(x):
  y = 90*(x*x) - 94*x + 10
  if y > new_test:
    return
  #print y, "7,79"
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((7+(90*(x-1)))*n)
    new2_y = y+((79+(90*(x-1)))*n) 
    #print new_y, "7"
    #print new2_y, "79"
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
######################################################

#####################################################

#29, 223, 597, 1151, 1885, 2799, 3893, 5167, 6621, 8255
#new
def dr4_ld3_43_61(x):
  y = 90*(x*x) - 76*x + 15  
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((43+(90*(x-1)))*n)
    new2_y = y+((61+(90*(x-1)))*n)   
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
   
 
    dr4_ld3_13_91(x)#
    dr4_ld3_19_67(x) #
    dr4_ld3_37_49(x) #
    dr4_ld3_31_73(x) #
    dr4_ld3_11_83(x)#
    dr4_ld3_29_47(x) #
    dr4_ld3_23_71(x)#
    dr4_ld3_41_53(x) #
    dr4_ld3_17_59(x) #
    dr4_ld3_77_89(x)#
    dr4_ld3_7_79(x)#
    dr4_ld3_43_61(x) #

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
            print ("{} is sexy prime".format(i))

execfile("ElderSieve.py") 










