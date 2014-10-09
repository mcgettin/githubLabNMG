"""

By listing the first six prime numbers: 2, 3, 5, 7, 11,and 13,
we can see that the 6th prime is 13.
What is the 10 001st prime number?

"""

#previously used function for prime
def isPrime(num):
    for i in range(2,int(num/2)+1):
        if not num%i:
            return False
    return True


maxi=10001 #this is the Nth prime number (i.e. 1st is 2, 2nd is 3)
pri=1 
i=0
while i < 10001: #keep goinguntil we find the maxi prime
    pri+=1
    while not isPrime(pri): pri+=1 #keep in loop until prime is found
    i+=1 #escapes; so increases prime iteration (i.e. which prime we're at)

print("prime #",maxi," is:",pri)  

