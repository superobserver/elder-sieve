#!/usr/local/env python #python 2.7
#Integration leaves residue sequence A202115
import sys
import csv
import time
import subprocess

dump = open("composite1.csv", "w")
new_test = 40000

def dr1_ld1_91_91(x):
  y = 90*(x*x) + 1*x 
  #print "91", y
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range(1, new_test):
    new_y = y+((91+(90*(x-1)))*n)  
    dump.write(str(new_y) + "\n")
    if new_y > new_test: 
      return
    else:
      pass

def dr1_ld1_19_19(x):
  y = 90*(x*x) - 142*x + 55 
  dump.write(str(y) + "\n") 
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+ ((19+(90*(x-1)))*n)
    dump.write(str(new_y) + "\n")
    if new_y > new_test: 
      return
    else:
      pass

def dr1_ld1_37_73(x):
  y = 90*(x*x) - 70*x + 9
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((37+(90*(x-1)))*n)
    new2_y = y+((73+(90*(x-1)))*n)   
    dump.write(str(new_y) + "\n")  
    dump.write(str(new2_y) + "\n")    
    if new_y > new_test: 
      return
    else:
      pass
    
def dr1_ld1_11_41(x):
  y = 90*(x*x) - 128*x + 42
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((11+(90*(x-1)))*n)
    new2_y = y+((41+(90*(x-1)))*n)   
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
    
def dr1_ld1_29_59(x):
  y = 90*(x*x) - 92*x + 20 
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((29+(90*(x-1)))*n)
    new2_y = y+((59+(90*(x-1)))*n) 
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
    
def dr1_ld1_47_23(x):
  y = 90*(x*x) - 110*x + 31
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((23+(90*(x-1)))*n) 
    new2_y = y+((47+(90*(x-1)))*n) 
    dump.write(str(new_y) + "\n")  
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
    
def dr1_ld1_77_83(x):
  y = 90*(x*x) - 20*x + 0
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((77+(90*(x-1)))*n)
    new2_y = y+((83+(90*(x-1)))*n)  
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
    
def dr1_ld1_7_13(x):
  y = 90*(x*x) - 160*x + 70
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((7+(90*(x-1)))*n) 
    new2_y = y+((13+(90*(x-1)))*n)
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
    

def dr1_ld1_31_61(x):
  y = 90*(x*x) - 88*x + 18
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((31+(90*(x-1)))*n)
    new2_y = y+((61+(90*(x-1)))*n)  
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
    
def dr1_ld1_49_79(x):
  y = 90*(x*x) - 52*x + 4 
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((49+(90*(x-1)))*n) 
    new2_y = y+((79+(90*(x-1)))*n)  
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
    

def dr1_ld1_43_67(x):
  y = 90*(x*x) - 70*x + 11 
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((43+(90*(x-1)))*n)
    new2_y = y+((67+(90*(x-1)))*n) 
    dump.write(str(new_y) + "\n")  
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
    
def dr1_ld1_17_53(x):
  y = 90*(x*x) - 110*x + 29 
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((17+(90*(x-1)))*n)
    new2_y = y+((53+(90*(x-1)))*n)   
    dump.write(str(new_y) + "\n")  
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
    
def dr1_ld1_71_71(x):
  y = 90*(x*x) - 38*x + 3  
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((71+(90*(x-1)))*n)   
    dump.write(str(new_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
    
def dr1_ld1_89_89(x):
  y = 90*(x*x) - 2*x -1
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((89+(90*(x-1)))*n) 
    dump.write(str(new_y) + "\n")
    if new_y > new_test: 
      return
    else:
      pass
    


####################################################
#new 
#89, 359, 809, 1439, 2249, 3239, 4409, 5759, 7289, 8999
def dr8_ld9_89_91(x):
  y = 90*(x*x) - 1 
  #print "89,91", y
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range(1, new_test):
    new_y = y+((89+(90*(x-1)))*n) 
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
#14, 194, 554, 1094, 1814, 2714, 3794, 5054, 6494, 8114, 9914
def dr8_ld9_19_71(x):
  y = 90*(x*x) - 90*x + 14
  dump.write(str(y) + "\n") 
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((19+(90*(x-1)))*n)
    new2_y = y+((71+(90*(x-1)))*n)   
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
###################################################

###################################################
#6, 150, 474, 978, 1662, 2526, 3570, 4794, 6198, 7782, 9546
#new
def dr8_ld9_17_37(x):
  y = 90*(x*x) - 126*x + 42
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((17+(90*(x-1)))*n)
    new2_y = y+((37+(90*(x-1)))*n)   
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
##################################################

##################################################
#42, 258, 654, 1230, 1986, 2922, 4038, 5334, 6810, 8466
#new 
def dr8_ld9_53_73(x):
  y = 90*(x*x) - 54*x + 6
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((53+(90*(x-1)))*n)
    new2_y = y+((73+(90*(x-1)))*n)   
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
###################################################	  

###################################################
#5, 155, 485, 995, 1685, 2555, 3605, 4835, 6245, 7835, 9605
#new
def dr8_ld9_11_49(x):
  y = 90*(x*x) - 120*x + 35  
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((11+(90*(x-1)))*n)
    new2_y = y+((49+(90*(x-1)))*n) 
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
####################################################

####################################################
#9, 159, 489, 999, 1689, 2559, 3609, 4839, 6249, 7839, 9609
#new
def dr8_ld9_29_31(x):
  y = 90*(x*x) - 120*x + 39
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((29+(90*(x-1)))*n) 
    new2_y = y+((31+(90*(x-1)))*n) 
    dump.write(str(new_y) + "\n")  
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
######################################################

######################################################

#34, 238, 622, 1186, 1930, 2854, 3958, 5242, 6706, 8350
#new
def dr8_ld9_47_67(x):
  y = 90*(x*x) - 66*x + 10
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((47+(90*(x-1)))*n)
    new2_y = y+((67+(90*(x-1)))*n)  
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
#############################################################

##############################################################

#11, 197, 563, 1109, 1835, 2741, 3827, 5093, 6539, 8165, 9971
#new
def dr8_ld9_13_83(x):
  y = 90*(x*x) - 84*x + 5 
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((13+(90*(x-1)))*n) 
    new2_y = y+((83+(90*(x-1)))*n)
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
############################################################

########################################################
 
#10, 166, 502, 1018, 1714, 2590, 3646, 4882, 6298, 7894, 9670
#new
def dr8_ld9_23_43(x):
  y = 90*(x*x) - 114*x + 34 
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((23+(90*(x-1)))*n)
    new2_y = y+((43+(90*(x-1)))*n)  
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
############################################################

########################################################

#35, 245, 635, 1205, 1955, 2885, 3995, 5285, 6755, 8405
#new
def dr8_ld9_41_79(x):
  y = 90*(x*x) - 60*x + 5
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((41+(90*(x-1)))*n) 
    new2_y = y+((79+(90*(x-1)))*n)  
    dump.write(str(new_y) + "\n")   
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
########################################################

########################################################
#39, 249, 639, 1209, 1959, 2889, 3999, 5289, 6759, 8409
#new
def dr8_ld9_59_61(x):
  y = 90*(x*x) - 60*x + 9
  #print y, "59,61"
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((59+(90*(x-1)))*n)
    new2_y = y+((61+(90*(x-1)))*n) 
    #print new_y, "59"
    #print new2_y, "61"
    dump.write(str(new_y) + "\n")  
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
######################################################

#####################################################

#5, 179, 533, 1067, 1781, 2675, 3749, 5003, 6437, 8051, 9845
#new
def dr8_ld9_7_77(x):
  y = 90*(x*x) - 96*x + 11
  dump.write(str(y) + "\n")
  if y > new_test:
    return
  for n in range (1, new_test):
    new_y = y+((7+(90*(x-1)))*n)
    new2_y = y+((77+(90*(x-1)))*n)   
    dump.write(str(new_y) + "\n")  
    dump.write(str(new2_y) + "\n") 
    if new_y > new_test: 
      return
    else:
      pass
   
#########################################################

for x in xrange(1, 100): 
 
    dr8_ld9_89_91(x)#  
    dr8_ld9_19_71(x)# 
    dr8_ld9_17_37(x)# 
    dr8_ld9_53_73(x)# 
    dr8_ld9_11_49(x)# 
    dr8_ld9_29_31(x)# 
    dr8_ld9_47_67(x)# 
    dr8_ld9_13_83(x)# 
    dr8_ld9_23_43(x)# 
    dr8_ld9_41_79(x)# 
    dr8_ld9_59_61(x)# 
    dr8_ld9_7_77(x)# 

    dr1_ld1_7_13(x) #1 @xrange(x) = 22, y = 1814 
    dr1_ld1_19_19(x) #4 
    dr1_ld1_11_41(x) #5 
    dr1_ld1_17_53(x) #10
    dr1_ld1_47_23(x) #12
    dr1_ld1_29_59(x) #19
    dr1_ld1_31_61(x) #21
    dr1_ld1_37_73(x) #30
    dr1_ld1_43_67(x) #32 
    dr1_ld1_49_79(x) #43
    dr1_ld1_71_71(x) #56
    dr1_ld1_77_83(x) #71
    dr1_ld1_89_89(x) #88
    dr1_ld1_91_91(x) #92
    

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










