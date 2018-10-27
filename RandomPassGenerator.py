import hashlib
import random
import time
import sys

################################################################################
def slowprint(s):                                                              #
    for c in s + '\n':                                                         #
        sys.stdout.write(c)                                                    #
        sys.stdout.flush() # defeat buffering                                  #
        time.sleep(random.random() * 0.1)                                      #
################################################################################

print "Welcome to the Password generator."
hardware_var = raw_input("Please place the Hardware ID here. Make sure there are NO ADDED SPACES!>>")

#First Pass
###############################################
hash_object = hashlib.sha1(hardware_var)
hex_dig = hash_object.hexdigest()
hash_object = hashlib.sha256(hex_dig)
hex_dig1 = hash_object.hexdigest()
hash_object = hashlib.sha512(hex_dig1)
hex_dig2 = hash_object.hexdigest()
###############################################

#concatenate values together into variable
###############################################
new_var = hex_dig + hex_dig1 + hex_dig2
###############################################

#Convert concatenated values to base 10 variable
###############################################
ten_var = new_var
i = int(ten_var, 16)
last = str(i)
length = len(last)
###############################################

#map salt 
###############################################
d_r_test = sum(map(int, str(last)))
###############################################

#convert the base 10 variable into binary variable
###############################################
lastly = int(last)
newly = bin(lastly)
###############################################

#slice binary value between 140 and 780 digits (slice salt)
###############################################
splicer = str(newly)
flinger = splicer[140:780] #can be made a dependent variable slice
d_rf_test = sum(map(int, str(flinger)))
###############################################

#perform final calulation to render new PW core
###############################################
flappster = str(flinger) + str(last) + str(new_var) + str(d_r_test) + str(d_rf_test)
hash_object = hashlib.sha512(flappster)
hex_dig = hash_object.hexdigest()
link = str(hex_dig)
link2 = link[38:48] #can be made a dependent variable slice
#link3 = link[39:109:7] #prime gap for 10 values
link3 = link[39:49] #right shifted 1 obscures the following wrapper rules:

#defined base-16 wrapper rules (also works on base-10) #can be made more random by adding additional position rules
################################################
new_linksy = link2[0:1] #characteristic term at position 38, not part of PW core

#print "hidden link", new_linksy

if new_linksy == "a":
    slowprint ("@"+link3+"#%%")
    
if new_linksy == "b":
    slowprint ("$@"+link3+"&%%")
    
if new_linksy == "c":
    slowprint ("#!"+link3+"%")

if new_linksy == "d":
    slowprint ("!"+link3+"%#")

if new_linksy == "e":
    slowprint ("%"+link3+"!@!")

if new_linksy == "f":
    slowprint ("&%"+link3+"!!")

if new_linksy == "1":
    slowprint ("(!"+link3+"##")

if new_linksy == "2":
    slowprint ("@&"+link3+"%%")

if new_linksy == "3":
    slowprint ("&&"+link3+"!#")

if new_linksy == "4":
    slowprint (")@"+link3+"@)")

if new_linksy == "5":
    slowprint ("!"+link3+"@$#")

if new_linksy == "6":
    slowprint ("!!"+link3+"$#")

if new_linksy == "7":
    slowprint ("(@"+link3+"#$")

if new_linksy == "8":
    slowprint ("$$"+link3+"$$")

if new_linksy == "9":
    slowprint ("%%"+link3+"%!")

if new_linksy == "0":
    slowprint ("@@"+link3+"((")

###############################################

execfile ("pypass.py")
