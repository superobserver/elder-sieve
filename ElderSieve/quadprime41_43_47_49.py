#!/usr/local/env python #python 2.7
#Integration leaves residue sequence A202104
import sys
import csv
import time
import subprocess

dump = open("composite1.csv", "w")
new_test = 40000

####################################################
#new 
#43, 267, 671, 1255, 2019, 2963, 4087, 5391, 6875, 8539
def dr7_ld3_43_91(x):
  y = 90*(x*x) - 46*x - 1 
  if y > new_test:
    return
  #print "49,89", y
  dump.write(str(y) + "\n")
  for n in range(1, new_test):
    new_y = y+((43+(90*(x-1)))*n) 
    new2_y = y+((91+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################

###################################################
#new
#1, 117, 413, 889, 1545, 2381, 3397, 4593, 5969, 7525, 9261
def dr7_ld3_7_19(x):
  y = 90*(x*x) - 154*x + 65
  if y > new_test:
    return
  dump.write(str(y) + "\n") 
  for n in range (1, new_test):
    new_y = y+((7+(90*(x-1)))*n)
    new2_y = y+((19+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################

###################################################
#32, 238, 624, 1190, 1936, 2862, 3968, 5254, 6720, 8366
#new
def dr7_ld3_37_79(x):
  y = 90*(x*x) - 64*x + 6
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((37+(90*(x-1)))*n)
    new2_y = y+((79+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
##################################################

##################################################
#49, 273, 677, 1261, 2025, 2969, 4093, 5397, 6881, 8545
#new 
def dr7_ld3_61_73(x):
  y = 90*(x*x) - 46*x + 5
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((61+(90*(x-1)))*n)
    new2_y = y+((73+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################	  

###################################################
#6, 160, 494, 1008, 1702, 2576, 3630, 4864, 6278, 7872, 9646
#new
def dr7_ld3_11_53(x):
  y = 90*(x*x) - 116*x + 32
  if y > new_test:
    return  
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((11+(90*(x-1)))*n)
    new2_y = y+((53+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
####################################################

####################################################
#5, 141, 457, 953, 1629, 2485, 3521, 4737, 6133, 7709, 9465
#new
def dr7_ld3_17_29(x):
  y = 90*(x*x) - 134*x + 49
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((17+(90*(x-1)))*n) 
    new2_y = y+((29+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
######################################################

######################################################

#46, 272, 678, 1264, 2030, 2976, 4102, 5408, 6894, 8560, 10406
#new
def dr7_ld3_47_89(x):
  y = 90*(x*x) - 44*x 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((47+(90*(x-1)))*n)
    new2_y = y+((89+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
#############################################################

##############################################################

#65, 309, 733, 1337, 2121, 3085, 4229, 5553, 7057, 8741, 10605
#new
def dr7_ld3_71_83(x):
  y = 90*(x*x) - 26*x + 1 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((71+(90*(x-1)))*n) 
    new2_y = y+((83+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
############################################################

########################################################
 
#4, 138, 452, 946, 1620, 2474, 3508, 4722, 6116, 7690
#new
def dr7_ld3_13_31(x):
  y = 90*(x*x) - 136*x + 50
  if y > new_test:
    return 
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((13+(90*(x-1)))*n)
    new2_y = y+((31+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
############################################################

########################################################

#36, 242, 628, 1194, 1940, 2866, 3972, 5258, 6724, 8370, 10196
#new
def dr7_ld3_49_67(x):
  y = 90*(x*x) - 64*x + 10
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((49+(90*(x-1)))*n) 
    new2_y = y+((67+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
########################################################

########################################################
#10, 164, 498, 1012, 1706, 2580, 3634, 4868, 6282, 7876, 9650
#new
def dr7_ld3_23_41(x):
  y = 90*(x*x) - 116*x + 36
  if y > new_test:
    return
  #print y, "49,49"
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((23+(90*(x-1)))*n)
    new2_y = y+((41+(90*(x-1)))*n) 
    #print new_y, "23"
    #print new2_y, "41"
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
######################################################

#####################################################

#50, 276, 682, 1268, 2034, 2980, 4106, 5412, 6898, 8564, 10410
#new
def dr7_ld3_59_77(x):
  y = 90*(x*x) - 44*x + 4
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((59+(90*(x-1)))*n)
    new2_y = y+((77+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")

####################################################
#new 
#48, 276, 684, 1272, 2040, 2988, 4116, 5424
def dr5_ld1_49_89(x):
  y = 90*(x*x) - 42*x 
  if y > new_test:
    return
  #print "49,89", y
  dump.write(str(y) + "\n")
  for n in range(1, new_test):
    new_y = y+((49+(90*(x-1)))*n) 
    new2_y = y+((89+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################


###################################################
#new
#41, 263, 665, 1247
def dr5_ld1_41_91(x):
  y = 90*(x*x) - 48*x - 1
  if y > new_test:
    return
  dump.write(str(y) + "\n") 
  for n in range (1, new_test):
    new_y = y+((41+(90*(x-1)))*n)
    new2_y = y+((91+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################

###################################################
#12, 180, 528, 1056, 1764, 2652, 3720
#new
def dr5_ld1_19_59(x):
  y = 90*(x*x) - 102*x + 24
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((19+(90*(x-1)))*n)
    new2_y = y+((59+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
##################################################

##################################################
#9, 159, 489, 999, 1689, 2559, 3609, 4839
#new 
def dr5_ld1_23_37(x):
  y = 90*(x*x) - 120*x + 39 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((23+(90*(x-1)))*n)
    new2_y = y+((37+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################	  

###################################################
#7, 169, 511, 1033, 1735, 2617, 3679
#new
def dr5_ld1_11_61(x):
  y = 90*(x*x) - 108*x + 25  
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((11+(90*(x-1)))*n)
    new2_y = y+((61+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
####################################################

####################################################
#25, 223, 601, 1159, 1897, 2815
#new
def dr5_ld1_29_79(x):
  y = 90*(x*x) - 72*x + 7
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((29+(90*(x-1)))*n) 
    new2_y = y+((79+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
######################################################

######################################################

#22, 202, 562, 1102, 1822, 2722, 3802, 5062
#new
def dr5_ld1_43_47(x):
  y = 90*(x*x) - 90*x + 22
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((43+(90*(x-1)))*n)
    new2_y = y+((47+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")

##############################################################

#2, 122, 422, 902, 1562, 2402, 3422, 4622, 6002, 7562
#new
def dr5_ld1_13_17(x):
  y = 90*(x*x) - 150*x + 62
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((13+(90*(x-1)))*n) 
    new2_y = y+((17+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
############################################################

########################################################
 
#24, 216, 588, 1140, 1872, 2784, 3876, 5148
#new
def dr5_ld1_31_71(x):
  y = 90*(x*x) - 78*x + 12
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((31+(90*(x-1)))*n)
    new2_y = y+((71+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
############################################################

########################################################

#62, 302, 722, 1322, 2102, 3062, 4202, 5522, 7022, 8702, 10562
#new
def dr5_ld1_73_77(x):
  y = 90*(x*x) - 30*x + 2 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((73+(90*(x-1)))*n) 
    new2_y = y+((77+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
########################################################

########################################################
#39, 249, 639, 1209, 1959, 2889, 3999, 5289, 6759
#new
def dr5_ld1_53_67(x):
  y = 90*(x*x) - 60*x + 9
  if y > new_test:
    return
  #print y, "53,67"
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((53+(90*(x-1)))*n)
    new2_y = y+((67+(90*(x-1)))*n) 
    #print new_y, "53"
    #print new2_y, "67"
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
######################################################

#####################################################

#6, 186, 546, 1086, 1806, 2706, 3786, 5046
#new
def dr5_ld1_7_83(x):
  y = 90*(x*x) - 90*x + 6
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((7+(90*(x-1)))*n)
    new2_y = y+((83+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
   
#########################################################


####################################################
#new 
#49, 279, 689, 1279, 2049, 2999, 4129, 5439, 6929
def dr4_ld9_49_91(x):
  y = 90*(x*x) - 40*x - 1 
  if y > new_test:
    return
  #print "49,91", y
  dump.write(str(y) + "\n")
  for n in range(1, new_test):
    new_y = y+((49+(90*(x-1)))*n) 
    new2_y = y+((91+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################


###################################################
#new
#6, 146, 466, 966, 1646, 2506, 3546, 4766, 6166, 7746
def dr4_ld9_19_31(x):
  y = 90*(x*x) - 130*x + 46
  if y > new_test:
    return
  dump.write(str(y) + "\n") 
  for n in range (1, new_test):
    new_y = y+((19+(90*(x-1)))*n)
    new2_y = y+((31+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################

###################################################
#27, 221, 595, 1149, 1883, 2797, 3891, 5165, 6619, 8253
#new
def dr4_ld9_37_67(x):
  y = 90*(x*x) - 76*x + 13
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((37+(90*(x-1)))*n)
    new2_y = y+((67+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
##################################################

##################################################
#10, 186, 542, 1078, 1794, 2690, 3766, 5022, 6458, 8074
#new 
def dr4_ld9_13_73(x):
  y = 90*(x*x) - 94*x + 14 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((13+(90*(x-1)))*n)
    new2_y = y+((73+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################	  

###################################################
#3, 133, 443, 933, 1603, 2453, 3483, 4693, 6083, 7653, 9403
#new
def dr4_ld9_11_29(x):
  y = 90*(x*x) - 140*x + 53  
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((11+(90*(x-1)))*n)
    new2_y = y+((29+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
####################################################

####################################################
#24, 208, 572, 1116, 1840, 2744, 3828, 5092, 6536, 8160
#new
def dr4_ld9_47_47(x):
  y = 90*(x*x) - 86*x + 20
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((47+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")

######################################################

######################################################

#76, 332, 768, 1384, 2180, 3156, 4312, 5648, 7164, 8860
#new
def dr4_ld9_83_83(x):
  y = 90*(x*x) - 14*x
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((83+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")

#############################################################

##############################################################

#13, 179, 525, 1051, 1757, 2643, 3709, 4955, 6381, 7987
#new
def dr4_ld9_23_53(x):
  y = 90*(x*x) - 104*x + 27
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((23+(90*(x-1)))*n) 
    new2_y = y+((53+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###############################################

########################################################
 
#40, 260, 660, 1240, 2000, 2940, 4060, 5360, 6840, 8500
#new
def dr4_ld9_41_89(x):
  y = 90*(x*x) - 50*x
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((41+(90*(x-1)))*n)
    new2_y = y+((89+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
############################################################

########################################################

#46, 266, 666, 1246, 2006, 2946, 4066, 5366, 6846, 8506
#new
def dr4_ld9_59_71(x):
  y = 90*(x*x) - 50*x + 6 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((59+(90*(x-1)))*n) 
    new2_y = y+((71+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
########################################################

########################################################
#14, 198, 562, 1106, 1830, 2734, 3818, 5082, 6526, 8150
#new
def dr4_ld9_17_77(x):
  y = 90*(x*x) - 86*x + 10
  if y > new_test:
    return
  #print y, "17,77"
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((17+(90*(x-1)))*n)
    new2_y = y+((77+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
######################################################

#####################################################

#0, 104, 388, 852, 1496, 2320, 3324, 4508, 5872, 7416, 9140
#new
def dr4_ld9_7_7(x):
  y = 90*(x*x) - 166*x + 76
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((7+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")

   
#########################################################

#####################################################

#20, 196, 552, 1088, 1804, 2700, 3776, 5032, 6468, 8084, 9880
#new
def dr4_ld9_43_43(x):
  y = 90*(x*x) - 94*x + 24
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((43+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")

   
#########################################################

#####################################################

#53, 283, 693, 1283, 2053, 3003, 4133, 5443, 6933, 8603
#new
def dr4_ld9_61_79(x):
  y = 90*(x*x) - 40*x + 3
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((61+(90*(x-1)))*n)
    new2_y = y+((79+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
   
#########################################################


####################################################
#new 
#47, 275, 683, 1271, 2039, 2987, 4115, 5423, 6911, 8579
def dr2_ld7_47_91(x):
  y = 90*(x*x) - 42*x - 1 
  if y > new_test:
    return
  #print "47,91", y
  dump.write(str(y) + "\n")
  for n in range(1, new_test):
    new_y = y+((47+(90*(x-1)))*n) 
    new2_y = y+((91+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################


###################################################
#new
#17, 209, 581, 1133, 1865, 2777, 3869, 5141, 6593, 8225
def dr2_ld7_19_83(x):
  y = 90*(x*x) - 78*x + 5
  if y > new_test:
    return
  dump.write(str(y) + "\n") 
  for n in range (1, new_test):
    new_y = y+((19+(90*(x-1)))*n)
    new2_y = y+((83+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################


###################################################
#4, 142, 460, 958, 1636, 2494, 3532, 4750, 6148
#new
def dr2_ld7_11_37(x):
  y = 90*(x*x) - 132*x + 46
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((11+(90*(x-1)))*n)
    new2_y = y+((37+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
##################################################


##################################################
#23, 215, 587, 1139, 1871, 2783, 3875, 5147, 6599, 8231
#new 
def dr2_ld7_29_73(x):
  y = 90*(x*x) - 78*x + 11 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((29+(90*(x-1)))*n)
    new2_y = y+((73+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
###################################################	  


###################################################
#8, 170, 512, 1034, 1736, 2618, 3680, 4922, 6344, 7946
#new
def dr2_ld7_13_59(x):
  y = 90*(x*x) - 108*x + 26  
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((13+(90*(x-1)))*n)
    new2_y = y+((59+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
####################################################


####################################################
#26, 224, 602, 1160, 1898, 2816, 3914, 5192, 6650, 8288
#new
def dr2_ld7_31_77(x):
  y = 90*(x*x) - 72*x + 8
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((31+(90*(x-1)))*n) 
    new2_y = y+((77+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
######################################################


######################################################

#12, 174, 516, 1038, 1740, 2622, 3684, 4926, 6348
#new
def dr2_ld7_23_49(x):
  y = 90*(x*x) - 108*x + 30
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((23+(90*(x-1)))*n)
    new2_y = y+((49+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
#############################################################


##############################################################

#5, 173, 521, 1049, 1757, 2645, 3713, 4961, 6389, 7997, 9785
#new
def dr2_ld7_7_71(x):
  y = 90*(x*x) - 102*x + 17
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((7+(90*(x-1)))*n) 
    new2_y = y+((71+(90*(x-1)))*n)
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
############################################################


########################################################
 
#42, 264, 666, 1248, 2010, 2952, 4074, 5376, 6858
#new
def dr2_ld7_43_89(x):
  y = 90*(x*x) - 48*x 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((43+(90*(x-1)))*n)
    new2_y = y+((89+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
############################################################


########################################################

#11, 179, 527, 1055, 1763, 2651, 3719, 4967, 6395, 8003
#new
def dr2_ld7_17_61(x):
  y = 90*(x*x) - 102*x + 23 
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((17+(90*(x-1)))*n) 
    new2_y = y+((61+(90*(x-1)))*n)  
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
########################################################

########################################################
#46, 268, 670, 1252, 2014, 2956, 4078, 5380
#new
def dr2_ld7_53_79(x):
  y = 90*(x*x) - 48*x + 4 
  if y > new_test:
    return
  #print y, "53,79"
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((53+(90*(x-1)))*n)
    new2_y = y+((79+(90*(x-1)))*n) 
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
######################################################

#####################################################

#30, 228, 606, 1164, 1902
#new
def dr2_ld7_41_67(x):
  y = 90*(x*x) - 72*x + 12  
  if y > new_test:
    return
  dump.write(str(y) + "\n")
  for n in range (1, new_test):
    new_y = y+((41+(90*(x-1)))*n)
    new2_y = y+((67+(90*(x-1)))*n)   
    if new_y < new_test: 
        dump.write(str(new_y) + "\n")
    if new2_y < new_test:
        dump.write(str(new2_y) + "\n")
   
#########################################################
 



for x in xrange(1, 100): 
 
    dr5_ld1_49_89(x)#
    dr5_ld1_41_91(x) #
    dr5_ld1_19_59(x) #
    dr5_ld1_23_37(x)#
    dr5_ld1_11_61(x)#
    dr5_ld1_29_79(x)#
    dr5_ld1_43_47(x)#
    dr5_ld1_13_17(x) #
    dr5_ld1_31_71(x) #
    dr5_ld1_73_77(x)#
    dr5_ld1_53_67(x)#
    dr5_ld1_7_83(x)#
    
    dr7_ld3_43_91(x)#
    dr7_ld3_7_19(x)#
    dr7_ld3_37_79(x)#
    dr7_ld3_61_73(x)#
    dr7_ld3_11_53(x)#
    dr7_ld3_17_29(x)#
    dr7_ld3_47_89(x)#
    dr7_ld3_71_83(x)#
    dr7_ld3_13_31(x)#
    dr7_ld3_49_67(x)#
    dr7_ld3_23_41(x)#
    dr7_ld3_59_77(x)#

 
    dr2_ld7_47_91(x) #
    dr2_ld7_19_83(x) #
    dr2_ld7_11_37(x) #
    dr2_ld7_29_73(x) #
    dr2_ld7_13_59(x) #
    dr2_ld7_31_77(x) #
    dr2_ld7_23_49(x) #
    dr2_ld7_7_71(x) #
    dr2_ld7_43_89(x) #
    dr2_ld7_17_61(x)#
    dr2_ld7_53_79(x) #
    dr2_ld7_41_67(x) #
	
    dr4_ld9_49_91(x)#
    dr4_ld9_19_31(x) #
    dr4_ld9_37_67(x) #
    dr4_ld9_13_73(x) #
    dr4_ld9_11_29(x)#
    dr4_ld9_47_47(x)#
    dr4_ld9_83_83(x)#
    dr4_ld9_23_53(x) #
    dr4_ld9_41_89(x) #
    dr4_ld9_59_71(x)#
    dr4_ld9_17_77(x)#
    dr4_ld9_7_7(x)#
    dr4_ld9_43_43(x)	
    dr4_ld9_61_79(x)


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











