#!/usr/local/env python #python 2.7
#Integration leaves residue sequence A201816
import sys
import csv
import time
import subprocess

dump = open("composite1.csv", "w")
new_test = 40000



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

    
for x in xrange(1, 100): 
 
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
            print ("{} is sexy prime".format(i))

execfile("ElderSieve.py")










