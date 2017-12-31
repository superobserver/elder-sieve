#!/usr/local/env python #python 2.7
#Sieve for generating sequence A201816

new_test = 1000
a = range(0, new_test)


def drLD(x, l, m, z, o):      
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


for x in xrange(1, 6): # 10000 = 12; 100000 = 36; 1,000,000 = 108; 10,000,000 = 336; 100,000,000 = 1056; 1,000,000,000 = 
 
 
    drLD(x, 76, -1, 13, 91)   #13,91
    drLD(x, 94, 18, 19, 67)  #19,67
    drLD(x, 94, 24, 37, 49)  #37,49
    drLD(x, 76, 11, 31, 73)  #31,73
    drLD(x, 86, 6, 11, 83)   #11,83
    drLD(x, 104, 29, 29, 47) #29,47
    drLD(x, 86, 14, 23, 71)  #23,71
    drLD(x, 86, 20, 41, 53)  #41,53
    drLD(x, 104, 25, 17, 59) #17,59
    drLD(x, 14, 0, 77, 89)   #77,89
    drLD(x, 94, 10, 7, 79)   #7,79
    drLD(x, 76, 15, 43, 61)  #43,61


#print a[0]
if a[0] == 0:
  list_A201816 = [i for i in a if i !=0]
  list_A201816.insert(0, 0)
  print list_A201816
  print "These are the first %d terms of Sloane's A201816." % len(list_A201816)
if a[0] > 0:
  list_A201816 = [i for i in a if i !=0]
  print list_A201816
  print "These are the first %d terms of Sloane's A201816." % len(list_A201816)


# #Use this code to search for Arithmetic Progressions of Twin Primes.
# A = list_A201816    # in sorted order
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
