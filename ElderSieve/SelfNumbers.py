

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

#[(1, 1), (3, 3), (5, 5), (7, 7), (0, 9), (2, 20), (4, 31), (6, 42), (8, 53), (1, 64), (3, 75), (5, 86), (7, 97), (0, 108), (2, 110), (4, 121), (6, 132), (8, 143), (1, 154), (3, 165), (5, 176), (7, 187), (0, 198), (2, 209), (4, 211), (6, 222), (8, 233), (1, 244), (3, 255), (5, 266), (7, 277), (0, 288), (2, 299), (4, 310), (6, 312), (8, 323), (1, 334), (3, 345), (5, 356), (7, 367), (0, 378), (2, 389), (4, 400), (6, 411), (8, 413), (1, 424), (3, 435), (5, 446), (7, 457), (0, 468), (2, 479), (4, 490), (6, 501), (8, 512), (1, 514), (3, 525), (5, 536), (7, 547), (0, 558), (2, 569), (4, 580), (6, 591), (8, 602), (1, 613), (3, 615), (5, 626), (7, 637), (0, 648), (2, 659), (4, 670), (6, 681), (8, 692), (1, 703), (3, 714), (5, 716), (7, 727), (0, 738), (2, 749), (4, 760), (6, 771), (8, 782), (1, 793), (3, 804), (5, 815), (7, 817), (0, 828), (2, 839), (4, 850), (6, 861), (8, 872), (1, 883), (3, 894), (5, 905), (7, 916), (0, 918), (2, 929), (4, 940), (6, 951), (8, 962), (1, 973), (3, 984), (5, 995), 

#(7, 1006), 

#Missing (0, xxxx) and (2, xxxx) it skips those digital roots when it goes into the 4-digit rank 

#(4, 1021), (6, 1032), (8, 1043), 

#(1, 1054), (3, 1065), (5, 1076), (7, 1087), (0, 1098), (2, 1109), (4, 1111), (6, 1122), (8, 1133), (1, 1144), (3, 1155), (5, 1166), (7, 1177), (0, 1188), (2, 1199), (4, 1210), (6, 1212), (8, 1223), (1, 1234), (3, 1245), (5, 1256), (7, 1267), (0, 1278), (2, 1289), (4, 1300), (6, 1311), (8, 1313), (1, 1324), (3, 1335), (5, 1346), (7, 1357), (0, 1368), (2, 1379), (4, 1390), (6, 1401), (8, 1412), (1, 1414), (3, 1425), (5, 1436), (7, 1447), (0, 1458), (2, 1469), (4, 1480), (6, 1491), (8, 1502), (1, 1513), (3, 1515), (5, 1526), (7, 1537), (0, 1548), (2, 1559), (4, 1570), (6, 1581), (8, 1592), (1, 1603), (3, 1614), (5, 1616), (7, 1627), (0, 1638), (2, 1649), (4, 1660), (6, 1671), (8, 1682), (1, 1693), (3, 1704), (5, 1715), (7, 1717), (0, 1728), (2, 1739), (4, 1750), (6, 1761), (8, 1772), (1, 1783), (3, 1794), (5, 1805), (7, 1816), (0, 1818), (2, 1829), (4, 1840), (6, 1851), (8, 1862), (1, 1873), (3, 1884), (5, 1895), (7, 1906), (0, 1917), (2, 1919), (4, 1930), (6, 1941), (8, 1952), (1, 1963), (3, 1974), (5, 1985), (7, 1996), 

#(0, 2007), 

#Missing (2, xxxx) and (4, xxxx)

#(6, 2022), (8, 2033), (1, 2044), 

#(3, 2055), (5, 2066), (7, 2077), (0, 2088), (2, 2099), (4, 2110), (6, 2112), (8, 2123), (1, 2134), (3, 2145), (5, 2156), (7, 2167), (0, 2178), (2, 2189), (4, 2200), (6, 2211), (8, 2213), (1, 2224), (3, 2235), (5, 2246), (7, 2257), (0, 2268), (2, 2279), (4, 2290), (6, 2301), (8, 2312), (1, 2314), (3, 2325), (5, 2336), (7, 2347), (0, 2358), (2, 2369), (4, 2380), (6, 2391), (8, 2402), (1, 2413), (3, 2415), (5, 2426), (7, 2437), (0, 2448), (2, 2459), (4, 2470), (6, 2481), (8, 2492), (1, 2503), (3, 2514), (5, 2516), (7, 2527), (0, 2538), (2, 2549), (4, 2560), (6, 2571), (8, 2582), (1, 2593), (3, 2604), (5, 2615), (7, 2617), (0, 2628), (2, 2639), (4, 2650), (6, 2661), (8, 2672), (1, 2683), (3, 2694), (5, 2705), (7, 2716), (0, 2718), (2, 2729), (4, 2740), (6, 2751), (8, 2762), (1, 2773), (3, 2784), (5, 2795), (7, 2806), (0, 2817), (2, 2819), (4, 2830), (6, 2841), (8, 2852), (1, 2863), (3, 2874), (5, 2885), (7, 2896), (0, 2907), (2, 2918), (4, 2920), (6, 2931), (8, 2942), (1, 2953), (3, 2964), (5, 2975), (7, 2986), (0, 2997)]

#(2, 3008), 

#Missing (4, xxxx) and (6, xxxx)

#(8, 3023), (1, 3034), (3, 3045), 

#(5, 3056), (7, 3067), (0, 3078), (2, 3089), (4, 3100), (6, 3111), (8, 3113), (1, 3124), (3, 3135), (5, 3146), (7, 3157), (0, 3168), (2, 3179), (4, 3190), (6, 3201), (8, 3212), (1, 3214), (3, 3225), (5, 3236), (7, 3247), (0, 3258), (2, 3269), (4, 3280), (6, 3291), (8, 3302), (1, 3313), (3, 3315), (5, 3326), (7, 3337), (0, 3348), (2, 3359), (4, 3370), (6, 3381), (8, 3392), (1, 3403), (3, 3414), (5, 3416), (7, 3427), (0, 3438), (2, 3449), (4, 3460), (6, 3471), (8, 3482), (1, 3493), (3, 3504), (5, 3515), (7, 3517), (0, 3528), (2, 3539), (4, 3550), (6, 3561), (8, 3572), (1, 3583), (3, 3594), (5, 3605), (7, 3616), (0, 3618), (2, 3629), (4, 3640), (6, 3651), (8, 3662), (1, 3673), (3, 3684), (5, 3695), (7, 3706), (0, 3717), (2, 3719), (4, 3730), (6, 3741), (8, 3752), (1, 3763), (3, 3774), (5, 3785), (7, 3796), (0, 3807), (2, 3818), (4, 3820), (6, 3831), (8, 3842), (1, 3853), (3, 3864), (5, 3875), (7, 3886), (0, 3897), (2, 3908), (4, 3919), (6, 3921), (8, 3932), (1, 3943), (3, 3954), (5, 3965), (7, 3976), (0, 3987), (2, 3998), 

#(4, 4009), 

#Missing (6, xxxx) and (8, xxxx)

#(1, 4024), (3, 4035), (5, 4046), 

#(7, 4057), (0, 4068), (2, 4079), (4, 4090), (6, 4101), (8, 4112), (1, 4114), (3, 4125), (5, 4136), (7, 4147), (0, 4158), (2, 4169), (4, 4180), (6, 4191), (8, 4202), (1, 4213), (3, 4215), (5, 4226), (7, 4237), (0, 4248), (2, 4259), (4, 4270), (6, 4281), (8, 4292), (1, 4303), (3, 4314), (5, 4316), (7, 4327), (0, 4338), (2, 4349), (4, 4360), (6, 4371), (8, 4382), (1, 4393), (3, 4404), (5, 4415), (7, 4417), (0, 4428), (2, 4439), (4, 4450), (6, 4461), (8, 4472), (1, 4483), (3, 4494), (5, 4505), (7, 4516), (0, 4518), (2, 4529), (4, 4540), (6, 4551), (8, 4562), (1, 4573), (3, 4584), (5, 4595), (7, 4606), (0, 4617), (2, 4619), (4, 4630), (6, 4641), (8, 4652), (1, 4663), (3, 4674), (5, 4685), (7, 4696), (0, 4707), (2, 4718), (4, 4720), (6, 4731), (8, 4742), (1, 4753), (3, 4764), (5, 4775), (7, 4786), (0, 4797), (2, 4808), (4, 4819), (6, 4821), (8, 4832), (1, 4843), (3, 4854), (5, 4865), (7, 4876), (0, 4887), (2, 4898), (4, 4909), (6, 4920), (8, 4922), (1, 4933), (3, 4944), (5, 4955), (7, 4966), (0, 4977), (2, 4988), (4, 4999), 

#(6, 5010), 

#Missing (8, xxx) and (1, xxxx)

#(3, 5025), (5, 5036), (7, 5047), 

#(0, 5058), (2, 5069), (4, 5080), (6, 5091), (8, 5102), (1, 5113), (3, 5115), (5, 5126), (7, 5137), (0, 5148), (2, 5159), (4, 5170), (6, 5181), (8, 5192), (1, 5203), (3, 5214), (5, 5216), (7, 5227), (0, 5238), (2, 5249), (4, 5260), (6, 5271), (8, 5282), (1, 5293), (3, 5304), (5, 5315), (7, 5317), (0, 5328), (2, 5339), (4, 5350), (6, 5361), (8, 5372), (1, 5383), (3, 5394), (5, 5405), (7, 5416), (0, 5418), (2, 5429), (4, 5440), (6, 5451), (8, 5462), (1, 5473), (3, 5484), (5, 5495), (7, 5506), (0, 5517), (2, 5519), (4, 5530), (6, 5541), (8, 5552), (1, 5563), (3, 5574), (5, 5585), (7, 5596), (0, 5607), (2, 5618), (4, 5620), (6, 5631), (8, 5642), (1, 5653), (3, 5664), (5, 5675), (7, 5686), (0, 5697), (2, 5708), (4, 5719), (6, 5721), (8, 5732), (1, 5743), (3, 5754), (5, 5765), (7, 5776), (0, 5787), (2, 5798), (4, 5809), (6, 5820), (8, 5822), (1, 5833), (3, 5844), (5, 5855), (7, 5866), (0, 5877), (2, 5888), (4, 5899), (6, 5910), (8, 5921), (1, 5923), (3, 5934), (5, 5945), (7, 5956), (0, 5967), (2, 5978), (4, 5989), (6, 6000), 

#(8, 6011), 

#Missing (1, xxxx) and (3, xxxx)

#(5, 6026), (7, 6037), (0, 6048), 

#(2, 6059), (4, 6070), (6, 6081), (8, 6092), (1, 6103), (3, 6114), (5, 6116), (7, 6127), (0, 6138), (2, 6149), (4, 6160), (6, 6171), (8, 6182), (1, 6193), (3, 6204), (5, 6215), (7, 6217), (0, 6228), (2, 6239), (4, 6250), (6, 6261), (8, 6272), (1, 6283), (3, 6294), (5, 6305), (7, 6316), (0, 6318), (2, 6329), (4, 6340), (6, 6351), (8, 6362), (1, 6373), (3, 6384), (5, 6395), (7, 6406), (0, 6417), (2, 6419), (4, 6430), (6, 6441), (8, 6452), (1, 6463), (3, 6474), (5, 6485), (7, 6496), (0, 6507), (2, 6518), (4, 6520), (6, 6531), (8, 6542), (1, 6553), (3, 6564), (5, 6575), (7, 6586), (0, 6597), (2, 6608), (4, 6619), (6, 6621), (8, 6632), (1, 6643), (3, 6654), (5, 6665), (7, 6676), (0, 6687), (2, 6698), (4, 6709), (6, 6720), (8, 6722), (1, 6733), (3, 6744), (5, 6755), (7, 6766), (0, 6777), (2, 6788), (4, 6799), (6, 6810), (8, 6821), (1, 6823), (3, 6834), (5, 6845), (7, 6856), (0, 6867), (2, 6878), (4, 6889), (6, 6900), (8, 6911), (1, 6922), (3, 6924), (5, 6935), (7, 6946), (0, 6957), (2, 6968), (4, 6979), (6, 6990)]
