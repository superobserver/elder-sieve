



new_test = 1000

a = [None]*int(new_test)

def drLD(x, z):      
  """Elder Sieve in A000040"""
  
  new_y = z+(90*(x-1)) 
  print x #pound this to cease watching the algorithm cycle
  if new_y < new_test:
    if a[new_y] == None:
      a[new_y] = 2  
  else:
    return
  for n in xrange (1, new_test): 
    new2_y = new_y*(n+1)
    if new2_y < new_test:
      try:
          a[new2_y] = 0
      except:
          pass


for x in xrange(1, 100): # untested range. will update with function
  
      drLD(x, 7)  #11,91          (first cancel = 11) 90*(x*x) 78x +(-1)
      drLD(x, 11)  #11,91          (first cancel = 11) 90*(x*x) 78x +(-1)
      drLD(x, 13)  #11,91          (first cancel = 11) 90*(x*x) 78x +(-1)
      drLD(x, 17)  #11,91          (first cancel = 11) 90*(x*x) 78x +(-1)
      drLD(x, 19)  #11,91          (first cancel = 11) 90*(x*x) 78x +(-1)
      drLD(x, 23)  #11,91          (first cancel = 11) 90*(x*x) 78x +(-1)
      drLD(x, 29)  #11,91          (first cancel = 11) 90*(x*x) 78x +(-1)
      drLD(x, 31)  #11,91          (first cancel = 11) 90*(x*x) 78x +(-1)
      drLD(x, 37)  #11,91          (first cancel = 11) 90*(x*x) 78x +(-1)
      drLD(x, 41)  #11,91          (first cancel = 11) 90*(x*x) 78x +(-1)
      drLD(x, 43)  #11,91          (first cancel = 11) 90*(x*x) 78x +(-1)
      drLD(x, 47)  #11,91          (first cancel = 11) 90*(x*x) 78x +(-1)
      drLD(x, 49)  #11,91          (first cancel = 11) 90*(x*x) 78x +(-1)
      drLD(x, 53)  #11,91          (first cancel = 11) 90*(x*x) 78x +(-1)
      drLD(x, 59)  #11,91          (first cancel = 11) 90*(x*x) 78x +(-1)
      drLD(x, 61)  #11,91          (first cancel = 11) 90*(x*x) 78x +(-1)
      drLD(x, 67)  #11,91          (first cancel = 11) 90*(x*x) 78x +(-1)
      drLD(x, 71)  #11,91          (first cancel = 11) 90*(x*x) 78x +(-1)
      drLD(x, 73)  #11,91          (first cancel = 11) 90*(x*x) 78x +(-1)
      drLD(x, 77)  #11,91          (first cancel = 11) 90*(x*x) 78x +(-1)
      drLD(x, 79)  #11,91          (first cancel = 11) 90*(x*x) 78x +(-1)
      drLD(x, 83)  #11,91          (first cancel = 11) 90*(x*x) 78x +(-1)
      drLD(x, 89)  #11,91          (first cancel = 11) 90*(x*x) 78x +(-1)
      drLD(x, 91)  #11,91          (first cancel = 11) 90*(x*x) 78x +(-1)
      
      
list_A000040 = [i for i,x in enumerate(a) if x > 1]
#list_test = [i for i in a if i > 1]
#print list_test
print list_A000040
print len(list_A000040)
#print 

# 
# def primes_sieve(limit):
#     limitn = limit+1
#     not_prime = set()
#     primes = []
# 
#     for i in range(2, limitn):
#         if i in not_prime:
#             continue
# 
#         for f in range(i*i, limitn, i):
#             not_prime.add(f)
# 
#         primes.append(i)
#     #print len(primes)
#     return primes
# 
# print primes_sieve(10000000)
