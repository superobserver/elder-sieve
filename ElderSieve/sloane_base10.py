import sys
import csv

print "\x1b[32mHello Mr. Sloane,\x1b[0m I hope that you are having a pleasant day.\x1b[0m"
print ""
print "We need to establish a limit for 'type-1 numbers' for our composite generator. I suggest starting with 10."

answer = raw_input("Type your limit here>")
limit = int(answer)


print ""
print "We need a limit for type-2 numbers; one that tells the generator how many terms to produce from each type-1 number."

answer2 = raw_input("Type your limit here>")
limit2 = int(answer2) 



#Digital Root 1 and Last Digit 1 composite equations:
 
# DONE 19 + (90*x) * 19 + (90*y) = 1 + (90*z)
# DONE 91 + (90*x) * 91 + (90*y) = 1 + (90*z)
# DONE 37 + (90*x) * 73 + (90*y) = 1 + (90*z)
# DONE 11 + (90*x) * 41 + (90*y) = 1 + (90*z)
# DONE 29 + (90*x) * 59 + (90*y) = 1 + (90*z)
# DONE 47 + (90*x) * 23 + (90*y) = 1 + (90*z)
# DONE 83 + (90*x) * 77 + (90*y) = 1 + (90*z)
# DONE 13 + (90*x) * 7 + (90*y) = 1 + (90*z)
# DONE 31 + (90*x) * 61 + (90*y) = 1 + (90*z)
# DONE 49 + (90*x) * 79 + (90*y) = 1 + (90*z)
# DONE 67 + (90*x) * 43 + (90*y) = 1 + (90*z)
# DONE 17 + (90*x) * 53 + (90*y) = 1 + (90*z)
# DONE 71 + (90*x) * 71 + (90*y) = 1 + (90*z)
# DONE 89 + (90*x) * 89 + (90*y) = 1 + (90*z)


#composites for 29, 59
var_29 = [29 + (90*x) for x in xrange(0, limit)]
var_59 = [y * (59 + (90*z)) for y in var_29 for z in xrange (0, limit2)]
print var_59

var_59a = [59 + (90*x) for x in xrange(0, limit)]
var_29a = [y * (29 + (90*z)) for y in var_59a for z in xrange(0, limit2)]
print var_29a

#composites for 13,7 
var_13 = [13 + (90*x) for x in xrange(0, limit)] 
var_7 = [y * (7 + (90*z)) for y in var_13 for z in xrange(0, limit2)] 
print var_7

var_7a = [7 + (90*x) for x in xrange(0, limit)]
var_13a = [y * (13 + (90*z)) for y in var_7a for z in xrange(0, limit2)]
print var_13a



#composites for 19,19
var_19 = [19 + (90*x) for x in xrange(0, limit)] 
var_19a = [y * (19 + (90*z)) for y in var_19 for z in xrange(0, limit2)] 
print var_19a 

#composites for 11,41
var_11 = [11 + (90*x) for x in xrange(0, limit)] 
var_41 = [y * (41 + (90*z)) for y in var_11 for z in xrange(0, limit2)] 

var_41a = [41 + (90*x) for x in xrange(0, limit)]
var_11a = [y * (11 + (90*z)) for y in var_41a for z in xrange(0, limit2)]

print var_41
print var_11a

#composites for 17,53
var_17 = [17 + (90*x) for x in xrange(0, limit)] 
var_53 = [y * (53 + (90*z)) for y in var_17 for z in xrange(0, limit2)] 

var_53a = [53 + (90*x) for x in xrange(0, limit)]
var_17a = [y * (17 + (90*z)) for y in var_53a for z in xrange(0, limit2)]

print var_53
print var_17a


#composites for 47,23
var_47 = [47 + (90*x) for x in xrange(0, limit)] 
var_23 = [y * (23 + (90*z)) for y in var_47 for z in xrange(0, limit2)] 

var_23a = [23 + (90*x) for x in xrange(0, limit)]
var_47a = [y * (47 + (90*z)) for y in var_23a for z in xrange(0, limit2)]

print var_23
print var_47a

#composites for 31,61
var_31 = [31 + (90*x) for x in xrange(0, limit)] 
var_61 = [y * (61 + (90*z)) for y in var_31 for z in xrange(0, limit2)] 

var_61a = [61 + (90*x) for x in xrange(0, limit)]
var_31a = [y * (31 + (90*z)) for y in var_61a for z in xrange(0, limit2)]

print var_61
print var_31a

#composites for 37,73
var_37 = [37 + (90*x) for x in xrange(0, limit)] 
var_73 = [y * (73 + (90*z)) for y in var_37 for z in xrange(0, limit2)] 

var_73a = [73 + (90*x) for x in xrange(0, limit)]
var_37a = [y * (37 + (90*z)) for y in var_73a for z in xrange(0, limit2)]

print var_73
print var_37a

#composites for 67,43
var_67 = [67 + (90*x) for x in xrange(0, limit)] 
var_43 = [y * (43 + (90*z)) for y in var_67 for z in xrange(0, limit2)] 

var_43a = [43 + (90*x) for x in xrange(0, limit)]
var_67a = [y * (67 + (90*z)) for y in var_43a for z in xrange(0, limit2)]

print var_43
print var_67a

#composites for 49,79
var_49 = [49 + (90*x) for x in xrange(0, limit)] 
var_79 = [y * (79 + (90*z)) for y in var_49 for z in xrange(0, limit2)] 

var_79a = [79 + (90*x) for x in xrange(0, limit)]
var_49a = [y * (49 + (90*z)) for y in var_79a for z in xrange(0, limit2)]

print var_79
print var_49a

#composites for 71,71
var_71 = [71 + (90*x) for x in xrange(0, limit)] 
var_71a = [y * (71 + (90*z)) for y in var_71 for z in xrange(0, limit2)] 
print var_71a

#composites for 83,77
var_83 = [83 + (90*x) for x in xrange(0, limit)] 
var_77 = [y * (77 + (90*z)) for y in var_83 for z in xrange(0, limit2)] 

var_77a = [77 + (90*x) for x in xrange(0, limit)]
var_83a = [y * (83 + (90*z)) for y in var_77a for z in xrange(0, limit2)]

print var_77
print var_83a

#composites for 89,89
var_89 = [89 + (90*x) for x in xrange(0, limit)] 
var_89a = [y * (89 + (90*z)) for y in var_89 for z in xrange(0, limit2)] 
print var_89a

#composites for 91,91
var_91 = [91 + (90*x) for x in xrange(0, limit)] 
var_91a = [y * (91 + (90*z)) for y in var_91 for z in xrange(0, limit2)] 
print var_91a


mergedlist = list(set(var_59 + var_29a + var_19a  + var_91a + var_73 + var_37a + var_41 + var_11a + var_23 + var_47a + var_77 + var_83a + var_7 + var_13a + var_61 + var_31a +  var_79 + var_49a + var_43 + var_67a + var_53 + var_17a + var_71a + var_89a))
#print mergedlist
#mergedlist.sort();
#print "List:", mergedlist

values = mergedlist
thecsv = csv.writer(open("jeff.csv", 'wb'))
for value in values:
    thecsv.writerow([value])


sys.exit(0)
