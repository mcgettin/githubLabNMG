"""

The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first
one hundred natural numbers and the square of the sum.

"""

#function for the sum of the squares of numbers from 1 to max 
def sumSqu(maxi):
    tally=0 #for counting up the squares
    for i in range(maxi):
        tally+=((i+1)**2) #add squared number to tally
    return tally #return the sum of all te squares

#function for the square of the sum of numbers from 1 to max 
def sqSum(maxi):
    tally=0 #for getting the sum of the numbers
    for i in range(maxi):
        tally+=(i+1)
    return (tally**2)    #return to square of the sum of numbers

print("Difference is:",sqSum(100)-sumSqu(100)) #result

