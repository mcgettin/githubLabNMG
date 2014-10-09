#WARNING: this program takes about 7hrs to complete
#(tested on 2GHz-Dual Core)

'''

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

'''

#prime func again
def isPrime(num):
    for i in range(2,int(num/2)+1):
        if not num%i:
            return False
    return True

maxi=2000000
tally=0

for i in reversed(range(2,maxi)): #reversed just gives an idea of time scale
    if(isPrime(i)):
        tally+=i #add to tally if prime
        print(i)

print("\nTally:",tally)
input("\n\n[ENTER] to close...")

