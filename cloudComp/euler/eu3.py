"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

"""

#function to test if a numbr is prime or not
def isPrime(num):
    for i in range(2,int(num/2)+1): #valid range for checking prime
        if not num%i: #if remainder is 0 for any num in range, then not prime
            return False 
    return True #must be prime if reaches here

#function to find the next prime factor
def getNextFactor(fac,num):
    for i in range(int(fac)+1,int(num/2)+1): #from last factor to half of num (valid range)
        if (not num%i): #is a factor
            return i
    return int(num/2)+1 #no more factors, sets off end progam



num= 600851475143 #big number
fac,pfac=1,1 #factor, prime factor
while(fac<(num/2)): # as long as factor is less than half the number 
    fac=getNextFactor(fac,num) #find next factor
    print("factor",fac)
    if (isPrime(fac)): #is it a prime factor?
        print("-- Prime factor of ",num,": ",fac,)
        pfac=fac


print("\nGreatest prime factor is:",pfac)

