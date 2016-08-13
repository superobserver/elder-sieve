#!/usr/local/env python #python 2.7
#Integration leaves reside sequence A201739
import sys
import csv
import time
import subprocess

dump = open("composite1.csv", "w")
new_test = 40000


####################################################
#new 
#31, 243, 635, 1207, 1959, 2891, 4003, 5295, 6787, 8419
def dr4_ld1_31_91(x):
  y = 90*(x*x) - 58*x - 1 
  #print "13,91", y
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range(1, new_test):
    new_y = y+((31+(90*(x-1)))*n) 
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
#10, 168, 506, 1024, 1722, 2600, 3658, 4896
def dr4_ld1_19_49(x):
  y = 90*(x*x) - 112*x + 32
  dump.write(str(y) + "\n") 
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((19+(90*(x-1)))*n)
    new2_y = y+((49+(90*(x-1)))*n)   
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
###################################################

###################################################
#5, 145, 465, 965, 1645, 2505, 3545, 4765, 6165, 7745
#new
def dr4_ld1_13_37(x):
  y = 90*(x*x) - 130*x + 45
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((13+(90*(x-1)))*n)
    new2_y = y+((37+(90*(x-1)))*n)   
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
##################################################

##################################################
#54, 284, 694, 1284, 2054, 3004, 4134, 5444, 6934, 8604
#new 
def dr4_ld1_67_73(x):
  y = 90*(x*x) - 40*x + 4 
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((67+(90*(x-1)))*n)
    new2_y = y+((73+(90*(x-1)))*n)   
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
###################################################	  

###################################################
#1, 113, 405, 877, 1529, 2361, 3373, 4565, 5937, 7489
#new
def dr4_ld1_11_11(x):
  y = 90*(x*x) - 158*x + 69  
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((11+(90*(x-1)))*n)
    #new2_y = y+((11+(90*(x-1)))*n) 
    dump.write(str(new_y) + "\n")   
    #dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
####################################################

####################################################
#9, 157, 485, 993, 1681, 2549, 3597, 4825, 6233, 7821
#new
def dr4_ld1_29_29(x):
  y = 90*(x*x) - 122*x + 41
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((29+(90*(x-1)))*n) 
    #new2_y = y+((29+(90*(x-1)))*n) 
    dump.write(str(new_y) + "\n")  
    #dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
######################################################

######################################################

#43, 263, 663, 1243, 2003, 2943, 4063, 5363, 6843
#new
def dr4_ld1_47_83(x):
  y = 90*(x*x) - 50*x + 3
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((47+(90*(x-1)))*n)
    new2_y = y+((83+(90*(x-1)))*n)  
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
#############################################################

##############################################################

#4, 134, 444, 934, 1604, 2454, 3484, 4694, 6084, 7654
#new
def dr4_ld1_17_23(x):
  y = 90*(x*x) - 140*x + 54
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((17+(90*(x-1)))*n) 
    new2_y = y+((23+(90*(x-1)))*n)
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
############################################################

########################################################
 
#32, 234, 616, 1178, 1920, 2842, 3944, 5226, 6688
#new
def dr4_ld1_41_71(x):
  y = 90*(x*x) - 68*x + 10
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((41+(90*(x-1)))*n)
    new2_y = y+((71+(90*(x-1)))*n)  
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
############################################################

########################################################

#58, 296, 714, 1312, 2090, 3048, 4186, 5504, 7002, 8680
#new
def dr4_ld1_59_89(x):
  y = 90*(x*x) - 32*x 
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((59+(90*(x-1)))*n) 
    new2_y = y+((89+(90*(x-1)))*n)  
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
########################################################

########################################################
#45, 265, 665, 1245, 2005, 2945, 4065, 5365, 6845, 8505
#new
def dr4_ld1_53_77(x):
  y = 90*(x*x) - 50*x + 5
  #print y, "7,79"
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((53+(90*(x-1)))*n)
    new2_y = y+((77+(90*(x-1)))*n) 
    #print new_y, "7"
    #print new2_y, "79"
    dump.write(str(new_y) + "\n")  
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
######################################################

#####################################################

#3, 143, 463, 963, 1643, 2503, 3543, 4763, 6163, 7743
#new
def dr4_ld1_7_43(x):
  y = 90*(x*x) - 130*x + 43  
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((7+(90*(x-1)))*n)
    new2_y = y+((43+(90*(x-1)))*n)   
    dump.write(str(new_y) + "\n")  
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
   
#########################################################

#####################################################

#41, 253, 645, 1217, 1969, 2901, 4013, 5305, 6777
#new
def dr4_ld1_61_61(x):
  y = 90*(x*x) - 58*x + 9  
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((61+(90*(x-1)))*n)
    #new2_y = y+((61+(90*(x-1)))*n)   
    dump.write(str(new_y) + "\n")  
    #dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
   
#########################################################

#####################################################

#69, 317, 745, 1353, 2141, 3109, 4257, 5585, 7093
#new
def dr4_ld1_79_79(x):
  y = 90*(x*x) - 22*x + 1  
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((79+(90*(x-1)))*n)
    #new2_y = y+((79+(90*(x-1)))*n)   
    dump.write(str(new_y) + "\n")  
    #dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
   
#########################################################

####################################################
#new 
#29, 239, 629, 1199, 1949, 2879, 3989, 5279, 6749, 8399
def dr2_ld9_29_91(x):
  y = 90*(x*x) - 60*x - 1 
  #print "47,91", y
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range(1, new_test):
    new_y = y+((29+(90*(x-1)))*n) 
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
#2, 122, 422, 902, 1562, 2402, 3422, 4622, 6002, 7562, 9302
def dr2_ld9_11_19(x):
  y = 90*(x*x) - 150*x + 62
  dump.write(str(y) + "\n") 
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((11+(90*(x-1)))*n)
    new2_y = y+((19+(90*(x-1)))*n)   
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
###################################################


###################################################
#19, 193, 547, 1081, 1795, 2689, 3763, 5017, 6451, 8065, 9859
#new
def dr2_ld9_37_47(x):
  y = 90*(x*x) - 96*x + 25
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((37+(90*(x-1)))*n)
    new2_y = y+((47+(90*(x-1)))*n)   
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
##################################################


##################################################
#67, 313, 739, 1345, 2131, 3097, 4243, 5569, 7075, 8761, 10627
#new 
def dr2_ld9_73_83(x):
  y = 90*(x*x) - 24*x + 1 
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((73+(90*(x-1)))*n)
    new2_y = y+((83+(90*(x-1)))*n)   
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
###################################################	  


###################################################
#3, 129, 435, 921, 1587, 2433, 3459, 4665, 6051
#new
def dr2_ld9_13_23(x):
  y = 90*(x*x) - 144*x + 57  
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((13+(90*(x-1)))*n)
    new2_y = y+((23+(90*(x-1)))*n) 
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
####################################################


####################################################
#20, 200, 560, 1100, 1820, 2720, 3800, 5060, 6500, 8120
#new
def dr2_ld9_31_59(x):
  y = 90*(x*x) - 90*x + 20
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((31+(90*(x-1)))*n) 
    new2_y = y+((59+(90*(x-1)))*n) 
    dump.write(str(new_y) + "\n")  
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
######################################################


######################################################

#22, 202, 562, 1102, 1822, 2722, 3802, 5062, 6502
#new
def dr2_ld9_41_49(x):
  y = 90*(x*x) - 90*x + 22
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((41+(90*(x-1)))*n)
    new2_y = y+((49+(90*(x-1)))*n)  
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
#############################################################


##############################################################

#57, 291, 705, 1299, 2073, 3027, 4161, 5475, 6969, 8643
#new
def dr2_ld9_67_77(x):
  y = 90*(x*x) - 36*x + 3
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((67+(90*(x-1)))*n) 
    new2_y = y+((77+(90*(x-1)))*n)
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
############################################################


########################################################
 
#1, 115, 409, 883, 1537, 2371, 3385, 4579, 5953, 7507, 9241
#new
def dr2_ld9_7_17(x):
  y = 90*(x*x) - 156*x + 67
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((7+(90*(x-1)))*n)
    new2_y = y+((17+(90*(x-1)))*n)  
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
############################################################

########################################################

#25, 211, 577, 1123, 1849, 2755, 3841, 5107, 6553, 8179
#new
def dr2_ld9_43_53(x):
  y = 90*(x*x) - 84*x + 19 
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((43+(90*(x-1)))*n) 
    new2_y = y+((53+(90*(x-1)))*n)  
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
########################################################


########################################################
#60, 300, 720, 1320, 2100, 3060, 4200, 5520, 7020, 8700
#new
def dr2_ld9_61_89(x):
  y = 90*(x*x) - 30*x 
  #print y, "61,89"
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((61+(90*(x-1)))*n)
    new2_y = y+((89+(90*(x-1)))*n) 
    #print new_y, "61"
    #print new2_y, "89"
    dump.write(str(new_y) + "\n")  
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
######################################################

#####################################################

#62, 302, 722, 1322, 2102, 3062, 4202, 5522
#new
def dr2_ld9_71_79(x):
  y = 90*(x*x) - 30*x + 2  
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((71+(90*(x-1)))*n)
    new2_y = y+((79+(90*(x-1)))*n)   
    dump.write(str(new_y) + "\n")  
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
   
#########################################################

    
for x in xrange(1, 100): 
 
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
	
    dr4_ld1_31_91(x)#
    dr4_ld1_19_49(x) #
    dr4_ld1_13_37(x) #
    dr4_ld1_67_73(x)#
    dr4_ld1_11_11(x)#
    dr4_ld1_29_29(x) #
    dr4_ld1_47_83(x)#
    dr4_ld1_17_23(x)#
    dr4_ld1_41_71(x)#
    dr4_ld1_59_89(x)#
    dr4_ld1_53_77(x)#
    dr4_ld1_7_43(x) #
    dr4_ld1_61_61(x)#
    dr4_ld1_79_79(x)#
    
    

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










