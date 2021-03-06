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
  




	
91
(x, 2, 0, 91, 91) #91,91
(x, 142, 56, 19, 19) #19,19
(x, 70, 10, 37, 73) #37, 73
(x, 128, 43, 11, 41) #11, 41
(x, 92, 21, 29, 59) #29,59
(x, 110, 32, 23, 47) #23,47
(x, 20, 1, 77, 83) #77,83
(x, 160, 71, 7, 13) #7,13
(x, 88, 19, 31, 61) #31,61
(x, 52, 5, 49, 79) #49,79
(x, 70, 12, 43, 67) #43,67
(x, 110, 30, 17, 53) #17,53
(x, 38, 4, 71, 71) #71,71
(x, 2, 0, 89, 89) #89,89

89
(x, 1, 0, 89, 91) #89,91
(x, 90, 14, 19, 71) #19,71
(x, 126, 42, 17, 37) #17,37
(x, 54, 6, 53, 73) #53,73
(x, 120, 35, 11, 49) #11,49
(x, 120, 39, 29, 31) #29,31
(x, 66, 10, 47, 67) #47,67
(x, 84, 5, 13, 83) #13,83
(x, 114, 34, 23, 43) #23,43
(x, 60, 5, 41, 79) #41,79
(x, 60, 9, 59, 61) #59,61
(x, 96, 11, 7, 77) #7,77

83
(x, 6, -1, 83, 91) #83,91
(x, 114, 33, 19, 47) #19,47
(x, 114, 35, 37, 29) #37,29
(x, 96, 14, 11, 73) #11,73
(x, 126, 41, 13, 41) #13,41
(x, 126, 43, 23, 31) #23,31
(x, 54, 5, 49, 77) #49,77
(x, 54, 7, 59, 67) #59,67
(x, 84, 0, 7, 89) #7,89
(x, 66, 9, 43, 71) #43,71
(x, 66, 11, 53, 61) #53,61
(x, 84, 8, 17, 79) #17,79

79
(x, 10, -1, 79, 91) #79,91
(x, 100, 22, 19, 61) #19,61
(x, 136, 48, 7, 37) #7,37
(x, 64, 8, 43, 73) #43,73
(x, 80, 0, 11, 89) #11,89
(x, 80, 12, 29, 71) #29,71
(x, 116, 34, 17, 47) #17,47
(x, 44, 2, 53, 83) #53,83
(x, 154, 65, 13, 13) #13,13
(x, 100, 26, 31, 49) #31,49
(x, 46, 5, 67, 67) #67,67
(x, 134, 49, 23, 23) #23,23
(x, 80, 16, 41, 59) #41,59
(x, 26, 1, 77, 77) #77,77

77
(x, 12, -1, 77, 91) #77,91
(x, 138, 52, 19, 23) #19,23
(x, 102, 28, 37, 41) #37,41
(x, 48, 5, 59, 73) #59,73
(x, 162, 72, 7, 11) #7,11
(x, 108, 31, 29, 43) #29,43
(x, 72, 13, 47, 61) #47,61
(x, 18, 0, 79, 83) #79,83
(x, 78, 0, 13, 89) #13,89
(x, 132, 47, 17, 31) #17,31
(x, 78, 16, 49, 53) #49,53
(x, 42, 4, 67, 71) #67,71

73
(x, 16, -1, 73, 91) #73,91
(x, 124, 41, 19, 37) #19,37
(x, 146, 58, 11, 23) #11,23
(x, 74, 8, 29, 77) #29,77
(x, 74, 14, 47, 59) #47,59
(x, 56, 3, 41, 83) #41,83
(x, 106, 24, 13, 61) #13,61
(x, 106, 30, 31, 43) #31,43
(x, 124, 37, 7, 49) #7,49
(x, 34, 2, 67, 79) #67,79
(x, 74, 0, 17, 89) #17,89
(x, 56, 7, 53, 71) #53,71

71
(x, 18, -1, 71, 91) #71,91
(x, 72, 0, 19, 89) #19,89
(x, 90, 21, 37, 53) #37,53
(x, 90, 13, 17, 73) #17,73
(x, 138, 51, 11, 31) #11,31
(x, 102, 27, 29, 49) #29,49
(x, 120, 36, 13, 47) #13,47
(x, 30, 1, 67, 83) #67,83
(x, 150, 61, 7, 23) #7,23
(x, 78, 15, 41, 61) #41,61
(x, 42, 3, 59, 79) #59,79
(x, 60, 6, 43, 77) #43,77

67
(x, 22, -1, 67, 91) #67,91
(x, 148, 60, 13, 19) #13,19
(x, 112, 34, 31, 37) #31,37
(x, 58, 7, 49, 73) #49,73
(x, 122, 37, 11, 47) #11,47
(x, 68, 4, 29, 83) #29,83
(x, 122, 39, 17, 41) #17,41
(x, 68, 12, 53, 59) #53,59
(x, 32, 2, 71, 77) #71,77
(x, 112, 26, 7, 61) #7,61
(x, 58, 5, 43, 79) #43,79
(x, 68, 0, 23, 89) #23,89

61
(x, 28, -1, 61, 91) #61,91
(x, 82, 8, 19, 79) #19,79
(x, 100, 27, 37, 43) #37,43)
(x, 100, 15, 7, 73) #7,73
(x, 98, 16, 11, 71) #11,71
(x, 62, 0, 29, 89) #29,89
(x, 80, 17, 47, 53) #47,53
(x, 80, 5, 17, 83) #17,83
(x, 100, 19, 13, 67) #13,67
(x, 118, 38, 31, 31) #31,31
(x, 82, 18, 49, 49) #49,49
(x, 80, 9, 23, 77) #23,77
(x, 98, 26, 41, 41) #41,41
(x, 62, 10, 59, 59) #59,59

59
(x, 30, -1, 59, 91) #59,91
(x, 120, 38, 19, 41) #19,41
(x, 66, 7, 37, 77) #37,77
(x, 84, 12, 23, 73) #23,73
(x, 90, 9, 11, 79) #11,79
(x, 90, 19, 29, 61) #29,61
(x, 126, 39, 7, 47) #7,47
(x, 54, 3, 43, 83) #43,83
(x, 114, 31, 13, 53) #13,53
(x, 60, 0, 31, 89) #31,89
(x, 60, 8, 49, 71) #49,71
(x, 96, 18, 17, 67) #17,67

53
(x, 36, -1, 53, 91) #53,91
(x, 144, 57, 17, 19) #17,19
(x, 54, 0, 37, 89) #37,89
(x, 36, 3, 71, 73) #71,73
(x, 156, 67, 11, 13) #11,13
(x, 84, 15, 29, 67) #29,67
(x, 84, 19, 47, 49) #47,49
(x, 66, 4, 31, 83) #31,83
(x, 96, 21, 23, 61) #23,61
(x, 96, 25, 41, 43) #41,43
(x, 114, 28, 7, 59) #7,59
(x, 24, 1, 77, 79) #77,79

49
(x, 40, -1, 49, 91) #49,91
(x, 130, 46, 19, 31) #19,31
(x, 76, 13, 37, 67) #37,67
(x, 94, 14, 13, 73) #13,73
(x, 140, 53, 11, 29) #11,29
(x, 86, 20, 47, 47) #47,47
(x, 14, 0, 83, 83) #83,83
(x, 104, 27, 23, 53) #23,53
(x, 50, 0, 41, 89) #41,89
(x, 50, 6, 59, 71) #59,71
(x, 86, 10, 17, 77) #17,77
(x, 166, 76, 7, 7) #7,7
(x, 94, 24, 43, 43) #43,43
(x, 40, 3, 61, 79) #61,79

47
(x, 42, -1, 47, 91) #47,91
(x, 78, 5, 19, 83) #19,83
(x, 132, 46, 11, 37) #11,37
(x, 78, 11, 29, 73) #29,73
(x, 108, 26, 13, 59) #13,59
(x, 72, 8, 31, 77) #31,77
(x, 108, 30, 23, 49) #23,49
(x, 102, 17, 7, 71) #7,71
(x, 48, 0, 43, 89) #43,89
(x, 102, 23, 17, 61) #17,61
(x, 48, 4, 53, 79) #53,79
(x, 72, 12, 41, 67) #41,67

43
(x, 46, -1, 43, 91) #43,91
(x, 154, 65, 7, 19) #7,19
(x, 64, 6, 37, 79) #37,79
(x, 46, 5, 61, 73) #61,73
(x, 116, 32, 11, 53) #11,53
(x, 134, 49, 17, 29) #17,29
(x, 44, 0, 47, 89) #47,89
(x, 26, 1, 71, 83) #71,83
(x, 136, 50, 13, 31) #13,31
(x, 64, 10, 49, 67) #49,67
(x, 116, 36, 23, 41) #23,41
(x, 44, 4, 59, 77) #59,77

41
(x, 48, -1, 41, 91) #41,91
(x, 42, 0, 49, 89) #49,89
(x, 102, 24, 19, 59) #19,59
(x, 120, 39, 23, 37) #23,37
(x, 108, 25, 11, 61) #11,61
(x, 72, 7, 29, 79) #29,79
(x, 90, 22, 43, 47) #43,47
(x, 150, 62, 13, 17) #13,17
(x, 78, 12, 31, 71) #31,71
(x, 30, 2, 73, 77) #73, 77
(x, 60, 9, 53, 67) #53,67
(x, 90, 6, 7, 83) #7,83

37
(x, 52, -1, 37, 91) #37,91
(x, 88, 13, 19, 73) #19,73
(x, 92, 11, 11, 77) #11,77
(x, 128, 45, 23, 29) #23,29
(x, 92, 23, 41, 47) #41,47
(x, 38, 2, 59, 83) #59,83
(x, 88, 9, 13, 79) #13,79
(x, 142, 54, 7, 31) #7,31
(x, 88, 21, 43, 49) #43,49
(x, 52, 7, 61, 67) #61,67
(x, 92, 15, 17, 71) #17,71
(x, 38, 0, 53, 89) #53,89

31
(x, 58, -1, 31, 91) #31,91
(x, 112, 32, 19, 49) #19,49
(x, 130, 45, 13, 37) #13,37
(x, 40, 4, 67, 73) #67,73
(x, 158, 69, 11, 11) #11,11
(x, 122, 41, 29, 29) #29,29
(x, 50, 3, 47, 83) #47,83
(x, 140, 54, 17, 23) #17,23
(x, 68, 10, 41, 71) #41,71
(x, 32, -, 59, 89) #59,89
(x, 50, 5, 53, 77) #53,77
(x, 130, 43, 7, 43) #7,43
(x, 58, 9, 61, 61) #61,61
(x, 22, 1, 79, 79) #79,79

29
(x, 60, -1, 29, 91) #29,91
(x, 150, 62, 11, 19) #11,19
(x, 96, 25, 37, 47) #37,47
(x, 24, 1, 73, 83) #73,83
(x, 144, 57, 13, 23) #13,23
(x, 90, 20, 31, 59) #31,59
(x, 90, 22, 41, 49) #41,49
(x, 36, 3, 67, 77) #67,77
(x, 156, 67, 7, 17) #7,17
(x, 84, 19, 43, 53) #43,53
(x, 30, 0, 61, 89) #61,89
(x, 30, 2, 71, 79) #71,79


23
(x, 66, -1, 23, 91) #23,91
(x, 84, 10, 19, 77) #19,77
(x, 84, 18, 37, 59) #37,59
(x, 66, 9, 41, 73) #41,73
(x, 126, 41, 11, 43) #11,43
(x, 144, 56, 7, 29) #7,29
(x, 54, 5, 47, 79) #47,79
(x, 36, 2, 61, 83) #61,83
(x, 96, 16, 13, 71) #13,71
(x, 96, 24, 31, 53) #31,53
(x, 114, 33, 17, 49) #17,49
(x, 24, 0, 67, 89) #67,89

19
(x, 70, -1, 19, 91) #19,91
(x, 106, 31, 37, 73) #37,73
(x, 34, 3, 73, 73) #73,73
(x, 110, 27, 11, 59) #11,59
(x, 110, 33, 29, 41) #29,41
(x, 56, 6, 47, 77) #47,77
(x, 74, 5, 23, 83) #23,83
(x, 124, 40, 13, 43) #13,43
(x, 70, 7, 31, 79) #31,79
(x, 70, 13, 49, 61) #49,61
(x, 106, 21, 7, 67) #7,67
(x, 20, 0, 71, 89) #71,89
(x, 74, 15, 53, 53) #53,53
(x, 146, 59, 17, 17) #17,17

17
(x, 72, 1, 17, 91)   #17,91
(x, 108, 29, 19, 53) #19,53
(x, 72, 11, 37, 71)   #37,71
(x, 18, 0, 73, 89)   #73,89
(x, 102, 20, 11, 67)  #11,67
(x, 138, 52, 13, 29) #13,29
(x, 102, 28, 31, 47)  #31,47
(x, 48, 3, 49, 83)  #49,83
(x, 78, 8, 23, 79)  #23,79
(x, 132, 45, 7, 41) #7,41
(x, 78, 16, 43, 59)   #43,59
(x, 42, 4, 61, 77)   #61,77

13
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
	
11
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

7
(x, 82, -1, 7, 91) #7,91
(x, 118, 37, 19, 43) #19,43
(x, 82, 17, 37, 61) #37,61
(x, 28, 2, 73, 79) #73,79
(x, 152, 64, 11, 17) #11,17
(x, 98, 25, 29, 53) #29,53
(x, 62, 9, 47, 71) #47,71
(x, 8, 0, 83, 89) #83,89
(x, 118, 35, 13, 49) #13,49
(x, 82, 15, 31, 67) #31,67
(x, 98, 23, 23, 59) #23,59
(x, 62, 7, 41, 77) #41,77


   

list_A201804 = [i for i,x in enumerate(a) if x != 0]
#print a  #uncomment this line to see the full list (None=primes and 0=composite)
print list_A201804
print "%d is the %dth term of Sloane's A201804." % (list_A201804[-1], len(list_A201804))
