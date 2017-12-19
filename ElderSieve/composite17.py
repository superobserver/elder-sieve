#!/usr/local/env python #python 2.7
#Integration leaves residue sequence A202115

new_test = 1000000
a = range(0, new_test)

def drLD_min_min(x, l, m, z, o):      
  y = 90*(x*x) - l*x - m 
  if y < new_test:
    #print y, x
    a[y] = 0
  else:
    return
  for n in xrange (1, new_test):
    new_y = y+((z+(90*(x-1)))*n)
    if new_y < new_test:
      a[new_y] = 0
    new2_y = y+((o+(90*(x-1)))*n)   
    if new2_y < new_test:   
      a[new2_y] = 0      
    if new_y > new_test:
      return
    else:
      pass

def drLD_min_plus(x, l, m, z, o):      
  y = 90*(x*x) - l*x + m 
  if y < new_test:
    a[y] = 0
  else:
    return
  for n in xrange (1, new_test):
    new_y = y+((z+(90*(x-1)))*n)
    if new_y < new_test:
      a[new_y] = 0
    new2_y = y+((o+(90*(x-1)))*n)   
    if new2_y < new_test:    
      a[new2_y] = 0      
    if new_y > new_test:
      return
    else:
      pass

for x in xrange(1, 108): # 10000 = 12; 100000 = 36; 1,000,000 = 108; 10,000,000 = 336; 100,000,000 = 1056; 1,000,000,000 = 
  
    drLD_min_min(x, 72, 1, 17, 91)   #17,91
    drLD_min_plus(x, 108, 29, 19, 53) #19,53
    drLD_min_plus(x, 72, 11, 37, 71)   #37,71
    drLD_min_plus(x, 18, 0, 73, 89)   #73,89
    drLD_min_plus(x, 102, 20, 11, 67)  #11,67
    drLD_min_plus(x, 138, 52, 13, 29) #13,29
    drLD_min_plus(x, 102, 28, 31, 47)  #31,47
    drLD_min_plus(x, 48, 3, 49, 83)  #49,83
    drLD_min_plus(x, 78, 8, 23, 79)  #23,79
    drLD_min_plus(x, 132, 45, 7, 41) #7,41
    drLD_min_plus(x, 78, 16, 43, 59)   #43,59
    drLD_min_plus(x, 42, 4, 61, 77)   #61,77

#print a  
if a[0] == 0:
  list_A202115 = [i for i in a if i !=0]
  list_A202115.insert(0, 0)
  print list_A202115
  print "These are the first %d terms of Sloane's A202115." % len(list_A202115)
if a[0] > 0:
  list_A202115 = [i for i in a if i !=0]
  print list_A202115
  print "These are the first %d terms of Sloane's A202115." % len(list_A202115)
  
# #Use this code to search for Arithmetic Progressions of Twin Primes.
# A = list_A202115    # in sorted order
# Aset = set(A)
# print len(A)
# 
# for d in xrange(1, 3):
#     already_seen = set()
#     for a in A:
#         if a not in already_seen:
#             b = a
#             count = 1
#             while b + d in Aset:
#                 b += d
#                 count += 1
#                 already_seen.add(b)
#             if count >= 5:
#                 print "found %d items in %d .. %d .. with gap = %d" % (count, a, b, d)
#                 #e.extend(d)
#             # collect here the largest 'count'
