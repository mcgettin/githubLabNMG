"""

2520 is the smallest number that can be divided by each
of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20?

"""


num=loop=20 #init vaiables
found=0

while not found:
    found=1 #will break loop if not changed in the following loop
    for i in range(loop): 
        if(num%(i+1)):    #from 1-20, check for remainders
            found=0 #if so number is not the answer
            num+=1 # so add 1 and try again
            
            
print(num) 

