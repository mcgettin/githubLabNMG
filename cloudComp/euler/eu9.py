"""

A Pythagorean triplet is a set of three natural numbers, a < b < c,
for which a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""


A=B=C=0 #the triplet variables to be found

for a in range (1,333): #logically worked out this as the only valid range for a
    if A is not 0: break 
    for b in range (a+1,499): #only valid range for b
        if A is not 0: break
        c=1000-b-a #and c makes up the 1000, for a+b+c=1000
        if c <= b: break
        #print(a,b,c)
        if (a**2+b**2) == c**2: #if triplet found, done. store it.
            A=a
            B=b
            C=c
            #print(a,b,c)
print("Product of triplet: ",A*B*C) #print ABC (i.e. product)

