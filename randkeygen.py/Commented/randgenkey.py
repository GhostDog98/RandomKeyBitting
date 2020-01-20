import random
from random import randrange







pins=int(input("Number of pins:")) # number of pins
minp=int(input("Minimum pin height (e.g. 0):")) # min pin hieght
maxp=int(input("Max pin height (e.g. 6):")) #max pin hight
#NGen=100 # Number of combo's to do at once
macs =int(input("MACS of key:"))# if 2 beside pins are of greater value then this the key will not work
bit1ofgroup = 0 # This controls which part of the list to call per bitting request
bit2ofgroup = 1 # same as above
iterations = -(-pins // 2) # roof round the number in case of odd value of 'pins', this variable controls how many times to run the code
#That controls sorting the random list

FinalBitting = [None] * pins # The final list for the bitting
thislist = [None] * 1000 # Temp list for all random numbers used in this 'seed' of the program

# All the needed values are now assigned




x = 0
for x in range(1000):
    thislist[x] = random.randint(minp, maxp) # genorate random values for all space in 'thislist'
    x = x +1

# unsorted and unfiltered list is now in the list "thislist" which has a length of the pins variable


bit1ofgroup = 0
bit2ofgroup = 1




#print("The RNG seed for this combo was: %s  If you are having trouble with errors file a report and include this number" %(seed))
for g in range(iterations):
    if thislist[bit1ofgroup] - thislist[bit2ofgroup] <= macs:
        print(thislist[bit1ofgroup])
        print(thislist[bit2ofgroup])

        FinalBitting[bit1ofgroup] = thislist[bit1ofgroup]
        FinalBitting[bit2ofgroup] = thislist[bit2ofgroup]
        
        bit1ofgroup = bit1ofgroup+2
        bit2ofgroup = bit2ofgroup+2
    else:
        bit1ofgroup = bit1ofgroup+2
        bit2ofgroup = bit2ofgroup+2
        print("Cut not suitable, rerolling")
        iterations = iterations+1



# Note: For future dev. a list called "FinalBitting" holds the normally printed values in a list



