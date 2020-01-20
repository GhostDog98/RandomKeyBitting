import random
from random import randrange
pins=int(input("Number of pins:"))
minp=int(input("Minimum pin height (e.g. 0):"))
maxp=int(input("Max pin height (e.g. 6):"))
macs =int(input("MACS of key:"))
bit1ofgroup = 0
bit2ofgroup = 1
iterations = -(-pins // 2)
thislist = [None] * 1000
x = 0
for x in range(1000):
    thislist[x] = random.randint(minp, maxp)
    x = x +1
bit1ofgroup = 0
bit2ofgroup = 1
for g in range(iterations):
    if thislist[bit1ofgroup] - thislist[bit2ofgroup] <= macs:
        print(thislist[bit1ofgroup])
        print(thislist[bit2ofgroup])
        bit1ofgroup = bit1ofgroup+2
        bit2ofgroup = bit2ofgroup+2
    else:
        bit1ofgroup = bit1ofgroup+2
        bit2ofgroup = bit2ofgroup+2
        iterations = iterations+1





