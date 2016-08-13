#!/usr/local/env python #python 2.7
#Integration leaves residue sequence A202115
import sys
import csv
import time
import subprocess

dump = open("composite1.csv", "w")
new_test = 40000



# dr1_ld1_19_91(x) #done 
#19, 219, 599, 1159, 1899, 2819, 3919, 5199, 6659
#new
def dr1_ld1_19_91(x):
  y = 90*(x*x) - 70*x - 1 
  #print "19,91", y
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range(1, new_test):
    new_y = y+((19+(90*(x-1)))*n) 
    new2_y = y+((91+(90*(x-1)))*n) 
    dump.write(str(new_y) + "\n")
    dump.write(str(new2_y) + "\n")
    if new_y > new_test: 
      return
    else:
      pass


#15, 179, 523, 1047, 1751, 2635, 3699, 4943, 6367, 7971
#new
def dr1_ld1_37_37(x):
  y = 90*(x*x) - 106*x + 31
  dump.write(str(y) + "\n") 
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+ ((37+(90*(x-1)))*n)
    dump.write(str(new_y) + "\n")
    if new_y > new_test: 
      return
    else:
      pass



#59, 295, 711, 1307, 2083, 3039, 4175, 5491, 6987, 8663
#new
def dr1_ld1_73_73(x):
  y = 90*(x*x) - 34*x + 3
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((73+(90*(x-1)))*n) 
    dump.write(str(new_y) + "\n")      
    if new_y > new_test: 
      return
    else:
      pass
  
#7, 167, 507, 1027, 1727, 2607, 3667, 4907, 6327, 7927
#new 
def dr1_ld1_11_59(x):
  y = 90*(x*x) - 110*x + 27 
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((11+(90*(x-1)))*n)
    new2_y = y+((59+(90*(x-1)))*n)   
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
   

#13, 173, 513, 1033, 1733, 2613, 3673, 4913, 6333, 7933
#new
def dr1_ld1_29_41(x):
  y = 90*(x*x) - 110*x + 33  
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((29+(90*(x-1)))*n)
    new2_y = y+((41+(90*(x-1)))*n) 
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass

#40, 254, 648, 1222, 1976, 2910, 4024, 5318, 6792, 8446
#new
def dr1_ld1_47_77(x):
  y = 90*(x*x) - 56*x + 6
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((47+(90*(x-1)))*n) 
    new2_y = y+((77+(90*(x-1)))*n) 
    dump.write(str(new_y) + "\n")  
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
    
#21, 217, 593, 1149, 1885, 2801, 3897, 5173, 6629, 8265
#new
def dr1_ld1_23_83(x):
  y = 90*(x*x) - 74*x + 5
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((23+(90*(x-1)))*n)
    new2_y = y+((83+(90*(x-1)))*n)  
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass

6, 152, 478, 984, 1670, 2536, 3582, 4808, 6214
#new
def dr1_ld1_13_43(x):
  y = 90*(x*x) - 124*x + 40
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((13+(90*(x-1)))*n) 
    new2_y = y+((43+(90*(x-1)))*n)
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
    
#27, 227, 607, 1167, 1907, 2827, 3927, 5207, 6667
#new
def dr1_ld1_31_79(x):
  y = 90*(x*x) - 70*x + 7
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((31+(90*(x-1)))*n)
    new2_y = y+((79+(90*(x-1)))*n)  
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass

#33, 233, 613, 1173, 1913, 2833, 3933, 5213
#new
def dr1_ld1_49_61(x):
  y = 90*(x*x) - 70*x + 13 
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((49+(90*(x-1)))*n) 
    new2_y = y+((61+(90*(x-1)))*n)  
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass

#5, 169, 513, 1037, 1741, 2625, 3689, 4933, 6357
#new
def dr1_ld1_7_67(x):
  y = 90*(x*x) - 106*x + 21 
  #print y, "7,67"
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((7+(90*(x-1)))*n)
    new2_y = y+((67+(90*(x-1)))*n) 
    #print new_y, "7"
    #print new2_y, "67"
    dump.write(str(new_y) + "\n")  
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
   

#70, 320, 750, 1360, 2150, 3120, 4270, 5600, 7110, 8800
#new
def dr1_ld1_71_89(x):
  y = 90*(x*x) - 20*x  
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((71+(90*(x-1)))*n)
    new2_y = y+((89+(90*(x-1)))*n)   
    dump.write(str(new_y) + "\n")  
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
   



#31, 227, 603, 1159, 1895, 2811, 3907, 5183, 6639
#new
def dr1_ld1_53_53(x):
  y = 90*(x*x) - 74*x + 15  
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((53+(90*(x-1)))*n)   
    dump.write(str(new_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
    
#3, 127, 431, 915, 1579, 2423, 3447, 4651, 6035
#new
def dr1_ld1_17_17(x):
  y = 90*(x*x) - 146*x + 59
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((17+(90*(x-1)))*n) 
    dump.write(str(new_y) + "\n")
    if new_y > new_test: 
      return
    else:
      pass







####################################################
#new 
#17, 215, 593, 1151, 1889, 2807, 3905, 5183, 6641, 8279, 10097
def dr8_ld7_17_91(x):
  y = 90*(x*x) - 72*x - 1 
  #print "71,91", y
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range(1, new_test):
    new_y = y+((17+(90*(x-1)))*n) 
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
#11, 173, 515, 1037, 1739, 2621, 3683, 4925, 6347, 7949, 9731
def dr8_ld7_19_53(x):
  y = 90*(x*x) - 108*x + 29
  dump.write(str(y) + "\n") 
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((19+(90*(x-1)))*n)
    new2_y = y+((53+(90*(x-1)))*n)   
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
###################################################

###################################################
#29, 227, 605, 1163, 1901, 2819, 3917, 5195, 6653, 8291
#new
def dr8_ld7_37_71(x):
  y = 90*(x*x) - 72*x + 11
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((37+(90*(x-1)))*n)
    new2_y = y+((71+(90*(x-1)))*n)   
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
##################################################

##################################################
#72, 324, 756, 1368, 2160, 3132, 4284, 5616, 7128, 8820
#new 
def dr8_ld7_73_89(x):
  y = 90*(x*x) - 18*x 
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((73+(90*(x-1)))*n)
    new2_y = y+((89+(90*(x-1)))*n)   
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
###################################################	  

###################################################
#8, 176, 524, 1052, 1760, 2648, 3716, 4964, 6392, 8000, 9788
#new
def dr8_ld7_11_67(x):
  y = 90*(x*x) - 102*x + 20  
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((11+(90*(x-1)))*n)
    new2_y = y+((67+(90*(x-1)))*n) 
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
####################################################

####################################################
#21, 207, 573, 1119, 1845, 2751, 3837, 5103, 6549, 8175, 9981
#new
def dr8_ld7_13_29(x):
  y = 90*(x*x) - 138*x + 52
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((13+(90*(x-1)))*n) 
    new2_y = y+((29+(90*(x-1)))*n) 
    dump.write(str(new_y) + "\n")  
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
######################################################

######################################################

#16, 184, 532, 1060, 1768, 2656, 3724, 4972, 6400, 8008, 9796
#new
def dr8_ld7_31_47(x):
  y = 90*(x*x) - 102*x + 28
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((31+(90*(x-1)))*n)
    new2_y = y+((47+(90*(x-1)))*n)  
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
#############################################################

##############################################################

#45, 267, 669, 1251, 2013, 2955, 4077, 5379, 6861, 8523
#new
def dr8_ld7_49_83(x):
  y = 90*(x*x) - 48*x + 3 
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((49+(90*(x-1)))*n) 
    new2_y = y+((83+(90*(x-1)))*n)
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
############################################################

########################################################
 
#20, 212, 584, 1136, 1868, 2780, 3872, 5144, 6596, 8228, 10040
#new
def dr8_ld7_23_79(x):
  y = 90*(x*x) - 78*x + 8 
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((23+(90*(x-1)))*n)
    new2_y = y+((79+(90*(x-1)))*n)  
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
############################################################

########################################################

#3, 141, 459, 957, 1635, 2493, 3531, 4749, 6147, 7725, 9483
#new
def dr8_ld7_7_41(x):
  y = 90*(x*x) - 132*x + 45
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((7+(90*(x-1)))*n) 
    new2_y = y+((41+(90*(x-1)))*n)  
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
########################################################

########################################################
#28, 220, 592, 1144, 1876, 2788, 3880, 5152, 6604, 8236, 10048
#new
def dr8_ld7_43_59(x):
  y = 90*(x*x) - 78*x + 16
  #print y, "7,59"
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((43+(90*(x-1)))*n)
    new2_y = y+((59+(90*(x-1)))*n) 
    #print new_y, "7"
    #print new2_y, "59"
    dump.write(str(new_y) + "\n")  
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
######################################################

#####################################################

#52, 280, 688, 1276, 2044, 2992, 4120, 5428, 6916, 8584
#new
def dr8_ld7_61_77(x):
  y = 90*(x*x) - 42*x + 4
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((61+(90*(x-1)))*n)
    new2_y = y+((77+(90*(x-1)))*n)   
    dump.write(str(new_y) + "\n")  
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
   
#########################################################

for x in xrange(1, 100): 
 
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
    
    dr1_ld1_17_17(x) #3
    dr1_ld1_7_67(x)  #5
    dr1_ld1_13_43(x) #6
    dr1_ld1_11_59(x) #7
    dr1_ld1_29_41(x) #13
    dr1_ld1_37_37(x) #15
    dr1_ld1_19_91(x) #19
    dr1_ld1_23_83(x) #21
    dr1_ld1_31_79(x) #27
    dr1_ld1_53_53(x) #31
    dr1_ld1_49_61(x) #33
    dr1_ld1_47_77(x) #40
    dr1_ld1_73_73(x) #59    
    dr1_ld1_71_89(x) #70
    

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










