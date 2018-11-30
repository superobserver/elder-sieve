#!/usr/bin/env python
#use timidity output.mid to play audio in Terminal
#use timidity output.mid -Ow -o primes.wav in Terminal to convert *.mid to *.wav

from midiutil.MidiFile import MIDIFile


new_test = 10000
#a = [4.9]*int(new_test) #11
#b = [5.1]*int(new_test) #13
#c = [1.7]*int(new_test) #17
#d = [9.1]*int(new_test) #91
#e = [8.9]*int(new_test)
#f = [8.7]*int(new_test)
#g = [8.5]*int(new_test)
#h = [8.3]*int(new_test)
#i = [8.1]*int(new_test)
#j = [7.9]*int(new_test)
#k = [7.7]*int(new_test)
#p = [7.5]*int(new_test)
#q = [7.3]*int(new_test)
#r = [7.1]*int(new_test)
#s = [6.9]*int(new_test)
#t = [6.7]*int(new_test)
#u = [6.5]*int(new_test)
#v = [6.3]*int(new_test)
#w = [6.1]*int(new_test)
#ww = [5.9]*int(new_test)
#www = [5.7]*int(new_test)
#wx = [5.5]*int(new_test)
#xx = [5.3]*int(new_test)
#xy = [4.7]*int(new_test)

#new_test = 14000
a = [11]*int(new_test) #11
b = [13]*int(new_test) #13
c = [17]*int(new_test) #17
d = [91]*int(new_test)
e = [89]*int(new_test)
f = [83]*int(new_test)
g = [79]*int(new_test)
h = [77]*int(new_test)
i = [73]*int(new_test)
j = [71]*int(new_test)
k = [67]*int(new_test)
p = [61]*int(new_test)
q = [57]*int(new_test)
r = [53]*int(new_test)
s = [49]*int(new_test)
t = [47]*int(new_test)
u = [43]*int(new_test)
v = [41]*int(new_test)
w = [37]*int(new_test)
ww = [31]*int(new_test)
www = [29]*int(new_test)
wx = [23]*int(new_test)
xx = [19]*int(new_test)
xy = [7]*int(new_test)





def drLDa(x, l, m, z, o):      
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

def drLDb(x, l, m, z, o):      
  y = 90*(x*x) - l*x + m 
  if y < new_test:
    b[y] = 0
  else:
    return
  for n in xrange (1, new_test):
    new_y = y+((z+(90*(x-1)))*n)
    if new_y < new_test:
      b[new_y] = 0
    new2_y = y+((o+(90*(x-1)))*n)   
    if new2_y < new_test:    
      b[new2_y] = 0      
    if new_y > new_test:
      return
    else:
      pass

def drLDc(x, l, m, z, o):      
  y = 90*(x*x) - l*x + m 
  if y < new_test:
    c[y] = 0
  else:
    return
  for n in xrange (1, new_test):
    new_y = y+((z+(90*(x-1)))*n)
    if new_y < new_test:
      c[new_y] = 0
    new2_y = y+((o+(90*(x-1)))*n)   
    if new2_y < new_test:    
      c[new2_y] = 0      
    if new_y > new_test:
      return
    else:
      pass


def drLDd(x, l, m, z, o):      
  y = 90*(x*x) - l*x + m 
  if y < new_test:
    d[y] = 0
  else:
    return
  for n in xrange (1, new_test):
    new_y = y+((z+(90*(x-1)))*n)
    if new_y < new_test:
      d[new_y] = 0
    new2_y = y+((o+(90*(x-1)))*n)   
    if new2_y < new_test:    
      d[new2_y] = 0      
    if new_y > new_test:
      return
    else:
      pass


def drLDe(x, l, m, z, o):      
  y = 90*(x*x) - l*x + m 
  if y < new_test:
    e[y] = 0
  else:
    return
  for n in xrange (1, new_test):
    new_y = y+((z+(90*(x-1)))*n)
    if new_y < new_test:
      e[new_y] = 0
    new2_y = y+((o+(90*(x-1)))*n)   
    if new2_y < new_test:    
      e[new2_y] = 0      
    if new_y > new_test:
      return
    else:
      pass

def drLDf(x, l, m, z, o):      
  y = 90*(x*x) - l*x + m 
  if y < new_test:
    f[y] = 0
  else:
    return
  for n in xrange (1, new_test):
    new_y = y+((z+(90*(x-1)))*n)
    if new_y < new_test:
      f[new_y] = 0
    new2_y = y+((o+(90*(x-1)))*n)   
    if new2_y < new_test:    
      f[new2_y] = 0      
    if new_y > new_test:
      return
    else:
      pass

def drLDg(x, l, m, z, o):      
  y = 90*(x*x) - l*x + m 
  if y < new_test:
    g[y] = 0
  else:
    return
  for n in xrange (1, new_test):
    new_y = y+((z+(90*(x-1)))*n)
    if new_y < new_test:
      g[new_y] = 0
    new2_y = y+((o+(90*(x-1)))*n)   
    if new2_y < new_test:    
      g[new2_y] = 0      
    if new_y > new_test:
      return
    else:
      pass

def drLDh(x, l, m, z, o):      
  y = 90*(x*x) - l*x + m 
  if y < new_test:
    h[y] = 0
  else:
    return
  for n in xrange (1, new_test):
    new_y = y+((z+(90*(x-1)))*n)
    if new_y < new_test:
      h[new_y] = 0
    new2_y = y+((o+(90*(x-1)))*n)   
    if new2_y < new_test:    
      h[new2_y] = 0      
    if new_y > new_test:
      return
    else:
      pass

def drLDi(x, l, m, z, o):      
  y = 90*(x*x) - l*x + m 
  if y < new_test:
    i[y] = 0
  else:
    return
  for n in xrange (1, new_test):
    new_y = y+((z+(90*(x-1)))*n)
    if new_y < new_test:
      i[new_y] = 0
    new2_y = y+((o+(90*(x-1)))*n)   
    if new2_y < new_test:    
      i[new2_y] = 0      
    if new_y > new_test:
      return
    else:
      pass

def drLDj(x, l, m, z, o):      
  y = 90*(x*x) - l*x + m 
  if y < new_test:
    j[y] = 0
  else:
    return
  for n in xrange (1, new_test):
    new_y = y+((z+(90*(x-1)))*n)
    if new_y < new_test:
      j[new_y] = 0
    new2_y = y+((o+(90*(x-1)))*n)   
    if new2_y < new_test:    
      j[new2_y] = 0      
    if new_y > new_test:
      return
    else:
      pass

def drLDk(x, l, m, z, o):      
  y = 90*(x*x) - l*x + m 
  if y < new_test:
    k[y] = 0
  else:
    return
  for n in xrange (1, new_test):
    new_y = y+((z+(90*(x-1)))*n)
    if new_y < new_test:
      k[new_y] = 0
    new2_y = y+((o+(90*(x-1)))*n)   
    if new2_y < new_test:    
      k[new2_y] = 0      
    if new_y > new_test:
      return
    else:
      pass


def drLDp(x, l, m, z, o):      
  y = 90*(x*x) - l*x + m 
  if y < new_test:
    p[y] = 0
  else:
    return
  for n in xrange (1, new_test):
    new_y = y+((z+(90*(x-1)))*n)
    if new_y < new_test:
      p[new_y] = 0
    new2_y = y+((o+(90*(x-1)))*n)   
    if new2_y < new_test:    
      p[new2_y] = 0      
    if new_y > new_test:
      return
    else:
      pass

def drLDq(x, l, m, z, o):      
  y = 90*(x*x) - l*x + m 
  if y < new_test:
    q[y] = 0
  else:
    return
  for n in xrange (1, new_test):
    new_y = y+((z+(90*(x-1)))*n)
    if new_y < new_test:
      q[new_y] = 0
    new2_y = y+((o+(90*(x-1)))*n)   
    if new2_y < new_test:    
      q[new2_y] = 0      
    if new_y > new_test:
      return
    else:
      pass

def drLDr(x, l, m, z, o):      
  y = 90*(x*x) - l*x + m 
  if y < new_test:
    r[y] = 0
  else:
    return
  for n in xrange (1, new_test):
    new_y = y+((z+(90*(x-1)))*n)
    if new_y < new_test:
      r[new_y] = 0
    new2_y = y+((o+(90*(x-1)))*n)   
    if new2_y < new_test:    
      r[new2_y] = 0      
    if new_y > new_test:
      return
    else:
      pass

def drLDs(x, l, m, z, o):      
  y = 90*(x*x) - l*x + m 
  if y < new_test:
    s[y] = 0
  else:
    return
  for n in xrange (1, new_test):
    new_y = y+((z+(90*(x-1)))*n)
    if new_y < new_test:
      s[new_y] = 0
    new2_y = y+((o+(90*(x-1)))*n)   
    if new2_y < new_test:    
      s[new2_y] = 0      
    if new_y > new_test:
      return
    else:
      pass

def drLDt(x, l, m, z, o):      
  y = 90*(x*x) - l*x + m 
  if y < new_test:
    t[y] = 0
  else:
    return
  for n in xrange (1, new_test):
    new_y = y+((z+(90*(x-1)))*n)
    if new_y < new_test:
      t[new_y] = 0
    new2_y = y+((o+(90*(x-1)))*n)   
    if new2_y < new_test:    
      t[new2_y] = 0      
    if new_y > new_test:
      return
    else:
      pass

def drLDu(x, l, m, z, o):      
  y = 90*(x*x) - l*x + m 
  if y < new_test:
    u[y] = 0
  else:
    return
  for n in xrange (1, new_test):
    new_y = y+((z+(90*(x-1)))*n)
    if new_y < new_test:
      u[new_y] = 0
    new2_y = y+((o+(90*(x-1)))*n)   
    if new2_y < new_test:    
      u[new2_y] = 0      
    if new_y > new_test:
      return
    else:
      pass

def drLDv(x, l, m, z, o):      
  y = 90*(x*x) - l*x + m 
  if y < new_test:
    v[y] = 0
  else:
    return
  for n in xrange (1, new_test):
    new_y = y+((z+(90*(x-1)))*n)
    if new_y < new_test:
      v[new_y] = 0
    new2_y = y+((o+(90*(x-1)))*n)   
    if new2_y < new_test:    
      v[new2_y] = 0      
    if new_y > new_test:
      return
    else:
      pass

def drLDw(x, l, m, z, o):      
  y = 90*(x*x) - l*x + m 
  if y < new_test:
    w[y] = 0
  else:
    return
  for n in xrange (1, new_test):
    new_y = y+((z+(90*(x-1)))*n)
    if new_y < new_test:
      w[new_y] = 0
    new2_y = y+((o+(90*(x-1)))*n)   
    if new2_y < new_test:    
      w[new2_y] = 0      
    if new_y > new_test:
      return
    else:
      pass

def drLDww(x, l, m, z, o):      
  y = 90*(x*x) - l*x + m 
  if y < new_test:
    ww[y] = 0
  else:
    return
  for n in xrange (1, new_test):
    new_y = y+((z+(90*(x-1)))*n)
    if new_y < new_test:
      ww[new_y] = 0
    new2_y = y+((o+(90*(x-1)))*n)   
    if new2_y < new_test:    
      ww[new2_y] = 0      
    if new_y > new_test:
      return
    else:
      pass

def drLDwww(x, l, m, z, o):      
  y = 90*(x*x) - l*x + m 
  if y < new_test:
    www[y] = 0
  else:
    return
  for n in xrange (1, new_test):
    new_y = y+((z+(90*(x-1)))*n)
    if new_y < new_test:
      www[new_y] = 0
    new2_y = y+((o+(90*(x-1)))*n)   
    if new2_y < new_test:    
      www[new2_y] = 0      
    if new_y > new_test:
      return
    else:
      pass

def drLDwx(x, l, m, z, o):      
  y = 90*(x*x) - l*x + m 
  if y < new_test:
    wx[y] = 0
  else:
    return
  for n in xrange (1, new_test):
    new_y = y+((z+(90*(x-1)))*n)
    if new_y < new_test:
      wx[new_y] = 0
    new2_y = y+((o+(90*(x-1)))*n)   
    if new2_y < new_test:    
      wx[new2_y] = 0      
    if new_y > new_test:
      return
    else:
      pass

def drLDxx(x, l, m, z, o):      
  y = 90*(x*x) - l*x + m 
  if y < new_test:
    xx[y] = 0
  else:
    return
  for n in xrange (1, new_test):
    new_y = y+((z+(90*(x-1)))*n)
    if new_y < new_test:
      xx[new_y] = 0
    new2_y = y+((o+(90*(x-1)))*n)   
    if new2_y < new_test:    
      xx[new2_y] = 0      
    if new_y > new_test:
      return
    else:
      pass

def drLDxy(x, l, m, z, o):      
  y = 90*(x*x) - l*x + m 
  if y < new_test:
    xy[y] = 0
  else:
    return
  for n in xrange (1, new_test):
    new_y = y+((z+(90*(x-1)))*n)
    if new_y < new_test:
      xy[new_y] = 0
    new2_y = y+((o+(90*(x-1)))*n)   
    if new2_y < new_test:    
      xy[new2_y] = 0      
    if new_y > new_test:
      return
    else:
      pass



for x in xrange(1, 17): # 10000 = 12; 100000 = 36; 1,000,000 = 108; 10,000,000 = 336; 100,000,000 = 1056; 1,000,000,000 = 
  
    drLDa(x, 120, 34, 7, 53)  #7,53  @4,  154 1
    drLDa(x, 132, 48, 19, 29) #19,29 @6,  144 2
    drLDa(x, 120, 38, 17, 43) #17,43 @8,  158 3
    drLDa(x, 90, 11, 13, 77)  #13,77 @11, 191 4
    drLDa(x, 78, -1, 11, 91)  #11,91 @11, 203 5
    drLDa(x, 108, 32, 31, 41) #31,41 @14, 176 6
    drLDa(x, 90, 17, 23, 67)  #23,67 @17, 197 7
    drLDa(x, 72, 14, 49, 59)  #49,59 @32, 230 8
    drLDa(x, 60, 4, 37, 83)   #37,83 @34, 244 9
    drLDa(x, 60, 8, 47, 73)   #47,73 @38, 248 10
    drLDa(x, 48, 6, 61, 71)   #61,71 @48, 270 11
    drLDa(x, 12, 0, 79, 89)   #79,89 @78, 336 12

    drLDb(x, 76, -1, 13, 91)   #13,91
    drLDb(x, 94, 18, 19, 67)  #19,67
    drLDb(x, 94, 24, 37, 49)  #37,49
    drLDb(x, 76, 11, 31, 73)  #31,73
    drLDb(x, 86, 6, 11, 83)   #11,83
    drLDb(x, 104, 29, 29, 47) #29,47
    drLDb(x, 86, 14, 23, 71)  #23,71
    drLDb(x, 86, 20, 41, 53)  #41,53
    drLDb(x, 104, 25, 17, 59) #17,59
    drLDb(x, 14, 0, 77, 89)   #77,89
    drLDb(x, 94, 10, 7, 79)   #7,79
    drLDb(x, 76, 15, 43, 61) #43,61


    drLDc(x, 72, -1, 17, 91)   #17,91
    drLDc(x, 108, 29, 19, 53) #19,53
    drLDc(x, 72, 11, 37, 71)   #37,71
    drLDc(x, 18, 0, 73, 89)   #73,89
    drLDc(x, 102, 20, 11, 67)  #11,67
    drLDc(x, 138, 52, 13, 29) #13,29
    drLDc(x, 102, 28, 31, 47)  #31,47
    drLDc(x, 48, 3, 49, 83)  #49,83
    drLDc(x, 78, 8, 23, 79)  #23,79
    drLDc(x, 132, 45, 7, 41) #7,41
    drLDc(x, 78, 16, 43, 59)   #43,59
    drLDc(x, 42, 4, 61, 77) #61,77   

    #91 = d
    drLDd(x, 2, 0, 91, 91) #91,91
    drLDd(x, 142, 56, 19, 19) #19,19
    drLDd(x, 70, 10, 37, 73) #37, 73
    drLDd(x, 128, 43, 11, 41) #11, 41
    drLDd(x, 92, 21, 29, 59) #29,59
    drLDd(x, 110, 32, 23, 47) #23,47
    drLDd(x, 20, 1, 77, 83) #77,83
    drLDd(x, 160, 71, 7, 13) #7,13
    drLDd(x, 88, 19, 31, 61) #31,61
    drLDd(x, 52, 5, 49, 79) #49,79
    drLDd(x, 70, 12, 43, 67) #43,67
    drLDd(x, 110, 30, 17, 53) #17,53
    drLDd(x, 38, 4, 71, 71) #71,71
    drLDd(x, 2, 0, 89, 89) #89,89

# 89 = e
    drLDe(x, 1, 0, 89, 91) #89,91
    drLDe(x, 90, 14, 19, 71) #19,71
    drLDe(x, 126, 42, 17, 37) #17,37
    drLDe(x, 54, 6, 53, 73) #53,73
    drLDe(x, 120, 35, 11, 49) #11,49
    drLDe(x, 120, 39, 29, 31) #29,31
    drLDe(x, 66, 10, 47, 67) #47,67
    drLDe(x, 84, 5, 13, 83) #13,83
    drLDe(x, 114, 34, 23, 43) #23,43
    drLDe(x, 60, 5, 41, 79) #41,79
    drLDe(x, 60, 9, 59, 61) #59,61
    drLDe(x, 96, 11, 7, 77) #7,77

# 83 = f
    drLDf(x, 6, -1, 83, 91) #83,91
    drLDf(x, 114, 33, 19, 47) #19,47
    drLDf(x, 114, 35, 37, 29) #37,29
    drLDf(x, 96, 14, 11, 73) #11,73
    drLDf(x, 126, 41, 13, 41) #13,41
    drLDf(x, 126, 43, 23, 31) #23,31
    drLDf(x, 54, 5, 49, 77) #49,77
    drLDf(x, 54, 7, 59, 67) #59,67
    drLDf(x, 84, 0, 7, 89) #7,89
    drLDf(x, 66, 9, 43, 71) #43,71
    drLDf(x, 66, 11, 53, 61) #53,61
    drLDf(x, 84, 8, 17, 79) #17,79



# 79 = g
    drLDg(x, 10, -1, 79, 91) #79,91
    drLDg(x, 100, 22, 19, 61) #19,61
    drLDg(x, 136, 48, 7, 37) #7,37
    drLDg(x, 64, 8, 43, 73) #43,73
    drLDg(x, 80, 0, 11, 89) #11,89
    drLDg(x, 80, 12, 29, 71) #29,71
    drLDg(x, 116, 34, 17, 47) #17,47
    drLDg(x, 44, 2, 53, 83) #53,83
    drLDg(x, 154, 65, 13, 13) #13,13
    drLDg(x, 100, 26, 31, 49) #31,49
    drLDg(x, 46, 5, 67, 67) #67,67
    drLDg(x, 134, 49, 23, 23) #23,23
    drLDg(x, 80, 16, 41, 59) #41,59
    drLDg(x, 26, 1, 77, 77) #77,77


# 77 = h
    drLDh(x, 12, -1, 77, 91) #77,91
    drLDh(x, 138, 52, 19, 23) #19,23
    drLDh(x, 102, 28, 37, 41) #37,41
    drLDh(x, 48, 5, 59, 73) #59,73
    drLDh(x, 162, 72, 7, 11) #7,11
    drLDh(x, 108, 31, 29, 43) #29,43
    drLDh(x, 72, 13, 47, 61) #47,61
    drLDh(x, 18, 0, 79, 83) #79,83
    drLDh(x, 78, 0, 13, 89) #13,89
    drLDh(x, 132, 47, 17, 31) #17,31
    drLDh(x, 78, 16, 49, 53) #49,53
    drLDh(x, 42, 4, 67, 71) #67,71

# 73 = i
    drLDi(x, 16, -1, 73, 91) #73,91
    drLDi(x, 124, 41, 19, 37) #19,37
    drLDi(x, 146, 58, 11, 23) #11,23
    drLDi(x, 74, 8, 29, 77) #29,77
    drLDi(x, 74, 14, 47, 59) #47,59
    drLDi(x, 56, 3, 41, 83) #41,83
    drLDi(x, 106, 24, 13, 61) #13,61
    drLDi(x, 106, 30, 31, 43) #31,43
    drLDi(x, 124, 37, 7, 49) #7,49
    drLDi(x, 34, 2, 67, 79) #67,79
    drLDi(x, 74, 0, 17, 89) #17,89
    drLDi(x, 56, 7, 53, 71) #53,71


# 71 = j
    drLDj(x, 18, -1, 71, 91) #71,91
    drLDj(x, 72, 0, 19, 89) #19,89
    drLDj(x, 90, 21, 37, 53) #37,53
    drLDj(x, 90, 13, 17, 73) #17,73
    drLDj(x, 138, 51, 11, 31) #11,31
    drLDj(x, 102, 27, 29, 49) #29,49
    drLDj(x, 120, 36, 13, 47) #13,47
    drLDj(x, 30, 1, 67, 83) #67,83
    drLDj(x, 150, 61, 7, 23) #7,23
    drLDj(x, 78, 15, 41, 61) #41,61
    drLDj(x, 42, 3, 59, 79) #59,79
    drLDj(x, 60, 6, 43, 77) #43,77

# 67 = k
    drLDk(x, 22, -1, 67, 91) #67,91
    drLDk(x, 148, 60, 13, 19) #13,19
    drLDk(x, 112, 34, 31, 37) #31,37
    drLDk(x, 58, 7, 49, 73) #49,73
    drLDk(x, 122, 37, 11, 47) #11,47
    drLDk(x, 68, 4, 29, 83) #29,83
    drLDk(x, 122, 39, 17, 41) #17,41
    drLDk(x, 68, 12, 53, 59) #53,59
    drLDk(x, 32, 2, 71, 77) #71,77
    drLDk(x, 112, 26, 7, 61) #7,61
    drLDk(x, 58, 5, 43, 79) #43,79
    drLDk(x, 68, 0, 23, 89) #23,89

# 61 = p
    drLDp(x, 28, -1, 61, 91) #61,91
    drLDp(x, 82, 8, 19, 79) #19,79
    drLDp(x, 100, 27, 37, 43) #37,43)
    drLDp(x, 100, 15, 7, 73) #7,73
    drLDp(x, 98, 16, 11, 71) #11,71
    drLDp(x, 62, 0, 29, 89) #29,89
    drLDp(x, 80, 17, 47, 53) #47,53
    drLDp(x, 80, 5, 17, 83) #17,83
    drLDp(x, 100, 19, 13, 67) #13,67
    drLDp(x, 118, 38, 31, 31) #31,31
    drLDp(x, 82, 18, 49, 49) #49,49
    drLDp(x, 80, 9, 23, 77) #23,77
    drLDp(x, 98, 26, 41, 41) #41,41
    drLDp(x, 62, 10, 59, 59) #59,59


# 59 = q
    drLDq(x, 30, -1, 59, 91) #59,91
    drLDq(x, 120, 38, 19, 41) #19,41
    drLDq(x, 66, 7, 37, 77) #37,77
    drLDq(x, 84, 12, 23, 73) #23,73
    drLDq(x, 90, 9, 11, 79) #11,79
    drLDq(x, 90, 19, 29, 61) #29,61
    drLDq(x, 126, 39, 7, 47) #7,47
    drLDq(x, 54, 3, 43, 83) #43,83
    drLDq(x, 114, 31, 13, 53) #13,53
    drLDq(x, 60, 0, 31, 89) #31,89
    drLDq(x, 60, 8, 49, 71) #49,71
    drLDq(x, 96, 18, 17, 67) #17,67

# 53 = r
    drLDr(x, 36, -1, 53, 91) #53,91
    drLDr(x, 144, 57, 17, 19) #17,19
    drLDr(x, 54, 0, 37, 89) #37,89
    drLDr(x, 36, 3, 71, 73) #71,73
    drLDr(x, 156, 67, 11, 13) #11,13
    drLDr(x, 84, 15, 29, 67) #29,67
    drLDr(x, 84, 19, 47, 49) #47,49
    drLDr(x, 66, 4, 31, 83) #31,83
    drLDr(x, 96, 21, 23, 61) #23,61
    drLDr(x, 96, 25, 41, 43) #41,43
    drLDr(x, 114, 28, 7, 59) #7,59
    drLDr(x, 24, 1, 77, 79) #77,79

# 49 = s
    drLDs(x, 40, -1, 49, 91) #49,91
    drLDs(x, 130, 46, 19, 31) #19,31
    drLDs(x, 76, 13, 37, 67) #37,67
    drLDs(x, 94, 14, 13, 73) #13,73
    drLDs(x, 140, 53, 11, 29) #11,29
    drLDs(x, 86, 20, 47, 47) #47,47
    drLDs(x, 14, 0, 83, 83) #83,83
    drLDs(x, 104, 27, 23, 53) #23,53
    drLDs(x, 50, 0, 41, 89) #41,89
    drLDs(x, 50, 6, 59, 71) #59,71
    drLDs(x, 86, 10, 17, 77) #17,77
    drLDs(x, 166, 76, 7, 7) #7,7
    drLDs(x, 94, 24, 43, 43) #43,43
    drLDs(x, 40, 3, 61, 79) #61,79

# 47 = t
    drLDt(x, 42, -1, 47, 91) #47,91
    drLDt(x, 78, 5, 19, 83) #19,83
    drLDt(x, 132, 46, 11, 37) #11,37
    drLDt(x, 78, 11, 29, 73) #29,73
    drLDt(x, 108, 26, 13, 59) #13,59
    drLDt(x, 72, 8, 31, 77) #31,77
    drLDt(x, 108, 30, 23, 49) #23,49
    drLDt(x, 102, 17, 7, 71) #7,71
    drLDt(x, 48, 0, 43, 89) #43,89
    drLDt(x, 102, 23, 17, 61) #17,61
    drLDt(x, 48, 4, 53, 79) #53,79
    drLDt(x, 72, 12, 41, 67) #41,67


# 43 = u
    drLDu(x, 46, -1, 43, 91) #43,91
    drLDu(x, 154, 65, 7, 19) #7,19
    drLDu(x, 64, 6, 37, 79) #37,79
    drLDu(x, 46, 5, 61, 73) #61,73
    drLDu(x, 116, 32, 11, 53) #11,53
    drLDu(x, 134, 49, 17, 29) #17,29
    drLDu(x, 44, 0, 47, 89) #47,89
    drLDu(x, 26, 1, 71, 83) #71,83
    drLDu(x, 136, 50, 13, 31) #13,31
    drLDu(x, 64, 10, 49, 67) #49,67
    drLDu(x, 116, 36, 23, 41) #23,41
    drLDu(x, 44, 4, 59, 77) #59,77

# 41 = v
    drLDv(x, 48, -1, 41, 91) #41,91
    drLDv(x, 42, 0, 49, 89) #49,89
    drLDv(x, 102, 24, 19, 59) #19,59
    drLDv(x, 120, 39, 23, 37) #23,37
    drLDv(x, 108, 25, 11, 61) #11,61
    drLDv(x, 72, 7, 29, 79) #29,79
    drLDv(x, 90, 22, 43, 47) #43,47
    drLDv(x, 150, 62, 13, 17) #13,17
    drLDv(x, 78, 12, 31, 71) #31,71
    drLDv(x, 30, 2, 73, 77) #73, 77
    drLDv(x, 60, 9, 53, 67) #53,67
    drLDv(x, 90, 6, 7, 83) #7,83

# 37 = w
    drLDw(x, 52, -1, 37, 91) #37,91
    drLDw(x, 88, 13, 19, 73) #19,73
    drLDw(x, 92, 11, 11, 77) #11,77
    drLDw(x, 128, 45, 23, 29) #23,29
    drLDw(x, 92, 23, 41, 47) #41,47
    drLDw(x, 38, 2, 59, 83) #59,83
    drLDw(x, 88, 9, 13, 79) #13,79
    drLDw(x, 142, 54, 7, 31) #7,31
    drLDw(x, 88, 21, 43, 49) #43,49
    drLDw(x, 52, 7, 61, 67) #61,67
    drLDw(x, 92, 15, 17, 71) #17,71
    drLDw(x, 38, 0, 53, 89) #53,89

# 31 = ww
    drLDww(x, 58, -1, 31, 91) #31,91
    drLDww(x, 112, 32, 19, 49) #19,49
    drLDww(x, 130, 45, 13, 37) #13,37
    drLDww(x, 40, 4, 67, 73) #67,73
    drLDww(x, 158, 69, 11, 11) #11,11
    drLDww(x, 122, 41, 29, 29) #29,29
    drLDww(x, 50, 3, 47, 83) #47,83
    drLDww(x, 140, 54, 17, 23) #17,23
    drLDww(x, 68, 10, 41, 71) #41,71
    drLDww(x, 32, 0, 59, 89) #59,89
    drLDww(x, 50, 5, 53, 77) #53,77
    drLDww(x, 130, 43, 7, 43) #7,43
    drLDww(x, 58, 9, 61, 61) #61,61
    drLDww(x, 22, 1, 79, 79) #79,79

# 29 = www
    drLDwww(x, 60, -1, 29, 91) #29,91
    drLDwww(x, 150, 62, 11, 19) #11,19
    drLDwww(x, 96, 25, 37, 47) #37,47
    drLDwww(x, 24, 1, 73, 83) #73,83
    drLDwww(x, 144, 57, 13, 23) #13,23
    drLDwww(x, 90, 20, 31, 59) #31,59
    drLDwww(x, 90, 22, 41, 49) #41,49
    drLDwww(x, 36, 3, 67, 77) #67,77
    drLDwww(x, 156, 67, 7, 17) #7,17
    drLDwww(x, 84, 19, 43, 53) #43,53
    drLDwww(x, 30, 0, 61, 89) #61,89
    drLDwww(x, 30, 2, 71, 79) #71,79

# 23 = wx
    drLDwx(x, 66, -1, 23, 91) #23,91
    drLDwx(x, 84, 10, 19, 77) #19,77
    drLDwx(x, 84, 18, 37, 59) #37,59
    drLDwx(x, 66, 9, 41, 73) #41,73
    drLDwx(x, 126, 41, 11, 43) #11,43
    drLDwx(x, 144, 56, 7, 29) #7,29
    drLDwx(x, 54, 5, 47, 79) #47,79
    drLDwx(x, 36, 2, 61, 83) #61,83
    drLDwx(x, 96, 16, 13, 71) #13,71
    drLDwx(x, 96, 24, 31, 53) #31,53
    drLDwx(x, 114, 33, 17, 49) #17,49
    drLDwx(x, 24, 0, 67, 89) #67,89

# 19 = xx
    drLDxx(x, 70, -1, 19, 91) #19,91
    drLDxx(x, 106, 31, 37, 73) #37,73
    drLDxx(x, 34, 3, 73, 73) #73,73
    drLDxx(x, 110, 27, 11, 59) #11,59
    drLDxx(x, 110, 33, 29, 41) #29,41
    drLDxx(x, 56, 6, 47, 77) #47,77
    drLDxx(x, 74, 5, 23, 83) #23,83
    drLDxx(x, 124, 40, 13, 43) #13,43
    drLDxx(x, 70, 7, 31, 79) #31,79
    drLDxx(x, 70, 13, 49, 61) #49,61
    drLDxx(x, 106, 21, 7, 67) #7,67
    drLDxx(x, 20, 0, 71, 89) #71,89
    drLDxx(x, 74, 15, 53, 53) #53,53
    drLDxx(x, 146, 59, 17, 17) #17,17


# 7 = xy
    drLDxy(x, 82, -1, 7, 91) #7,91
    drLDxy(x, 118, 37, 19, 43) #19,43
    drLDxy(x, 82, 17, 37, 61) #37,61
    drLDxy(x, 28, 2, 73, 79) #73,79
    drLDxy(x, 152, 64, 11, 17) #11,17
    drLDxy(x, 98, 25, 29, 53) #29,53
    drLDxy(x, 62, 9, 47, 71) #47,71
    drLDxy(x, 8, 0, 83, 89) #83,89
    drLDxy(x, 118, 35, 13, 49) #13,49
    drLDxy(x, 82, 15, 31, 67) #31,67
    drLDxy(x, 98, 23, 23, 59) #23,59
    drLDxy(x, 62, 7, 41, 77) #41,77



#list_A201804 = [i for i,x in enumerate(a) if x != 0]
#print a  #uncomment this line to see the full list (None=primes and 0=composite)
#print list_A201804
#print "%d is the %dth term of Sloane's A201804." % (list_A201804[-1], len(list_A201804))










# Just an example
try:
    # import version included with old SymPy
    from sympy.mpmath import mp
except ImportError:
    # import newer version
    from mpmath import mp
mp.dps = 1000  # set number of digits

# Create the MIDIFile Object with 24 tracks
MyMIDI = MIDIFile(23)

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
time_var = 1000
#time_var = 0
#time_var_delta = 111 #example

#duration variable setup
duration_var = 1

#volume variable setup
volume_var = 60

#pitch variable setup
pitch_var = 0


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
for digit in a:
    if digit == '.':
        continue
    MyMIDI.addNote(track1, channel1, pitch1 + int(digit), time1, duration1, volume1)
    time1 += 1
    if time1 == 11800:
        pass
for digit in b:
    if digit == '.':
        continue
    MyMIDI.addNote(track2, channel2, pitch2 + int(digit), time2, duration2, volume2)
    time2 += 1
    if time2 == 11800:
        pass

for digit in c:
    if digit == '.':
        continue
    MyMIDI.addNote(track3, channel3, pitch3 + int(digit), time3, duration3, volume3)
    time3 += 1
    if time3 == 11800:
        pass

for digit in d:
    if digit == '.':
        continue
    MyMIDI.addNote(track4, channel4, pitch4 + int(digit), time4, duration4, volume4)
    time4 += 1
    if time4 == 11800:
        pass

for digit in e:
    if digit == '.':
        continue
    MyMIDI.addNote(track5, channel5, pitch5 + int(digit), time5, duration5, volume5)
    time5 += 1
    if time5 == 11800:
        pass

for digit in f:
    if digit == '.':
        continue
    MyMIDI.addNote(track6, channel6, pitch6 + int(digit), time6, duration6, volume6)
    time6 += 1
    if time6 == 11800:
        pass

for digit in g:
    if digit == '.':
        continue
    MyMIDI.addNote(track7, channel7, pitch7 + int(digit), time7, duration7, volume7)
    time7 += 1
    if time7 == 11800:
        pass

for digit in h:
    if digit == '.':
        continue
    MyMIDI.addNote(track8, channel8, pitch8 + int(digit), time8, duration8, volume8)
    time8 += 1
    if time8 == 11800:
        pass


for digit in i:
    if digit == '.':
        continue
    MyMIDI.addNote(track9, channel9, pitch9 + int(digit), time9, duration9, volume9)
    time9 += 1
    if time9 == 11800:
        pass

for digit in j:
    if digit == '.':
        continue
    MyMIDI.addNote(track10, channel10, pitch10 + int(digit), time10, duration10, volume10)
    time10 += 1
    if time10 == 11800:
        pass

for digit in k:
    if digit == '.':
        continue
    MyMIDI.addNote(track11, channel11, pitch11 + int(digit), time11, duration11, volume11)
    time11 += 1
    if time11 == 11800:
        pass

for digit in p:
    if digit == '.':
        continue
    MyMIDI.addNote(track12, channel12, pitch12 + int(digit), time12, duration12, volume12)
    time12 += 1
    if time12 == 11800:
        pass

for digit in q:
    if digit == '.':
        continue
    MyMIDI.addNote(track13, channel13, pitch13 + int(digit), time13, duration13, volume13)
    time13 += 1
    if time13 == 11800:
        pass

for digit in r:
    if digit == '.':
        continue
    MyMIDI.addNote(track14, channel14, pitch14 + int(digit), time14, duration14, volume14)
    time14 += 1
    if time14 == 11800:
        pass

for digit in s:
    if digit == '.':
        continue
    MyMIDI.addNote(track15, channel15, pitch15 + int(digit), time15, duration15, volume15)
    time15 += 1
    if time15 == 11800:
        pass

for digit in t:
    if digit == '.':
        continue
    MyMIDI.addNote(track16, channel16, pitch16 + int(digit), time16, duration16, volume16)
    time16 += 1
    if time16 == 11800:
        pass

for digit in u:
    if digit == '.':
        continue
    MyMIDI.addNote(track17, channel17, pitch17 + int(digit), time17, duration17, volume17)
    time17 += 1
    if time17 == 11800:
        pass

for digit in v:
    if digit == '.':
        continue
    MyMIDI.addNote(track18, channel18, pitch18 + int(digit), time18, duration18, volume18)
    time18 += 1
    if time18 == 11800:
        pass

for digit in w:
    if digit == '.':
        continue
    MyMIDI.addNote(track19, channel19, pitch19 + int(digit), time19, duration19, volume19)
    time19 += 1
    if time19 == 11800:
        pass

for digit in ww:
    if digit == '.':
        continue
    MyMIDI.addNote(track20, channel20, pitch20 + int(digit), time20, duration20, volume20)
    time20 += 1
    if time20 == 11800:
        pass

for digit in www:
    if digit == '.':
        continue
    MyMIDI.addNote(track21, channel21, pitch21 + int(digit), time21, duration21, volume21)
    time21 += 1
    if time21 == 11800:
        pass

for digit in wx:
    if digit == '.':
        continue
    MyMIDI.addNote(track22, channel22, pitch22 + int(digit), time22, duration22, volume22)
    time22 += 1
    if time22 == 11800:
        pass

for digit in xx:
    if digit == '.':
        continue
    MyMIDI.addNote(track23, channel23, pitch23 + int(digit), time23, duration23, volume23)
    time23 += 1
    if time23 == 11800:
        pass


for digit in xy:
    if digit == '.':
        continue
    MyMIDI.addNote(track24, channel24, pitch24 + int(digit), time24, duration24, volume24)
    time24 += 1
    if time24 == 11800:
        break

# And write it to disk.
binfile = open("output.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()


print(a)











