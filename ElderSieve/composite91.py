#!/usr/local/env python #python 2.7
import sys
import csv
import time
import subprocess

dump = open("composite1.csv", "w")
new_test = 40000

def dr1_ld1_91_91(x):
  y = 90*(x*x) + 2*x 
  if y > new_test:
    return
  #print "91", y
  dump.write(str(y) + "\n")
  for n in range(1, new_test):
    new_y = y+((91+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")


def dr1_ld1_19_19(x):
  y = 90*(x*x) - 142*x + 56
  if y > new_test:
    return 
  dump.write(str(y) + "\n") 
  for n in range (1, new_test):
    new_y = y+ ((19+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")


def dr1_ld1_37_73(x):
  y = 90*(x*x) - 70*x + 10
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((37+(90*(x-1)))*n)
    new2_y = y+((73+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
    
def dr1_ld1_11_41(x):
  y = 90*(x*x) - 128*x + 43
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((11+(90*(x-1)))*n)
    new2_y = y+((41+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
    
def dr1_ld1_29_59(x):
  y = 90*(x*x) - 92*x + 21 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((29+(90*(x-1)))*n)
    new2_y = y+((59+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
    
def dr1_ld1_47_23(x):
  y = 90*(x*x) - 110*x + 32
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((23+(90*(x-1)))*n) 
    new2_y = y+((47+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
    
def dr1_ld1_77_83(x):
  y = 90*(x*x) - 20*x + 1
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((77+(90*(x-1)))*n)
    new2_y = y+((83+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
    
def dr1_ld1_7_13(x):
  y = 90*(x*x) - 160*x + 71
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((7+(90*(x-1)))*n) 
    new2_y = y+((13+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
    

def dr1_ld1_31_61(x):
  y = 90*(x*x) - 88*x + 19
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((31+(90*(x-1)))*n)
    new2_y = y+((61+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
    
def dr1_ld1_49_79(x):
  y = 90*(x*x) - 52*x + 5 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((49+(90*(x-1)))*n) 
    new2_y = y+((79+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
    

def dr1_ld1_43_67(x):
  y = 90*(x*x) - 70*x + 12 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((43+(90*(x-1)))*n)
    new2_y = y+((67+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
    
def dr1_ld1_17_53(x):
  y = 90*(x*x) - 110*x + 30 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((17+(90*(x-1)))*n)
    new2_y = y+((53+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
    
def dr1_ld1_71_71(x):
  y = 90*(x*x) - 38*x + 4  
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((71+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")

    
def dr1_ld1_89_89(x):
  y = 90*(x*x) - 2*x 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((89+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")

    
for x in xrange(1, 900): #22
 
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
time.sleep(1.2) #make sure subprocess has finished

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
            print ("{} is prime".format(i))

execfile("ElderSieve.py")
