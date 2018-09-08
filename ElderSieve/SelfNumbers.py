

#This program is for exploring self numbers. See Sloane's A003052 http://oeis.org/A003052
from collections import Counter

#a = range(0, new_test)

v = input()
a = [None]*10000
b = [None]*10000
try:
    v = int(v)
except:
    v = 2017   
# the generator prints all self numbers in range 1..v
for i in range(1, v+1):
    self = True
    for j in range(1, i):
        if j + sum(map(int, str(j))) == i:
            self = False
    if self:
        print(i)
        b[i]=0
        
#       zed = [ x%9 for x in list_A201804]
          
        
#        108
#110, 211, 312, 413, 514, 615, 716, 817, 918
#121, 222, 323, 424, 525, 626, 727, 828, 929
#132, 233, 334, 435, 536, 637, 738, 839, 940
#143, 244, 345, 446, 547, 648, 749, 850, 951
#154, 255, 356, 457, 558, 659, 760, 861, 962
#165, 266, 367, 468, 569, 670, 771, 872, 973
#176, 277, 378, 479, 580, 681, 782, 883, 984
#187, 288, 389, 490, 591, 692, 793, 894, 995
#198, 299, 400, 501, 602, 703, 804, 905, 1006
#209, 310, 411, 512, 613, 714, 815, 916, 


list_b = [i for i,x in enumerate(b) if x == 0]
#print list_b

new_list = [ x%9 for x in list_b]

print new_list






#### CATASTROPHICALLY FAILS AT 1006 ##############

x1 = 110
x2 = 121
x3 = 132
x4 = 143
x5 = 154
x6 = 165
x7 = 176
x8 = 187
x9 = 198
x10 = 209

for x in xrange(1, 100):
    xx = x1 + 101*x
    try:
        a[xx]=0
        #print "This is xx", xx
    except:
        pass
    
    x2x = x2 + 101*x
    try:
        a[x2x]=0
    except:
        pass
    
    x3x = x3 + 101*x
    try:
        a[x3x]=0
    except:
        pass    
    
   
    x4x = x4 + 101*x
    try:
        a[x4x]=0
    except:
        pass

    x5x = x5 + 101*x
    try:
        a[x5x]=0
    except:
        pass

    x6x = x6 + 101*x
    try:
        a[x6x]=0
    except:
        pass



    x7x = x7 + 101*x
    try:
        a[x7x]=0
    except:
        pass    
    
    
    x8x = x8 + 101*x
    try:
        a[x8x]=0
    except:
        pass 
 
    x9x = x9 + 101*x
    try:
        a[x9x]=0
    except:
        pass 
 
 
    x10x = x10 + 101*x
    try:
        a[x10x]=0
    except:
        pass

######################### THE ABOVE CODE BLOCK FAILS AT 1006 ################


list_a = [i for i,x in enumerate(a) if x == 0]
#print list_a
#print sorted(a)
#print b
lib = zip(new_list, list_b)
#print sorted([lib], key=lambda x: x[-1])

################################## ISOLATE SELF NUMBER GROWTH RATES BY DIGITAL ROOT ############

zed = Counter(new_list)
print zed

#Digital Root counted per item in list

# @7000 = Counter({5: 78, 7: 78, 0: 77, 3: 77, 1: 76, 2: 76, 4: 76, 6: 76, 8: 75})
# @6000 = Counter({3: 67, 5: 67, 7: 67, 0: 66, 1: 66, 2: 65, 4: 65, 6: 65, 8: 64})
# @5000 = Counter({1: 56, 3: 56, 5: 56, 7: 56, 0: 55, 2: 54, 4: 54, 8: 54, 6: 53})
# @4000 = Counter({1: 45, 3: 45, 5: 45, 7: 45, 0: 44, 8: 44, 2: 43, 6: 43, 4: 42})
# @3000 = Counter({1: 34, 3: 34, 5: 34, 7: 34, 0: 33, 6: 33, 8: 33, 4: 32, 2: 31})
# @2000 = Counter({1: 23, 3: 23, 5: 23, 7: 23, 4: 22, 6: 22, 8: 22, 0: 21, 2: 21})
# @1000 = Counter({1: 12, 3: 12, 5: 12, 0: 11, 2: 11, 4: 11, 6: 11, 7: 11, 8: 11})

# @0900 = Counter({1: 11, 3: 11, 0: 10, 2: 10, 4: 10, 5: 10, 6: 10, 7: 10, 8: 10})
# @0800 = Counter({1: 10, 0: 9,  2: 9,  3: 9,  4: 9,  5: 9,  6: 9,  7: 9,  8: 9})
# @0700 = Counter({0: 8,  1: 8,  2: 8,  3: 8,  4: 8,  5: 8,  6: 8,  7: 8,  8: 8})
# @0600 = Counter({0: 7,  1: 7,  2: 7,  3: 7,  4: 7,  5: 7,  6: 7,  7: 7,  8: 6})
# @0500 = Counter({0: 6,  1: 6,  2: 6,  3: 6,  4: 6,  5: 6,  7: 6,  6: 5,  8: 5})
# @0400 = Counter({0: 5,  1: 5,  2: 5,  3: 5,  4: 5,  5: 5,  7: 5,  6: 4,  8: 4})
# @0300 = Counter({0: 4,  1: 4,  2: 4,  3: 4,  5: 4,  7: 4,  4: 3,  6: 3,  8: 3})
# @0200 = Counter({0: 3,  1: 3,  3: 3,  5: 3,  7: 3,  2: 2,  4: 2,  6: 2,  8: 2})
# @0100 = Counter({1: 2,  3: 2,  5: 2,  7: 2,  0: 1,  2: 1,  4: 1,  6: 1,  8: 1})

