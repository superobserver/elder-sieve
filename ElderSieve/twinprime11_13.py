#!/usr/local/env python #python 2.7
#Sieve for generating sequence A224854

new_test = 100000
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
 
 
    drLD_min_min(x, 78, 1, 11, 91)   #11,91
    drLD_min_plus(x, 132, 48, 19, 29) #19,29
    drLD_min_plus(x, 60, 4, 37, 83)   #37,83
    drLD_min_plus(x, 60, 8, 47, 73)   #47,73
    drLD_min_plus(x, 90, 11, 13, 77)  #13,77
    drLD_min_plus(x, 108, 32, 31, 41) #31,41
    drLD_min_plus(x, 72, 14, 49, 59)  #49,59
    drLD_min_plus(x, 90, 17, 23, 67)  #23,67
    drLD_min_plus(x, 120, 34, 7, 53)  #7,53
    drLD_min_plus(x, 120, 38, 17, 43) #17,43
    drLD_min_plus(x, 48, 6, 61, 71)   #61,71
    drLD_min_plus(x, 12, 0, 79, 89)   #79,89

    drLD_min_min(x, 76, 1, 13, 91)   #13,91
    drLD_min_plus(x, 94, 18, 19, 67)  #19,67
    drLD_min_plus(x, 94, 24, 37, 49)  #37,49
    drLD_min_plus(x, 76, 11, 31, 73)  #31,73
    drLD_min_plus(x, 86, 6, 11, 83)   #11,83
    drLD_min_plus(x, 104, 29, 29, 47) #29,47
    drLD_min_plus(x, 86, 14, 23, 71)  #23,71
    drLD_min_plus(x, 86, 20, 41, 53)  #41,53
    drLD_min_plus(x, 104, 25, 17, 59) #17,59
    drLD_min_plus(x, 14, 0, 77, 89)   #77,89
    drLD_min_plus(x, 94, 10, 7, 79)   #7,79
    drLD_min_plus(x, 76, 15, 43, 61)  #43,61


#print a  

#print a[0]
if a[0] == 0:
  list_A224854 = [i for i in a if i !=0]
  list_A224854.insert(0, 0)
  print list_A224854
  print "These are the first %d terms of Sloane's A224854." % len(list_A224854)
if a[0] > 0:
  list_A224854 = [i for i in a if i !=0]
  print list_A224854
  print "These are the first %d terms of Sloane's A224854." % len(list_A224854)


# #Use this code to search for Arithmetic Progressions of Twin Primes.
# A = list_A224854    # in sorted order
# Aset = set(A)
# print len(A)
# 
# for d in xrange(1, 500):
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

