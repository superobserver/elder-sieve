#!/usr/local/env python #python 2.7
#Integration leaves residue sequence A196007
import sys
import csv
import time
import subprocess

dump = open("composite1.csv", "w")
new_test = 40000




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
            print ("{} is prime".format(i))


execfile("ElderSieve.py")









