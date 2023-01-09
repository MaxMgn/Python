
import random

dec = 5
bin = ""
print ('decimal: ', dec)
while dec != 0:
    bin = str(dec %2) + bin
    print (bin)
    dec //= 2

print ("binary: ", bin) 
