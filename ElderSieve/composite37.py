#!/usr/local/env python #python 2.7
#Integration leaves residue sequence A198382

import sys
import csv
import time
import subprocess

dump = open("composite1.csv", "w")
new_test = 40000



#37, 255, 653, 1231, 1989, 2927, 4045, 5343
#done/done
def dr1_ld1_37_91(x): #37
  y = 90*(x*x) - 52*x - 1 
  if y > new_test:
    return
  #print "37,91", y
  dump.write(str(y) + "\n")
  for n in range(1, new_test):
    new_y = y+((37+(90*(x-1)))*n)
    new2_y = y+((91+(90*(x-1)))*n)
    #print new_y, "37"
    #print new2_y, "91"  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")


#15, 197, 559, 1101, 1823, 2725, 3807, 5069
#new/done
def dr1_ld1_19_73(x):
  y = 90*(x*x) - 88*x + 13 
  if y > new_test:
    return
  dump.write(str(y) + "\n") 
  for n in range (1, new_test):
    new_y = y+ ((19+(90*(x-1)))*n)
    new2_y = y+ ((73+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")


#9, 187, 545, 1083, 1801, 2699, 3777, 5035, 6473
#new/done
def dr1_ld1_11_77(x):
  y = 90*(x*x) - 92*x + 11
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((11+(90*(x-1)))*n)
    new2_y = y+((77+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")


#7, 149, 471, 973, 1655, 2517, 3559, 4781, 6183, 7765, 9527
#new/done
def dr1_ld1_23_29(x):
  y = 90*(x*x) - 128*x + 45
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((23+(90*(x-1)))*n)
    new2_y = y+((29+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")

#21, 199, 557, 1095, 1813, 2711, 3789, 5047, 6485, 8103
#new/done
def dr1_ld1_41_47(x):
  y = 90*(x*x) - 92*x + 23
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((41+(90*(x-1)))*n)
    new2_y = y+((47+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")



#54, 286, 698, 1290, 2062, 3014, 4146, 5458, 6950, 8622
#new/done
def dr1_ld1_59_83(x):
  y = 90*(x*x) - 38*x + 2
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((59+(90*(x-1)))*n) 
    new2_y = y+((83+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")

#11, 193, 555, 1097, 1819, 2721, 3803, 5065, 5607
#new/done
def dr1_ld1_13_79(x):
  y = 90*(x*x) - 88*x + 9
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((13+(90*(x-1)))*n)
    new2_y = y+((79+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")


#2, 130, 438, 926, 1594, 2442, 3470, 4678, 6066, 7634
#new/done
def dr1_ld1_7_31(x):
  y = 90*(x*x) - 142*x + 54
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((7+(90*(x-1)))*n) 
    new2_y = y+((31+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")


#23, 205, 567, 1109, 1831, 2733, 3815, 5077, 6519, 8141, 9943
#new/done
def dr1_ld1_43_49(x):
  y = 90*(x*x) - 88*x + 21
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((43+(90*(x-1)))*n)
    new2_y = y+((49+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")


#45, 263, 661, 1239, 1997, 2935, 4053, 5351, 6829, 8487
#new/done
def dr1_ld1_61_67(x):
  y = 90*(x*x) - 52*x + 7
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((61+(90*(x-1)))*n) 
    new2_y = y+((67+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")


#13, 191, 549, 1087, 1805, 2703, 3781, 5039, 6477
#new/done
def dr1_ld1_17_71(x):
  y = 90*(x*x) - 92*x + 15 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((17+(90*(x-1)))*n)
    new2_y = y+((71+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")


#52, 284, 696, 1288, 2060, 3012, 4144, 5456, 6948, 8620
#new/done
def dr1_ld1_53_89(x):
  y = 90*(x*x) - 38*x
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((53+(90*(x-1)))*n)
    new2_y = y+((89+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")

    
for x in xrange(1, 202): 
    dr1_ld1_37_91(x) #done
    dr1_ld1_19_73(x) #done
    dr1_ld1_11_77(x) #done
    dr1_ld1_23_29(x) #done
    dr1_ld1_41_47(x) #done 
    dr1_ld1_59_83(x) #done 
    dr1_ld1_13_79(x) #done
    dr1_ld1_7_31(x) #done 
    dr1_ld1_43_49(x) #done 
    dr1_ld1_61_67(x) #done 
    dr1_ld1_17_71(x) #done 
    dr1_ld1_53_89(x) #done



def bash_command(cmd):
    subprocess.Popen(cmd, shell=True)
bash_command('sort -n composite1.csv -o composite2.csv')
time.sleep(1.2) #make sure subprocess has finished

z=200
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
            print ("{} is prime".format(i))


execfile("ElderSieve.py")


