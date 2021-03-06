#!/usr/local/env python #python 2.7
#Sieve for generating sequence A201804

new_test = 1000000
a = [None]*int(new_test)

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
  
    drLD(x, 120, 34, 7, 53)  #7,53  @4,  154 1
    drLD(x, 132, 48, 19, 29) #19,29 @6,  144 2
    drLD(x, 120, 38, 17, 43) #17,43 @8,  158 3
    drLD(x, 90, 11, 13, 77)  #13,77 @11, 191 4
    drLD(x, 78, -1, 11, 91)  #11,91 @11, 203 5
    drLD(x, 108, 32, 31, 41) #31,41 @14, 176 6
    drLD(x, 90, 17, 23, 67)  #23,67 @17, 197 7
    drLD(x, 72, 14, 49, 59)  #49,59 @32, 230 8
    drLD(x, 60, 4, 37, 83)   #37,83 @34, 244 9
    drLD(x, 60, 8, 47, 73)   #47,73 @38, 248 10
    drLD(x, 48, 6, 61, 71)   #61,71 @48, 270 11
    drLD(x, 12, 0, 79, 89)   #79,89 @78, 336 12

list_A201804 = [i for i,x in enumerate(a) if x != 0]
#print a  #uncomment this line to see the full list (None=primes and 0=composite)
print list_A201804
print "%d is the %dth term of Sloane's A201804." % (list_A201804[-1], len(list_A201804))
  
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
