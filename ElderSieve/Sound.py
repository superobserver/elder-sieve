#!/usr/bin/env python
#use timidity output.mid to play audio in Terminal
#use timidity output.mid -Ow -o primes.wav in Terminal to convert *.mid to *.wav

from midiutil.MidiFile import MIDIFile


new_test  =  10000
new_floor =   9000
new_limit = new_floor
#the number in brackets is the note to be played. 
#The prime numbers, less 2,3,5, are given by 24 classes (notes) as:


#toggle the # to change the note categories or even experiment etc

##these notes are primes:

#d = [91]*int(new_test - new_limit)

d = [91]*int(new_test - new_limit) #A224889 Numbers n such that 90n + 91 are prime
e = [89]*int(new_test - new_limit) #A202116 Numbers n such that 90n + 89 is prime.
f = [83]*int(new_test - new_limit) #A196007 Numbers n such that 90n + 83 is prime.
g = [79]*int(new_test - new_limit) #A202112 Numbers n such that 90n + 79 is prime.
h = [77]*int(new_test - new_limit) #A201822 Numbers k such that 90*k + 77 is prime.
i = [73]*int(new_test - new_limit) #A195993 Numbers n such that 90n + 73 is prime.
j = [71]*int(new_test - new_limit) #A202129 Numbers n such that 90n + 71 is prime.
k = [67]*int(new_test - new_limit) #A201817 Numbers k such that 90*k + 67 is prime.
q = [61]*int(new_test - new_limit) ##A202113 Numbers n such that 90n + 61 is prime.
p = [59]*int(new_test - new_limit) #A202101 Numbers n such that 90*n + 59 is prime.
r = [53]*int(new_test - new_limit) #A202114 Numbers n such that 90n + 53 is prime.
s = [49]*int(new_test - new_limit) #A201818 Numbers k such that 90*k + 49 is prime.
t = [47]*int(new_test - new_limit) #A201734 Numbers n such that 90*n + 47 is prime 
u = [43]*int(new_test - new_limit) #A202105 Numbers n such that 90*n + 43 is prime.
v = [41]*int(new_test - new_limit) #A202104 Numbers n such that 90*n + 41 is prime.
w = [37]*int(new_test - new_limit) #A198382 Numbers n such that 90n + 37 is prime.
ww = [31]*int(new_test - new_limit) #A201819 Numbers n such that 90*n + 31 is prime.
www = [29]*int(new_test - new_limit) #A201739 Numbers n such that 90*n + 29 is prime.
wx = [23]*int(new_test - new_limit) #A201820 Numbers k such that 90*k + 23 is prime.
xx = [19]*int(new_test - new_limit) #A196000 Numbers n such that 90n + 19 is prime.
c = [17]*int(new_test - new_limit) #A202115 Numbers n such that 90n + 17 is prime.
b = [13]*int(new_test - new_limit) #A201816 Numbers k such that 90*k + 13 is prime.
a = [11]*int(new_test - new_limit) #A201804 Numbers k such that 90*k + 11 are prime.
xy = [7]*int(new_test - new_limit) #A202110 Numbers n such that 90*n + 7 is prime.

#^--- all the primes

composites_base10 = []



#Same patterns, different notes:

#a = [37]*int(new_test) #11
#b = [39]*int(new_test) #13
#c = [40]*int(new_test) #17
#d = [75]*int(new_test) #91
#e = [73]*int(new_test)
#f = [71]*int(new_test)
#g = [69]*int(new_test)
#h = [68]*int(new_test)
#i = [66]*int(new_test)
#j = [64]*int(new_test)
#k = [63]*int(new_test)
#p = [61]*int(new_test)
#q = [59]*int(new_test)
#r = [57]*int(new_test)
#s = [56]*int(new_test)
#t = [54]*int(new_test)
#u = [52]*int(new_test)
#v = [51]*int(new_test)
#w = [49]*int(new_test)
#ww = [47]*int(new_test)
#www = [45]*int(new_test)
#wx = [44]*int(new_test)
#xx = [42]*int(new_test)
#xy = [35]*int(new_test)
##^--- still all the primes, just different notes

#special=A255491 Numbers k such that 90*k+1 is composite.
#here you also have to toggle the variable value at lines 105, 111, 114. Once you see it you will know and can erase this line

#d = [0]*int(new_test) #A224889 Numbers n such that 90n + 91 are prime
#e = [0]*int(new_test) #A202116 Numbers n such that 90n + 89 is prime.
#f = [0]*int(new_test) #A196007 Numbers n such that 90n + 83 is prime.
#g = [0]*int(new_test) #A202112 Numbers n such that 90n + 79 is prime.
#h = [0]*int(new_test) #A201822 Numbers k such that 90*k + 77 is prime.
#i = [0]*int(new_test) #A195993 Numbers n such that 90n + 73 is prime.
#j = [0]*int(new_test) #A202129 Numbers n such that 90n + 71 is prime.
#k = [0]*int(new_test) #A201817 Numbers k such that 90*k + 67 is prime.
#q = [0]*int(new_test) ##A202113 Numbers n such that 90n + 61 is prime.
#p = [0]*int(new_test) #A202101 Numbers n such that 90*n + 59 is prime.
#r = [0]*int(new_test) #A202114 Numbers n such that 90n + 53 is prime.
#s = [0]*int(new_test) #A201818 Numbers k such that 90*k + 49 is prime.
#t = [0]*int(new_test) #A201734 Numbers n such that 90*n + 47 is prime 
#u = [0]*int(new_test) #A202105 Numbers n such that 90*n + 43 is prime.
#v = [0]*int(new_test) #A202104 Numbers n such that 90*n + 41 is prime.
#w = [0]*int(new_test) #A198382 Numbers n such that 90n + 37 is prime.
#ww = [0]*int(new_test) #A201819 Numbers n such that 90*n + 31 is prime.
#www = [0]*int(new_test) #A201739 Numbers n such that 90*n + 29 is prime.
#wx = [0]*int(new_test) #A201820 Numbers k such that 90*k + 23 is prime.
#xx = [0]*int(new_test) #A196000 Numbers n such that 90n + 19 is prime.
#c = [0]*int(new_test) #A202115 Numbers n such that 90n + 17 is prime.
#b = [0]*int(new_test) #A201816 Numbers k such that 90*k + 13 is prime.
#a = [0]*int(new_test) #A201804 Numbers k such that 90*k + 11 are prime.
#xy = [0]*int(new_test) #A202110 Numbers n such that 90*n + 7 is prime.
#^--- all the primes


#maps composites to lists
def drLD(x, l, m, z, o, list_var, primitive_var):      
  y = 90*(x*x) - l*x + m 
  if y > new_test:
    return
  if y >= new_floor:
    if y <= new_test:
      print y
      try:
        list_var[y-new_floor] = 0# primitive_var #0
      except:
        pass
  
  for n in xrange (1, new_test):
    new_y = y+((z+(90*(x-1)))*n)
    if new_y <= new_test:
      if new_y >= new_limit:
        try:
          list_var[new_y-new_floor] = 0# z #0
        except:
          pass
    new2_y = y+((o+(90*(x-1)))*n)   
    if new2_y <= new_test: 
      if new_y >= new_floor:
        try:    
          list_var[new2_y-new_floor] = 0#o #0    
        except:
          pass 
    if new_y > new_test:
      return
    else:
      pass





for x in xrange(1, 1056): # 10000 = 12; 100000 = 36; 1,000,000 = 108; 10,000,000 = 336; 100,000,000 = 1056; 1,000,000,000 = "Hey I need to checksum these tables, all hand-entered
 

#11 = a
    drLD(x, 120, 34, 7, 53, a, 11)  #7,53  @4,  154 1
    drLD(x, 132, 48, 19, 29, a, 11) #19,29 @6,  144 2
    drLD(x, 120, 38, 17, 43, a, 11) #17,43 @8,  158 3
    drLD(x, 90, 11, 13, 77, a, 11)  #13,77 @11, 191 4
    drLD(x, 78, -1, 11, 91, a, 11)  #11,91 @11, 203 5
    drLD(x, 108, 32, 31, 41, a, 11) #31,41 @14, 176 6
    drLD(x, 90, 17, 23, 67, a, 11)  #23,67 @17, 197 7
    drLD(x, 72, 14, 49, 59, a, 11)  #49,59 @32, 230 8
    drLD(x, 60, 4, 37, 83, a, 11)   #37,83 @34, 244 9
    drLD(x, 60, 8, 47, 73, a, 11)   #47,73 @38, 248 10
    drLD(x, 48, 6, 61, 71, a, 11)   #61,71 @48, 270 11
    drLD(x, 12, 0, 79, 89, a, 11)   #79,89 @78, 336 12


#13 = b
    drLD(x, 76, -1, 13, 91, b, 13)   #13,91
    drLD(x, 94, 18, 19, 67, b, 13)  #19,67
    drLD(x, 94, 24, 37, 49, b, 13)  #37,49
    drLD(x, 76, 11, 31, 73, b, 13)  #31,73
    drLD(x, 86, 6, 11, 83, b, 13)   #11,83
    drLD(x, 104, 29, 29, 47, b, 13) #29,47
    drLD(x, 86, 14, 23, 71, b, 13)  #23,71
    drLD(x, 86, 20, 41, 53, b, 13)  #41,53
    drLD(x, 104, 25, 17, 59, b, 13) #17,59
    drLD(x, 14, 0, 77, 89, b, 13)   #77,89
    drLD(x, 94, 10, 7, 79, b, 13)   #7,79
    drLD(x, 76, 15, 43, 61, b, 13) #43,61

#17 = c
    drLD(x, 72, -1, 17, 91, c, 17)   #17,91
    drLD(x, 108, 29, 19, 53, c, 17) #19,53
    drLD(x, 72, 11, 37, 71, c, 17)   #37,71
    drLD(x, 18, 0, 73, 89, c, 17)   #73,89
    drLD(x, 102, 20, 11, 67, c, 17)  #11,67
    drLD(x, 138, 52, 13, 29, c, 17) #13,29
    drLD(x, 102, 28, 31, 47, c, 17)  #31,47
    drLD(x, 48, 3, 49, 83, c, 17)  #49,83
    drLD(x, 78, 8, 23, 79, c, 17)  #23,79
    drLD(x, 132, 45, 7, 41, c, 17) #7,41
    drLD(x, 78, 16, 43, 59, c, 17)   #43,59
    drLD(x, 42, 4, 61, 77, c, 17) #61,77   

#91 = d
    drLD(x, 2, 0, 91, 91, d, 91) #91,91
    drLD(x, 142, 56, 19, 19, d, 91) #19,19
    drLD(x, 70, 10, 37, 73, d, 91) #37, 73
    drLD(x, 128, 43, 11, 41, d, 91) #11, 41
    drLD(x, 92, 21, 29, 59, d, 91) #29,59
    drLD(x, 110, 32, 23, 47, d, 91) #23,47
    drLD(x, 20, 1, 77, 83, d, 91) #77,83
    drLD(x, 160, 71, 7, 13, d, 91) #7,13
    drLD(x, 88, 19, 31, 61, d, 91) #31,61
    drLD(x, 52, 5, 49, 79, d, 91) #49,79
    drLD(x, 70, 12, 43, 67, d, 91) #43,67
    drLD(x, 110, 30, 17, 53, d, 91) #17,53
    drLD(x, 38, 4, 71, 71, d, 91) #71,71
    drLD(x, 2, 0, 89, 89, d, 91) #89,89

# 89 = e
    drLD(x, 1, 0, 89, 91, e, 89) #89,91
    drLD(x, 90, 14, 19, 71, e, 89) #19,71
    drLD(x, 126, 42, 17, 37, e, 89) #17,37
    drLD(x, 54, 6, 53, 73, e, 89) #53,73
    drLD(x, 120, 35, 11, 49, e, 89) #11,49
    drLD(x, 120, 39, 29, 31, e, 89) #29,31
    drLD(x, 66, 10, 47, 67, e, 89) #47,67
    drLD(x, 84, 5, 13, 83, e, 89) #13,83
    drLD(x, 114, 34, 23, 43, e, 89) #23,43
    drLD(x, 60, 5, 41, 79, e, 89) #41,79
    drLD(x, 60, 9, 59, 61, e, 89) #59,61
    drLD(x, 96, 11, 7, 77, e, 89) #7,77

# 83 = f
    drLD(x, 6, -1, 83, 91, f, 83) #83,91
    drLD(x, 114, 33, 19, 47, f, 83) #19,47
    drLD(x, 114, 35, 37, 29, f, 83) #37,29
    drLD(x, 96, 14, 11, 73, f, 83) #11,73
    drLD(x, 126, 41, 13, 41, f, 83) #13,41
    drLD(x, 126, 43, 23, 31, f, 83) #23,31
    drLD(x, 54, 5, 49, 77, f, 83) #49,77
    drLD(x, 54, 7, 59, 67, f, 83) #59,67
    drLD(x, 84, 0, 7, 89, f, 83) #7,89
    drLD(x, 66, 9, 43, 71, f, 83) #43,71
    drLD(x, 66, 11, 53, 61, f, 83) #53,61
    drLD(x, 84, 8, 17, 79, f, 83) #17,79



# 79 = g
    drLD(x, 10, -1, 79, 91, g, 79) #79,91
    drLD(x, 100, 22, 19, 61, g, 79) #19,61
    drLD(x, 136, 48, 7, 37, g, 79) #7,37
    drLD(x, 64, 8, 43, 73, g, 79) #43,73
    drLD(x, 80, 0, 11, 89, g, 79) #11,89
    drLD(x, 80, 12, 29, 71, g, 79) #29,71
    drLD(x, 116, 34, 17, 47, g, 79) #17,47
    drLD(x, 44, 2, 53, 83, g, 79) #53,83
    drLD(x, 154, 65, 13, 13, g, 79) #13,13
    drLD(x, 100, 26, 31, 49, g, 79) #31,49
    drLD(x, 46, 5, 67, 67, g, 79) #67,67
    drLD(x, 134, 49, 23, 23, g, 79) #23,23
    drLD(x, 80, 16, 41, 59, g, 79) #41,59
    drLD(x, 26, 1, 77, 77, g, 79) #77,77


# 77 = h
    drLD(x, 12, -1, 77, 91, h, 79) #77,91
    drLD(x, 138, 52, 19, 23, h, 79) #19,23
    drLD(x, 102, 28, 37, 41, h, 79) #37,41
    drLD(x, 48, 5, 59, 73, h, 79) #59,73
    drLD(x, 162, 72, 7, 11, h, 79) #7,11
    drLD(x, 108, 31, 29, 43, h, 79) #29,43
    drLD(x, 72, 13, 47, 61, h, 79) #47,61
    drLD(x, 18, 0, 79, 83, h, 79) #79,83
    drLD(x, 78, 0, 13, 89, h, 79) #13,89
    drLD(x, 132, 47, 17, 31, h, 79) #17,31
    drLD(x, 78, 16, 49, 53, h, 79) #49,53
    drLD(x, 42, 4, 67, 71, h, 79) #67,71

# 73 = i
    drLD(x, 16, -1, 73, 91, i, 73) #73,91
    drLD(x, 124, 41, 19, 37, i, 73) #19,37
    drLD(x, 146, 58, 11, 23, i, 73) #11,23
    drLD(x, 74, 8, 29, 77, i, 73) #29,77
    drLD(x, 74, 14, 47, 59, i, 73) #47,59
    drLD(x, 56, 3, 41, 83, i, 73) #41,83
    drLD(x, 106, 24, 13, 61, i, 73) #13,61
    drLD(x, 106, 30, 31, 43, i, 73) #31,43
    drLD(x, 124, 37, 7, 49, i, 73) #7,49
    drLD(x, 34, 2, 67, 79, i, 73) #67,79
    drLD(x, 74, 0, 17, 89, i, 73) #17,89
    drLD(x, 56, 7, 53, 71, i, 73) #53,71


# 71 = j
    drLD(x, 18, -1, 71, 91, j, 71) #71,91
    drLD(x, 72, 0, 19, 89, j, 71) #19,89
    drLD(x, 90, 21, 37, 53, j, 71) #37,53
    drLD(x, 90, 13, 17, 73, j, 71) #17,73
    drLD(x, 138, 51, 11, 31, j, 71) #11,31
    drLD(x, 102, 27, 29, 49, j, 71) #29,49
    drLD(x, 120, 36, 13, 47, j, 71) #13,47
    drLD(x, 30, 1, 67, 83, j, 71) #67,83
    drLD(x, 150, 61, 7, 23, j, 71) #7,23
    drLD(x, 78, 15, 41, 61, j, 71) #41,61
    drLD(x, 42, 3, 59, 79, j, 71) #59,79
    drLD(x, 60, 6, 43, 77, j, 71) #43,77

# 67 = k
    drLD(x, 22, -1, 67, 91, k, 67) #67,91
    drLD(x, 148, 60, 13, 19, k, 67) #13,19
    drLD(x, 112, 34, 31, 37, k, 67) #31,37
    drLD(x, 58, 7, 49, 73, k, 67) #49,73
    drLD(x, 122, 37, 11, 47, k, 67) #11,47
    drLD(x, 68, 4, 29, 83, k, 67) #29,83
    drLD(x, 122, 39, 17, 41, k, 67) #17,41
    drLD(x, 68, 12, 53, 59, k, 67) #53,59
    drLD(x, 32, 2, 71, 77, k, 67) #71,77
    drLD(x, 112, 26, 7, 61, k, 67) #7,61
    drLD(x, 58, 5, 43, 79, k, 67) #43,79
    drLD(x, 68, 0, 23, 89, k, 67) #23,89

# 61 = p
    drLD(x, 28, -1, 61, 91, p, 61) #61,91
    drLD(x, 82, 8, 19, 79, p, 61) #19,79
    drLD(x, 100, 27, 37, 43, p, 61) #37,43)
    drLD(x, 100, 15, 7, 73, p, 61) #7,73
    drLD(x, 98, 16, 11, 71, p, 61) #11,71
    drLD(x, 62, 0, 29, 89, p, 61) #29,89
    drLD(x, 80, 17, 47, 53, p, 61) #47,53
    drLD(x, 80, 5, 17, 83, p, 61) #17,83
    drLD(x, 100, 19, 13, 67, p, 61) #13,67
    drLD(x, 118, 38, 31, 31, p, 61) #31,31
    drLD(x, 82, 18, 49, 49, p, 61) #49,49
    drLD(x, 80, 9, 23, 77, p, 61) #23,77
    drLD(x, 98, 26, 41, 41, p, 61) #41,41
    drLD(x, 62, 10, 59, 59, p, 61) #59,59


# 59 = q
    drLD(x, 30, -1, 59, 91, q, 59) #59,91
    drLD(x, 120, 38, 19, 41, q, 59) #19,41
    drLD(x, 66, 7, 37, 77, q, 59) #37,77
    drLD(x, 84, 12, 23, 73, q, 59) #23,73
    drLD(x, 90, 9, 11, 79, q, 59) #11,79
    drLD(x, 90, 19, 29, 61, q, 59) #29,61
    drLD(x, 126, 39, 7, 47, q, 59) #7,47
    drLD(x, 54, 3, 43, 83, q, 59) #43,83
    drLD(x, 114, 31, 13, 53, q, 59) #13,53
    drLD(x, 60, 0, 31, 89, q, 59) #31,89
    drLD(x, 60, 8, 49, 71, q, 59) #49,71
    drLD(x, 96, 18, 17, 67, q, 59) #17,67

# 53 = r
    drLD(x, 36, -1, 53, 91, r, 53) #53,91
    drLD(x, 144, 57, 17, 19, r, 53) #17,19
    drLD(x, 54, 0, 37, 89, r, 53) #37,89
    drLD(x, 36, 3, 71, 73, r, 53) #71,73
    drLD(x, 156, 67, 11, 13, r, 53) #11,13
    drLD(x, 84, 15, 29, 67, r, 53) #29,67
    drLD(x, 84, 19, 47, 49, r, 53) #47,49
    drLD(x, 66, 4, 31, 83, r, 53) #31,83
    drLD(x, 96, 21, 23, 61, r, 53) #23,61
    drLD(x, 96, 25, 41, 43, r, 53) #41,43
    drLD(x, 114, 28, 7, 59, r, 53) #7,59
    drLD(x, 24, 1, 77, 79, r, 53) #77,79

# 49 = s
    drLD(x, 40, -1, 49, 91, s, 49) #49,91
    drLD(x, 130, 46, 19, 31, s, 49) #19,31
    drLD(x, 76, 13, 37, 67, s, 49) #37,67
    drLD(x, 94, 14, 13, 73, s, 49) #13,73
    drLD(x, 140, 53, 11, 29, s, 49) #11,29
    drLD(x, 86, 20, 47, 47, s, 49) #47,47
    drLD(x, 14, 0, 83, 83, s, 49) #83,83
    drLD(x, 104, 27, 23, 53, s, 49) #23,53
    drLD(x, 50, 0, 41, 89, s, 49) #41,89
    drLD(x, 50, 6, 59, 71, s, 49) #59,71
    drLD(x, 86, 10, 17, 77, s, 49) #17,77
    drLD(x, 166, 76, 7, 7, s, 49) #7,7
    drLD(x, 94, 24, 43, 43, s, 49) #43,43
    drLD(x, 40, 3, 61, 79, s, 49) #61,79

# 47 = t
    drLD(x, 42, -1, 47, 91, t, 47) #47,91
    drLD(x, 78, 5, 19, 83, t, 47) #19,83
    drLD(x, 132, 46, 11, 37, t, 47) #11,37
    drLD(x, 78, 11, 29, 73, t, 47) #29,73
    drLD(x, 108, 26, 13, 59, t, 47) #13,59
    drLD(x, 72, 8, 31, 77, t, 47) #31,77
    drLD(x, 108, 30, 23, 49, t, 47) #23,49
    drLD(x, 102, 17, 7, 71, t, 47) #7,71
    drLD(x, 48, 0, 43, 89, t, 47) #43,89
    drLD(x, 102, 23, 17, 61, t, 47) #17,61
    drLD(x, 48, 4, 53, 79, t, 47) #53,79
    drLD(x, 72, 12, 41, 67, t, 47) #41,67


# 43 = u
    drLD(x, 46, -1, 43, 91, u, 43) #43,91
    drLD(x, 154, 65, 7, 19, u, 43) #7,19
    drLD(x, 64, 6, 37, 79, u, 43) #37,79
    drLD(x, 46, 5, 61, 73, u, 43) #61,73
    drLD(x, 116, 32, 11, 53, u, 43) #11,53
    drLD(x, 134, 49, 17, 29, u, 43) #17,29
    drLD(x, 44, 0, 47, 89, u, 43) #47,89
    drLD(x, 26, 1, 71, 83, u, 43) #71,83
    drLD(x, 136, 50, 13, 31, u, 43) #13,31
    drLD(x, 64, 10, 49, 67, u, 43) #49,67
    drLD(x, 116, 36, 23, 41, u, 43) #23,41
    drLD(x, 44, 4, 59, 77, u, 43) #59,77

# 41 = v
    drLD(x, 48, -1, 41, 91, v, 41) #41,91
    drLD(x, 42, 0, 49, 89, v, 41) #49,89
    drLD(x, 102, 24, 19, 59, v, 41) #19,59
    drLD(x, 120, 39, 23, 37, v, 41) #23,37
    drLD(x, 108, 25, 11, 61, v, 41) #11,61
    drLD(x, 72, 7, 29, 79, v, 41) #29,79
    drLD(x, 90, 22, 43, 47, v, 41) #43,47
    drLD(x, 150, 62, 13, 17, v, 41) #13,17
    drLD(x, 78, 12, 31, 71, v, 41) #31,71
    drLD(x, 30, 2, 73, 77, v, 41) #73, 77
    drLD(x, 60, 9, 53, 67, v, 41) #53,67
    drLD(x, 90, 6, 7, 83, v, 41) #7,83

# 37 = w
    drLD(x, 52, -1, 37, 91, w, 37) #37,91
    drLD(x, 88, 13, 19, 73, w, 37) #19,73
    drLD(x, 92, 11, 11, 77, w, 37) #11,77
    drLD(x, 128, 45, 23, 29, w, 37) #23,29
    drLD(x, 92, 23, 41, 47, w, 37) #41,47
    drLD(x, 38, 2, 59, 83, w, 37) #59,83
    drLD(x, 88, 9, 13, 79, w, 37) #13,79
    drLD(x, 142, 54, 7, 31, w, 37) #7,31
    drLD(x, 88, 21, 43, 49, w, 37) #43,49
    drLD(x, 52, 7, 61, 67, w, 37) #61,67
    drLD(x, 92, 15, 17, 71, w, 37) #17,71
    drLD(x, 38, 0, 53, 89, w, 37) #53,89

# 31 = ww
    drLD(x, 58, -1, 31, 91, ww, 31) #31,91
    drLD(x, 112, 32, 19, 49, ww, 31) #19,49
    drLD(x, 130, 45, 13, 37, ww, 31) #13,37
    drLD(x, 40, 4, 67, 73, ww, 31) #67,73
    drLD(x, 158, 69, 11, 11, ww, 31) #11,11
    drLD(x, 122, 41, 29, 29, ww, 31) #29,29
    drLD(x, 50, 3, 47, 83, ww, 31) #47,83
    drLD(x, 140, 54, 17, 23, ww, 31) #17,23
    drLD(x, 68, 10, 41, 71, ww, 31) #41,71
    drLD(x, 32, 0, 59, 89, ww, 31) #59,89
    drLD(x, 50, 5, 53, 77, ww, 31) #53,77
    drLD(x, 130, 43, 7, 43, ww, 31) #7,43
    drLD(x, 58, 9, 61, 61, ww, 31) #61,61
    drLD(x, 22, 1, 79, 79, ww, 31) #79,79

# 29 = www
    drLD(x, 60, -1, 29, 91, www, 29) #29,91
    drLD(x, 150, 62, 11, 19, www, 29) #11,19
    drLD(x, 96, 25, 37, 47, www, 29) #37,47
    drLD(x, 24, 1, 73, 83, www, 29) #73,83
    drLD(x, 144, 57, 13, 23, www, 29) #13,23
    drLD(x, 90, 20, 31, 59, www, 29) #31,59
    drLD(x, 90, 22, 41, 49, www, 29) #41,49
    drLD(x, 36, 3, 67, 77, www, 29) #67,77
    drLD(x, 156, 67, 7, 17, www, 29) #7,17
    drLD(x, 84, 19, 43, 53, www, 29) #43,53
    drLD(x, 30, 0, 61, 89, www, 29) #61,89
    drLD(x, 30, 2, 71, 79, www, 29) #71,79

# 23 = wx
    drLD(x, 66, -1, 23, 91, wx, 23) #23,91
    drLD(x, 84, 10, 19, 77, wx, 23) #19,77
    drLD(x, 84, 18, 37, 59, wx, 23) #37,59
    drLD(x, 66, 9, 41, 73, wx, 23) #41,73
    drLD(x, 126, 41, 11, 43, wx, 23) #11,43
    drLD(x, 144, 56, 7, 29, wx, 23) #7,29
    drLD(x, 54, 5, 47, 79, wx, 23) #47,79
    drLD(x, 36, 2, 61, 83, wx, 23) #61,83
    drLD(x, 96, 16, 13, 71, wx, 23) #13,71
    drLD(x, 96, 24, 31, 53, wx, 23) #31,53
    drLD(x, 114, 33, 17, 49, wx, 23) #17,49
    drLD(x, 24, 0, 67, 89, wx, 23) #67,89

# 19 = xx
    drLD(x, 70, -1, 19, 91, xx, 19) #19,91
    drLD(x, 106, 31, 37, 73, xx, 19) #37,73
    drLD(x, 34, 3, 73, 73, xx, 19) #73,73
    drLD(x, 110, 27, 11, 59, xx, 19) #11,59
    drLD(x, 110, 33, 29, 41, xx, 19) #29,41
    drLD(x, 56, 6, 47, 77, xx, 19) #47,77
    drLD(x, 74, 5, 23, 83, xx, 19) #23,83
    drLD(x, 124, 40, 13, 43, xx, 19) #13,43
    drLD(x, 70, 7, 31, 79, xx, 19) #31,79
    drLD(x, 70, 13, 49, 61, xx, 19) #49,61
    drLD(x, 106, 21, 7, 67, xx, 19) #7,67
    drLD(x, 20, 0, 71, 89, xx, 19) #71,89
    drLD(x, 74, 15, 53, 53, xx, 19) #53,53
    drLD(x, 146, 59, 17, 17, xx, 19) #17,17


# 7 = xy
    drLD(x, 82, -1, 7, 91, xy, 7) #7,91
    drLD(x, 118, 37, 19, 43, xy, 7) #19,43
    drLD(x, 82, 17, 37, 61, xy, 7) #37,61
    drLD(x, 28, 2, 73, 79, xy, 7) #73,79
    drLD(x, 152, 64, 11, 17, xy, 7) #11,17
    drLD(x, 98, 25, 29, 53, xy, 7) #29,53
    drLD(x, 62, 9, 47, 71, xy, 7) #47,71
    drLD(x, 8, 0, 83, 89, xy, 7) #83,89
    drLD(x, 118, 35, 13, 49, xy, 7) #13,49
    drLD(x, 82, 15, 31, 67, xy, 7) #31,67
    drLD(x, 98, 23, 23, 59, xy, 7) #23,59
    drLD(x, 62, 7, 41, 77, xy, 7) #41,77


# Just an example
#try:
    # import version included with old SymPy
#    from sympy.mpmath import mp
#except ImportError:
    # import newer version
#    from mpmath import mp
#mp.dps = 1000  # set number of digits

# Create the MIDIFile Object with 24 tracks
MyMIDI = MIDIFile(23)

instrument_var = 105 #Sitar

#piano
instrument_var_acousticgrand = 1 #acoustic grand piano
instrument_var_brightacousticpiano = 2
instrument_var_electricgrandpiano = 3
instrument_var_honkytonkpiano = 4
instrument_var_electricpiano1 = 5
instrument_var_electricpiano2 = 6
instrument_var_harpsichord = 7
instrument_var_clavinet = 8 #Clavinet

#chromatic percussion
instrument_var_celestra = 9
instrument_var_glockenspiel = 10 #Glockenspiel
instrument_var_musicbox = 11
instrument_var_vibraphone = 12
instrument_var_marima = 13
instrument_var_xylophone = 14 #xylophone
instrument_var_tubularbells = 15
instrument_var_dulcimer = 16


#organ
instrument_var_drawbarorgan = 17
instrument_var_percussiveorgan = 18
instrument_var_rockorgan = 19
instrument_var_churchorgan = 20
instrument_var_reedorgan = 21
instrument_var_accordion = 22
instrument_var_harmonica = 23
instrument_var_tangoaccordion = 34

#guitar
instrument_var_acousticnylonguitar = 25
instrument_var_acousticsteelguitar = 26
instrument_var_electricjazzguitar = 27
instrument_var_electriccleanguitar = 28
instrument_var_electricmutedguitar = 29
instrument_var_overdrivenguitar = 30
instrument_var_distortionguitar = 31
instrument_var_harmonicsguitar = 32

#bass
instrument_var_acousticbass = 33
instrument_var_fingerelectricbass = 34
instrument_var_pickelectricbass = 35
instrument_var_fretlessbass = 36
instrument_var_slap1bass = 37
instrument_var_slap2bass = 38
instrument_var_synth1bass = 38
instrument_var_synth2bass = 40

#strings
instrument_var_violin = 41 #violin
instrument_var_viola = 42 #viola
instrument_var_cello = 43 #Cello
instrument_var_contrabass = 44 #Contrabase
instrument_var_tremulostrings = 45
instrument_var_pizzicatostrings = 46
instrument_var_orchestralharp = 47 #orchestral harp
instrument_var_timpani = 48
instrument_var_stringensemble1 = 49 #string ensemble
instrument_var_stringensemble2 = 50
instrument_var_synthstrings1 = 51
instrument_var_synthstrings2 = 52
instrument_var_choralahh = 53
instrument_var_voiceooh = 54
instrument_var_synthvoice = 55
instrument_var_orchestrahit = 56

#brass
instrument_var_trumpet = 57 #trumpet
instrument_var_trombone = 58 #trombone
instrument_var_tuba = 59
instrument_var_mutedtrumpet = 60
instrument_var_frenchhorn = 61 #french horn
instrument_var_brasssection = 62
instrument_var_synthbrass1 = 63
instrument_var_synthbrass2 = 64

#reed
instrument_var_sopranosax = 65 #sopranosax
instrument_var_altosax = 66
instrument_var_tenorsax = 67
instrument_var_baritonesax = 68
instrument_var_oboe = 69 #Oboe
instrument_var_englishhorn = 70 #English Horn
instrument_var_bassoon = 71 #bassoon
instrument_var_clarinet = 72

#pipe
instrument_var_piccolo = 73
instrument_var_flute = 74
instrument_var_recorder = 75
instrument_var_panflute = 76
instrument_var_blownbottle = 77
instrument_var_shakuhachi = 78
instrument_var_whistle = 79
instrument_var_ocarina = 80

#synthlead
instrument_var_square = 81
instrument_var_sawtooth = 82
instrument_var_calliope = 83
instrument_var_chiff = 84
instrument_var_charang = 85
instrument_var_voice = 86
instrument_var_fifths = 87
instrument_var_baselead = 88

#synthpad
instrument_var_newagepad = 89 
instrument_var_warmpad = 90
instrument_var_polysynthpad = 91
instrument_var_choirpad = 92
instrument_var_bowedpad = 93
instrument_var_metallicpad = 94 
instrument_var_halopad = 95
instrument_var_sweeppad = 96

#syntheffects
instrument_var_rain = 97
instrument_var_soundtrack = 98
instrument_var_crystal = 99
instrument_var_atmosphere =100 
instrument_var_brightness = 101
instrument_var_goblins = 102
instrument_var_echoes = 103
instrument_var_scifi = 104

#ethnic
instrument_var_sitar = 105
instrument_var_banjo = 106
instrument_var_shamisen = 107
instrument_var_koto = 108
instrument_var_kalimba = 109
instrument_var_bagpipe = 110
instrument_var_fiddle = 111
instrument_var_shanai = 112

#percussive
instrument_var_tinklebell = 113
instrument_var_agogo = 114
instrument_var_steeldrums = 115
instrument_var_woodblock = 116
instrument_var_taikodrum = 117
instrument_var_melodictom = 118
instrument_var_synthdrum = 119

#soundeffects
instrument_var_reversesymbal = 120 
instrument_var_guitarfretnoise = 121
instrument_var_breathnoise = 122
instrument_var_seashore = 123
instrument_var_birdtweet = 124
instrument_var_telephonering = 125 
instrument_var_helicopter = 126
instrument_var_applause = 127
instrument_var_gunshot = 128




MyMIDI.addProgramChange(0, 0, 0, int(instrument_var_shakuhachi))
MyMIDI.addProgramChange(0, 1, 0, int(instrument_var_shakuhachi))
MyMIDI.addProgramChange(0, 2, 0, int(instrument_var_shakuhachi))
MyMIDI.addProgramChange(0, 3, 0, int(instrument_var_shakuhachi))
MyMIDI.addProgramChange(0, 4, 0, int(instrument_var_shakuhachi))
MyMIDI.addProgramChange(0, 5, 0, int(instrument_var_shakuhachi))
MyMIDI.addProgramChange(0, 6, 0, int(instrument_var_shakuhachi))
MyMIDI.addProgramChange(0, 7, 0, int(instrument_var_shakuhachi))
MyMIDI.addProgramChange(0, 8, 0, int(instrument_var_shakuhachi))
MyMIDI.addProgramChange(0, 9, 0, int(instrument_var_shakuhachi))
MyMIDI.addProgramChange(0, 10, 0, int(instrument_var_shakuhachi))
MyMIDI.addProgramChange(0, 11, 0, int(instrument_var_shakuhachi))
MyMIDI.addProgramChange(0, 12, 0, int(instrument_var_shakuhachi))
MyMIDI.addProgramChange(0, 13, 0, int(instrument_var_shakuhachi))
MyMIDI.addProgramChange(0, 14, 0, int(instrument_var_shakuhachi))
MyMIDI.addProgramChange(0, 15, 0, int(instrument_var_shakuhachi))
MyMIDI.addProgramChange(0, 16, 0, int(instrument_var_shakuhachi))
MyMIDI.addProgramChange(0, 17, 0, int(instrument_var_shakuhachi))
MyMIDI.addProgramChange(0, 18, 0, int(instrument_var_shakuhachi))
MyMIDI.addProgramChange(0, 19, 0, int(instrument_var_shakuhachi))
MyMIDI.addProgramChange(0, 20, 0, int(instrument_var_shakuhachi))
MyMIDI.addProgramChange(0, 21, 0, int(instrument_var_shakuhachi))
MyMIDI.addProgramChange(0, 22, 0, int(instrument_var_shakuhachi))
MyMIDI.addProgramChange(0, 23, 0, int(instrument_var_shakuhachi))




track1 = 0
channel1 = 0
track2 = 0
channel2 = 0
track3 = 0
channel3 = 0
track4 = 0
channel4 = 0
track5 = 0
channel5 = 0
track6 = 0
channel6 = 0
track7 = 0
channel7 = 0
track8 = 0
channel8 = 0
track9 = 0
channel9 = 0
track10 = 0
channel10 = 0
track11 = 0
channel11 = 0
track12 = 0
channel12 = 0
track13 = 0
channel13 = 0
track14 = 0
channel14 = 0
track15 = 0
channel15 = 0
track16 = 0
channel16 = 0
track17 = 0
channel17 = 0
track18 = 0
channel18 = 0
track19 = 0
channel19 = 0
track20 = 0
channel20 = 0
track21 = 0
channel21 = 0
track22 = 0
channel22 = 0
track23 = 0
channel23 = 0
track24 = 0
channel24 = 0

#set your variable global time variable. The beat the write output starts at
time_var = 0
#time_var = 0
#time_var_delta = 111 #example

#duration variable setup
duration_var =1

#volume variable setup
volume_var = 60

#pitch variable setup
pitch_var = 0

#second time variable
#time2_var = 10000

pitch1 = int(pitch_var)
time1 = int(time_var) # OR int(time_var_delta)
duration1 = int(duration_var) 
volume1 = int(volume_var)

pitch2 = int(pitch_var)
time2 = int(time_var)
duration2 = int(duration_var)
volume2 = int(volume_var)

pitch3 = int(pitch_var)
time3 = int(time_var)
duration3 = int(duration_var)
volume3 = int(volume_var)

pitch4 = int(pitch_var)
time4 = int(time_var)
duration4 = int(duration_var)
volume4 = int(volume_var)

pitch5 = int(pitch_var)
time5 = int(time_var)
duration5 = int(duration_var)
volume5 = int(volume_var)

pitch6 = int(pitch_var)
time6 = int(time_var)
duration6 = int(duration_var)
volume6 = int(volume_var)

pitch7 = int(pitch_var)
time7 = int(time_var)
duration7 = int(duration_var)
volume7 = int(volume_var)

pitch8 = int(pitch_var)
time8 = int(time_var)
duration8 = int(duration_var)
volume8 = int(volume_var)

pitch9 = int(pitch_var)
time9 = int(time_var)
duration9 = int(duration_var)
volume9 = int(volume_var)

pitch10 = int(pitch_var)
time10 = int(time_var)
duration10 = int(duration_var)
volume10 = int(volume_var)

pitch11 = int(pitch_var)
time11 = int(time_var)
duration11 = int(duration_var)
volume11 = int(volume_var)

pitch12 = int(pitch_var)
time12 = int(time_var)
duration12 = int(duration_var)
volume12 = int(volume_var)

pitch13 = int(pitch_var)
time13 = int(time_var)
duration13 = int(duration_var)
volume13 = int(volume_var)

pitch14 = int(pitch_var)
time14 = int(time_var)
duration14 = int(duration_var)
volume14 = int(volume_var)

pitch15 = int(pitch_var)
time15 = int(time_var)
duration15 = int(duration_var)
volume15 = int(volume_var)

pitch16 = int(pitch_var)
time16 = int(time_var)
duration16 = int(duration_var)
volume16 = int(volume_var)

pitch17 = int(pitch_var)
time17 = int(time_var)
duration17 = int(duration_var)
volume17 = int(volume_var)

pitch18 = int(pitch_var)
time18 = int(time_var)
duration18 = int(duration_var)
volume18 = int(volume_var)

pitch19 = int(pitch_var)
time19 = int(time_var)
duration19 = int(duration_var)
volume19 = int(volume_var)

pitch20 = int(pitch_var)
time20 = int(time_var)
duration20 = int(duration_var)
volume20 = int(volume_var)

pitch21 = int(pitch_var)
time21 = int(time_var)
duration21 = int(duration_var)
volume21 = int(volume_var)

pitch22 = int(pitch_var)
time22 = int(time_var)
duration22 = int(duration_var)
volume22 = int(volume_var)

pitch23 = int(pitch_var)
time23 = int(time_var)
duration23 = int(duration_var)
volume23 = int(volume_var)

pitch24 = int(pitch_var)
time24 = int(time_var)
duration24 = int(duration_var)
volume24 = int(volume_var)



#setup track inputs

time_limit_var = 1000





for digit in a:
    #if digit == '.':
    #    continue
    MyMIDI.addNote(track1, channel1, pitch1 + int(digit), time1, duration1, volume1)
    time1 += 1
    if time1 == int(time_limit_var):
        pass


for digit in b:
    #if digit == '.':
    #    continue
    #print digit
    MyMIDI.addNote(track2, channel2, pitch2 + int(digit), time2, duration2, volume2)
    time2 += 1
    if time2 == int(time_limit_var):
        pass



for digit in c:
    #if digit == '.':
    #    continue
    MyMIDI.addNote(track3, channel3, pitch3 + int(digit), time3, duration3, volume3)
    time3 += 1
    if time3 == int(time_limit_var):
        pass



for digit in d:
    #if digit == '.':
    #    continue
    MyMIDI.addNote(track4, channel4, pitch4 + int(digit), time4, duration4, volume4)
    time4 += 1
    if time4 == int(time_limit_var):
        pass


for digit in e:
    #if digit == '.':
    #    continue
    MyMIDI.addNote(track5, channel5, pitch5 + int(digit), time5, duration5, volume5)
    time5 += 1
    if time5 == int(time_limit_var):
        pass



for digit in f:
    #if digit == '.':
    #    continue
    MyMIDI.addNote(track6, channel6, pitch6 + int(digit), time6, duration6, volume6)
    time6 += 1
    if time6 == 11800:
        pass



for digit in g:
    #if digit == '.':
    #    continue
    MyMIDI.addNote(track7, channel7, pitch7 + int(digit), time7, duration7, volume7)
    time7 += 1
    if time7 == int(time_limit_var):
        pass

for digit in h:
    #if digit == '.':
    #    continue
    MyMIDI.addNote(track8, channel8, pitch8 + int(digit), time8, duration8, volume8)
    time8 += 1
    if time8 == int(time_limit_var):
        pass


for digit in i:
    #if digit == '.':
    #    continue
    MyMIDI.addNote(track9, channel9, pitch9 + int(digit), time9, duration9, volume9)
    time9 += 1
    if time9 == int(time_limit_var):
        pass



for digit in j:
    #if digit == '.':
    #    continue
    MyMIDI.addNote(track10, channel10, pitch10 + int(digit), time10, duration10, volume10)
    time10 += 1
    if time10 == int(time_limit_var):
        pass


for digit in k:
    #if digit == '.':
    #    continue
    MyMIDI.addNote(track11, channel11, pitch11 + int(digit), time11, duration11, volume11)
    time11 += 1
    if time11 == int(time_limit_var):
        pass



for digit in p:
    #if digit == '.':
    #    continue
    MyMIDI.addNote(track12, channel12, pitch12 + int(digit), time12, duration12, volume12)
    time12 += 1
    if time12 == int(time_limit_var):
        pass


for digit in q:
    #if digit == '.':
    #    continue
    MyMIDI.addNote(track13, channel13, pitch13 + int(digit), time13, duration13, volume13)
    time13 += 1
    if time13 == int(time_limit_var):
        pass


for digit in r:
    #if digit == '.':
    #    continue
    MyMIDI.addNote(track14, channel14, pitch14 + int(digit), time14, duration14, volume14)
    time14 += 1
    if time14 == int(time_limit_var):
        pass


for digit in s:
    #if digit == '.':
    #    continue
    MyMIDI.addNote(track15, channel15, pitch15 + int(digit), time15, duration15, volume15)
    time15 += 1
    if time15 == int(time_limit_var):
        pass



for digit in t:
    #if digit == '.':
    #    continue
    MyMIDI.addNote(track16, channel16, pitch16 + int(digit), time16, duration16, volume16)
    time16 += 1
    if time16 == int(time_limit_var):
        pass


for digit in u:
    #if digit == '.':
    #    continue
    MyMIDI.addNote(track17, channel17, pitch17 + int(digit), time17, duration17, volume17)
    time17 += 1
    if time17 == int(time_limit_var):
        pass


for digit in v:
    #if digit == '.':
    #    continue
    MyMIDI.addNote(track18, channel18, pitch18 + int(digit), time18, duration18, volume18)
    time18 += 1
    if time18 == int(time_limit_var):
        pass


for digit in w:
    #if digit == '.':
    #    continue
    MyMIDI.addNote(track19, channel19, pitch19 + int(digit), time19, duration19, volume19)
    time19 += 1
    if time19 == int(time_limit_var):
        pass


for digit in ww:
    #if digit == '.':
    #    continue
    MyMIDI.addNote(track20, channel20, pitch20 + int(digit), time20, duration20, volume20)
    time20 += 1
    if time20 == int(time_limit_var):
        pass


for digit in www:
    #if digit == '.':
    #    continue
    MyMIDI.addNote(track21, channel21, pitch21 + int(digit), time21, duration21, volume21)
    time21 += 1
    if time21 == int(time_limit_var):
        pass


for digit in wx:
    #if digit == '.':
    #    continue
    MyMIDI.addNote(track22, channel22, pitch22 + int(digit), time22, duration22, volume22)
    time22 += 1
    if time22 == int(time_limit_var):
        pass


for digit in xx:
    #if digit == '.':
    #    continue
    MyMIDI.addNote(track23, channel23, pitch23 + int(digit), time23, duration23, volume23)
    time23 += 1
    if time23 == int(time_limit_var):
        pass


for digit in xy:
    #if digit == '.':
    #    continue
    MyMIDI.addNote(track24, channel24, pitch24 + int(digit), time24, duration24, volume24)
    time24 += 1
    if time24 == int(time_limit_var):
        break

# And write it to disk.
binfile = open("output.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()


print(a)
#composites_base10.sort(reverse = True)
#print(composites_base10)
#zed = [x for x in composite_base10]




list_A = [i for i,x in enumerate(a) if x != 0]
list_B = [((x+new_floor)*90)+11 for x in list_A]
print list_A
print list_B
print len(list_A)
#print a  #uncomment this line to see the full list (None=primes and 0=composite)
#print list_A201804
#print "%d is the %dth term of Sloane's A201804." % (list_A201804[-1], len(list_A201804))










