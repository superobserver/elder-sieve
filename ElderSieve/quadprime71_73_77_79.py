#!/usr/local/env python #python 2.7
#Integration leaves residue sequence A202129
import sys
import csv
import time
import subprocess

dump = open("composite1.csv", "w")
new_test = 40000



####################################################
#new 
#71, 323, 755, 1367, 2159, 3131, 4283, 5615, 7127, 8819
def dr8_ld1_71_91(x):
  y = 90*(x*x) - 18*x - 1 
  if y > new_test:
    return
  #print "71,91", y
  dump.write(str(y) + "\n")
  for n in range(1, new_test):
    new_y = y+((71+(90*(x-1)))*n) 
    new2_y = y+((91+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################

###################################################
#new
#18, 216, 594, 1152, 1890, 2808, 3906, 5184, 6642, 8280, 10098
def dr8_ld1_19_89(x):
  y = 90*(x*x) - 72*x 
  if y > new_test:
    return
  dump.write(str(y) + "\n") 
  for n in range (1, new_test):
    new_y = y+((19+(90*(x-1)))*n)
    new2_y = y+((89+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################

###################################################
#21, 201, 561, 1101, 1821, 2721, 3801, 5061, 6501, 8121, 9921
#new
def dr8_ld1_37_53(x):
  y = 90*(x*x) - 90*x + 21
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((37+(90*(x-1)))*n)
    new2_y = y+((53+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
##################################################

##################################################
#13, 193, 553, 1093, 1813, 2713, 3793, 5053, 6493, 8113, 9913
#new 
def dr8_ld1_17_73(x):
  y = 90*(x*x) - 90*x + 13
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((17+(90*(x-1)))*n)
    new2_y = y+((73+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################	  

###################################################
#13, 135, 447, 939, 1611, 2463, 3495, 4707, 6099, 7671, 9423
#new
def dr8_ld1_11_31(x):
  y = 90*(x*x) - 138*x + 51  
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((11+(90*(x-1)))*n)
    new2_y = y+((31+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
####################################################

####################################################
#15, 183, 531, 1059, 1767, 2655, 3723, 4971, 6399, 8007, 9795
#new
def dr8_ld1_29_49(x):
  y = 90*(x*x) - 102*x + 27
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((29+(90*(x-1)))*n) 
    new2_y = y+((49+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
######################################################

######################################################

#6, 156, 486, 996, 1686, 2556, 3606, 4836, 6246, 7836, 9606
#new
def dr8_ld1_13_47(x):
  y = 90*(x*x) - 120*x + 36
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((13+(90*(x-1)))*n)
    new2_y = y+((47+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
#############################################################

##############################################################

#61, 301, 721, 1321, 2101, 3061, 4201, 5521, 7021, 8701
#new
def dr8_ld1_67_83(x):
  y = 90*(x*x) - 30*x + 1 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((67+(90*(x-1)))*n) 
    new2_y = y+((83+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
############################################################

########################################################
 
#1, 121, 421, 901, 1561, 2401, 3421, 4621, 6001, 7561, 9301
#new
def dr8_ld1_7_23(x):
  y = 90*(x*x) - 150*x + 61 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((7+(90*(x-1)))*n)
    new2_y = y+((23+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
############################################################

########################################################

#27, 219, 591, 1143, 1875, 2787, 3879, 5151, 6603, 8235, 10047
#new
def dr8_ld1_41_61(x):
  y = 90*(x*x) - 78*x + 15
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((41+(90*(x-1)))*n) 
    new2_y = y+((61+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
########################################################

########################################################
#51, 279, 687, 1275, 2043, 2991, 4119, 5427, 6915, 8583
#new
def dr8_ld1_59_79(x):
  y = 90*(x*x) - 42*x + 3
  if y > new_test:
    return
  #print y, "59,79"
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((59+(90*(x-1)))*n)
    new2_y = y+((79+(90*(x-1)))*n) 
    #print new_y, "59"
    #print new2_y, "79"
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
######################################################

#####################################################

#36, 246, 636, 1206, 1956, 2886, 3996, 5286, 6756, 8406
#new
def dr8_ld1_43_77(x):
  y = 90*(x*x) - 60*x + 6
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((43+(90*(x-1)))*n)
    new2_y = y+((77+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
   
#########################################################

def dr1_ld1_73_91(x):
  y = 90*(x*x) - 16*x - 1 
  if y > new_test:
    return
  #print "73,91", y
  dump.write(str(y) + "\n")
  for n in range(1, new_test):
    new_y = y+((73+(90*(x-1)))*n)
    new2_y = y+((91+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")


def dr1_ld1_19_37(x):
  y = 90*(x*x) - 124*x + 41 
  if y > new_test:
    return
  dump.write(str(y) + "\n") 
  for n in range (1, new_test):
    new_y = y+ ((19+(90*(x-1)))*n)
    new2_y = y+ ((37+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")


def dr1_ld1_11_23(x):
  y = 90*(x*x) - 146*x + 58
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((11+(90*(x-1)))*n)
    new2_y = y+((23+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")



def dr1_ld1_29_77(x):
  y = 90*(x*x) - 74*x + 8
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((29+(90*(x-1)))*n)
    new2_y = y+((77+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")


def dr1_ld1_47_59(x):
  y = 90*(x*x) - 74*x + 14
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((47+(90*(x-1)))*n)
    new2_y = y+((59+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")


def dr1_ld1_41_83(x):
  y = 90*(x*x) - 56*x + 3
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((41+(90*(x-1)))*n) 
    new2_y = y+((83+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")



def dr1_ld1_13_61(x):
  y = 90*(x*x) - 106*x + 24
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((13+(90*(x-1)))*n)
    new2_y = y+((61+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")


def dr1_ld1_31_43(x):
  y = 90*(x*x) - 106*x + 30
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((31+(90*(x-1)))*n) 
    new2_y = y+((43+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")


def dr1_ld1_7_49(x):
  y = 90*(x*x) - 124*x + 37
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((7+(90*(x-1)))*n)
    new2_y = y+((49+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")



def dr1_ld1_67_79(x):
  y = 90*(x*x) - 34*x + 2
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((67+(90*(x-1)))*n) 
    new2_y = y+((79+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")


def dr1_ld1_17_89(x):
  y = 90*(x*x) - 74*x 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((17+(90*(x-1)))*n)
    new2_y = y+((89+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")

def dr1_ld1_53_71(x):
  y = 90*(x*x) - 56*x + 7
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((53+(90*(x-1)))*n)
    new2_y = y+((71+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")


####################################################
#new 
#77, 335, 773, 1391, 2189, 3167, 4325, 5663, 7181, 8879
def dr5_ld7_77_91(x):
  y = 90*(x*x) - 12*x - 1 
  if y > new_test:
    return
  #print "49,89", y
  dump.write(str(y) + "\n")
  for n in range(1, new_test):
    new_y = y+((77+(90*(x-1)))*n) 
    new2_y = y+((91+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################

###################################################
#new
#4, 136, 448, 940, 1612, 2464, 3496, 4708, 6100, 7672, 9424
def dr5_ld7_19_23(x):
  y = 90*(x*x) - 138*x + 52
  if y > new_test:
    return
  dump.write(str(y) + "\n") 
  for n in range (1, new_test):
    new_y = y+((19+(90*(x-1)))*n)
    new2_y = y+((23+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################

###################################################
#16, 184, 532, 1060, 1768, 2656, 3724, 4972, 6400, 8008, 9796
#new
def dr5_ld7_37_41(x):
  y = 90*(x*x) - 102*x + 28
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((37+(90*(x-1)))*n)
    new2_y = y+((41+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
##################################################

##################################################
#47, 269, 671, 1253, 2015, 2957, 4079, 5381, 6863, 8525
#new 
def dr5_ld7_59_73(x):
  y = 90*(x*x) - 48*x + 5 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((59+(90*(x-1)))*n)
    new2_y = y+((73+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################	  

###################################################
#0, 108, 396, 864, 1512, 2340, 3348, 4536, 5904, 7452, 9180
#new
def dr5_ld7_7_11(x):
  y = 90*(x*x) - 162*x + 72  
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((7+(90*(x-1)))*n)
    new2_y = y+((11+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
####################################################

####################################################
#13, 175, 517, 1039, 1741, 2623, 3685, 4927, 6349, 7951, 9733
#new
def dr5_ld7_29_43(x):
  y = 90*(x*x) - 108*x + 31
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((29+(90*(x-1)))*n) 
    new2_y = y+((43+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
######################################################

######################################################

#31, 229, 607, 1165, 1903, 2821, 3919, 5197, 6655, 8293
#new
def dr5_ld7_47_61(x):
  y = 90*(x*x) - 72*x + 13
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((47+(90*(x-1)))*n)
    new2_y = y+((61+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
#############################################################

##############################################################

#72, 324, 756, 1368, 2160, 3132, 4284, 5616, 7128, 8820
#new
def dr5_ld7_79_83(x):
  y = 90*(x*x) - 18*x 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((79+(90*(x-1)))*n) 
    new2_y = y+((83+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
############################################################

########################################################
 
#12, 204, 576, 1128, 1860, 2772, 3864, 5136, 6588, 8220
#new
def dr5_ld7_13_89(x):
  y = 90*(x*x) - 78*x 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((13+(90*(x-1)))*n)
    new2_y = y+((89+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
############################################################

########################################################

#5, 143, 461, 959, 1637, 2495, 3533, 4751, 6149, 7727, 9485
#new
def dr5_ld7_17_31(x):
  y = 90*(x*x) - 132*x + 47 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((17+(90*(x-1)))*n) 
    new2_y = y+((31+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
########################################################

########################################################
#28, 220, 592, 1144, 1876, 2788, 3880, 5152, 6604, 8236
#new
def dr5_ld7_49_53(x):
  y = 90*(x*x) - 78*x + 16
  if y > new_test:
    return
  #print y, "49,53"
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((49+(90*(x-1)))*n)
    new2_y = y+((53+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
######################################################

#####################################################

#52, 280, 688, 1276, 2044, 2992, 4120, 5428, 6916, 8584
#new
def dr5_ld7_67_71(x):
  y = 90*(x*x) - 42*x + 4
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((67+(90*(x-1)))*n)
    new2_y = y+((71+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
   
#########################################################

####################################################
#new 
#79, 339, 779, 1399, 2199, 3179, 4339, 5679, 7199, 8899
def dr7_ld9_79_91(x):
  y = 90*(x*x) - 10*x - 1 
  if y > new_test:
    return
  #print "7w,91", y
  dump.write(str(y) + "\n")
  for n in range(1, new_test):
    new_y = y+((79+(90*(x-1)))*n) 
    new2_y = y+((91+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################

###################################################
#new
#12, 182, 532, 1062, 1772, 2662, 3732, 4982, 6412, 8022, 9812
def dr7_ld9_19_61(x):
  y = 90*(x*x) - 100*x + 22
  if y > new_test:
    return
  dump.write(str(y) + "\n") 
  for n in range (1, new_test):
    new_y = y+((19+(90*(x-1)))*n)
    new2_y = y+((61+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################

###################################################
#2, 136, 450, 944, 1618, 2472, 3506, 4720, 6114, 7688, 9442
#new
def dr7_ld9_7_37(x):
  y = 90*(x*x) - 136*x + 48
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((7+(90*(x-1)))*n)
    new2_y = y+((37+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
##################################################

##################################################
#34, 240, 626, 1192, 1938, 2864, 3970, 5256, 6722, 8368
#new 
def dr7_ld9_43_73(x):
  y = 90*(x*x) - 64*x + 8
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((43+(90*(x-1)))*n)
    new2_y = y+((73+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################	  

###################################################
#10, 200, 570, 1120, 1850, 2760, 3850, 5120, 6570, 8200
#new
def dr7_ld9_11_89(x):
  y = 90*(x*x) - 80*x  
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((11+(90*(x-1)))*n)
    new2_y = y+((89+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
####################################################

####################################################
#22, 212, 582, 1132, 1862, 2772, 3862, 5132, 6582, 8212
#new
def dr7_ld9_29_71(x):
  y = 90*(x*x) - 80*x + 12
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((29+(90*(x-1)))*n) 
    new2_y = y+((71+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
######################################################

######################################################

#8, 162, 496, 1010, 1704, 2578, 3632, 4866, 6280, 7874, 9648
#new
def dr7_ld9_17_47(x):
  y = 90*(x*x) - 116*x + 34
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((17+(90*(x-1)))*n)
    new2_y = y+((47+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
#############################################################

##############################################################

#48, 274, 680, 1266, 2032, 2978, 4104, 5410, 6896, 8562
#new
def dr7_ld9_53_83(x):
  y = 90*(x*x) - 44*x + 2 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((53+(90*(x-1)))*n) 
    new2_y = y+((83+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
############################################################

########################################################
 
#1, 117, 413, 889, 1545, 2381, 3397, 4593, 5969, 7525, 9261
#new
def dr7_ld9_13_13(x):
  y = 90*(x*x) - 154*x + 65 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((13+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")

############################################################

########################################################

#16, 186, 536, 1066, 1776, 2666, 3736, 4986, 6416, 8026, 9816
#new
def dr7_ld9_31_49(x):
  y = 90*(x*x) - 100*x + 26
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((31+(90*(x-1)))*n) 
    new2_y = y+((49+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
########################################################

########################################################
#49, 273, 677, 1261, 2025, 2969, 4093, 5397, 6881, 8545
#new
def dr7_ld9_67_67(x):
  y = 90*(x*x) - 46*x + 5
  if y > new_test:
    return
  #print y, "67,67"
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((67+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")

######################################################

#####################################################

#5, 141, 457, 953, 1629, 2485, 3521, 4737, 6133, 7709, 9465
#new
def dr7_ld9_23_23(x):
  y = 90*(x*x) - 134*x + 49
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((23+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
   
#########################################################

#####################################################

#26, 216, 586, 1136, 1866, 2776, 3866, 5136, 6586, 8216, 10026
#new
def dr7_ld9_41_59(x):
  y = 90*(x*x) - 80*x + 16
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((41+(90*(x-1)))*n)
    new2_y = y+((59+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
   
#########################################################

#####################################################

#65, 309, 733, 1337, 2121, 3085, 4229, 5553, 7057, 8741
#new
def dr7_ld9_77_77(x):
  y = 90*(x*x) - 26*x + 1
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((77+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
   
#########################################################



for x in xrange(1, 100): 
 
    dr8_ld1_71_91(x)#  
    dr8_ld1_19_89(x)# 
    dr8_ld1_37_53(x)# 
    dr8_ld1_17_73(x)# 
    dr8_ld1_11_31(x)# 
    dr8_ld1_29_49(x)# 
    dr8_ld1_13_47(x)# 
    dr8_ld1_67_83(x)# 
    dr8_ld1_7_23(x)# 
    dr8_ld1_41_61(x)# 
    dr8_ld1_59_79(x)# 
    dr8_ld1_43_77(x)# 

    dr1_ld1_11_23(x) #2
    dr1_ld1_7_49(x)  #3
    dr1_ld1_19_37(x) #7
    dr1_ld1_13_61(x) #8
    dr1_ld1_31_43(x) #14 
    dr1_ld1_17_89(x) #16 
    dr1_ld1_29_77(x) #24
    dr1_ld1_47_59(x) #30 
    dr1_ld1_41_83(x) #37 
    dr1_ld1_53_71(x) #41 
    dr1_ld1_67_79(x) #58 
    dr1_ld1_73_91(x) #73

 
    dr5_ld7_77_91(x)#
    dr5_ld7_19_23(x)#
    dr5_ld7_37_41(x) #
    dr5_ld7_59_73(x)#
    dr5_ld7_7_11(x)#
    dr5_ld7_29_43(x)#
    dr5_ld7_47_61(x)#
    dr5_ld7_79_83(x)#
    dr5_ld7_13_89(x) #
    dr5_ld7_17_31(x)#
    dr5_ld7_49_53(x)#
    dr5_ld7_67_71(x)#

 
    dr7_ld9_79_91(x)#  
    dr7_ld9_19_61(x)# 
    dr7_ld9_7_37(x)# 
    dr7_ld9_43_73(x)# 
    dr7_ld9_11_89(x)# 
    dr7_ld9_29_71(x)# 
    dr7_ld9_17_47(x)# 
    dr7_ld9_53_83(x)# 
    dr7_ld9_13_13(x)# 
    dr7_ld9_31_49(x)# 
    dr7_ld9_67_67(x)# 
    dr7_ld9_23_23(x)# 
    dr7_ld9_41_59(x)#
    dr7_ld9_77_77(x)#

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
            print ("{} is quad prime".format(i))


execfile("ElderSieve.py")









