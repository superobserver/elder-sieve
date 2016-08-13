#!/usr/local/env python #python 2.7
#Integration leaves residue sequence A196000
import sys
import csv
import time
import subprocess

dump = open("composite1.csv", "w")
new_test = 40000

#find 131


# dr1_ld1_19_91(x) #done 
#19, 219, 599, 1159, 1899, 2819, 3919, 5199, 6659
#new
def dr1_ld1_19_91(x):
  y = 90*(x*x) - 70*x - 1 
  if y > new_test:
    return
  #print "19,91", y
  dump.write(str(y) + "\n")
  for n in range(1, new_test):
    new_y = y+((19+(90*(x-1)))*n) 
    new2_y = y+((91+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")


#15, 179, 523, 1047, 1751, 2635, 3699, 4943, 6367, 7971
#new
def dr1_ld1_37_37(x):
  y = 90*(x*x) - 106*x + 31
  if y > new_test:
    return
  dump.write(str(y) + "\n") 
  for n in range (1, new_test):
    new_y = y+ ((37+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")




#59, 295, 711, 1307, 2083, 3039, 4175, 5491, 6987, 8663
#new
def dr1_ld1_73_73(x):
  y = 90*(x*x) - 34*x + 3
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((73+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")

  
#7, 167, 507, 1027, 1727, 2607, 3667, 4907, 6327, 7927
#new 
def dr1_ld1_11_59(x):
  y = 90*(x*x) - 110*x + 27 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((11+(90*(x-1)))*n)
    new2_y = y+((59+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
   

#13, 173, 513, 1033, 1733, 2613, 3673, 4913, 6333, 7933
#new
def dr1_ld1_29_41(x):
  y = 90*(x*x) - 110*x + 33  
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((29+(90*(x-1)))*n)
    new2_y = y+((41+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")

#40, 254, 648, 1222, 1976, 2910, 4024, 5318, 6792, 8446
#new
def dr1_ld1_47_77(x):
  y = 90*(x*x) - 56*x + 6
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((47+(90*(x-1)))*n) 
    new2_y = y+((77+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
    
#21, 217, 593, 1149, 1885, 2801, 3897, 5173, 6629, 8265
#new
def dr1_ld1_23_83(x):
  y = 90*(x*x) - 74*x + 5
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((23+(90*(x-1)))*n)
    new2_y = y+((83+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")

#6, 152, 478, 984, 1670, 2536, 3582, 4808, 6214
#new
def dr1_ld1_13_43(x):
  y = 90*(x*x) - 124*x + 40
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((13+(90*(x-1)))*n) 
    new2_y = y+((43+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
    
#27, 227, 607, 1167, 1907, 2827, 3927, 5207, 6667
#new
def dr1_ld1_31_79(x):
  y = 90*(x*x) - 70*x + 7
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((31+(90*(x-1)))*n)
    new2_y = y+((79+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")

#33, 233, 613, 1173, 1913, 2833, 3933, 5213
#new
def dr1_ld1_49_61(x):
  y = 90*(x*x) - 70*x + 13 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((49+(90*(x-1)))*n) 
    new2_y = y+((61+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")

#5, 169, 513, 1037, 1741, 2625, 3689, 4933, 6357
#new
def dr1_ld1_7_67(x):
  y = 90*(x*x) - 106*x + 21 
  if y > new_test:
    return
  #print y, "7,67"
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((7+(90*(x-1)))*n)
    new2_y = y+((67+(90*(x-1)))*n) 
    #print new_y, "7"
    #print new2_y, "67"
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
   

#70, 320, 750, 1360, 2150, 3120, 4270, 5600, 7110, 8800
#new
def dr1_ld1_71_89(x):
  y = 90*(x*x) - 20*x  
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((71+(90*(x-1)))*n)
    new2_y = y+((89+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
   



#31, 227, 603, 1159, 1895, 2811, 3907, 5183, 6639
#new
def dr1_ld1_53_53(x):
  y = 90*(x*x) - 74*x + 15  
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((53+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")

    
#3, 127, 431, 915, 1579, 2423, 3447, 4651, 6035
#new
def dr1_ld1_17_17(x):
  y = 90*(x*x) - 146*x + 59
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((17+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")



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
    
for x in xrange(1, 100): 
 
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

#run this code to compare to https://oeis.org/A181732/b181732.txt
with open("composite2.csv") as f:
    rd=f.readlines()
    x=[t.strip("\n") for t in rd]
    for i in range(0, 37188):
        if str(i) not in x:
            print ("{} is cousin prime".format(i))


execfile("ElderSieve.py")

