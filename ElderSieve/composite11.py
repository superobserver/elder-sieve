#!/usr/local/env python #python 2.7
#Sieve for generating sequence A201804

new_test = 1000000
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

for x in xrange(1, 108): # 10000 = 12; 100000 = 36; 1,000,000 = 108; 10,000,000 = 336; 100,000,000 = 1056; 1,000,000,000 = 
  
    drLD(x, 78, -1, 11, 91)   #11,91
    drLD(x, 132, 48, 19, 29) #19,29
    drLD(x, 60, 4, 37, 83)   #37,83
    drLD(x, 60, 8, 47, 73)   #47,73
    drLD(x, 90, 11, 13, 77)  #13,77
    drLD(x, 108, 32, 31, 41) #31,41
    drLD(x, 72, 14, 49, 59)  #49,59
    drLD(x, 90, 17, 23, 67)  #23,67
    drLD(x, 120, 34, 7, 53)  #7,53
    drLD(x, 120, 38, 17, 43) #17,43
    drLD(x, 48, 6, 61, 71)   #61,71
    drLD(x, 12, 0, 79, 89)   #79,89

print a  #uncomment this line to see the full list (primes and 0=composite)
if a[0] == 0:
  list_A201804 = [i for i in a if i !=0]
  list_A201804.insert(0, 0)
#  print list_A201804
  print "These are the first %d terms of Sloane's A201804." % len(list_A201804)
if a[0] > 0:
  list_A201804 = [i for i in a if i !=0]
  print list_A201804
  print "These are the first %d terms of Sloane's A201804." % len(list_A201804)
  
# #Use this code to search for Arithmetic Progressions of Twin Primes.
# A = list_A201804    # in sorted order
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
