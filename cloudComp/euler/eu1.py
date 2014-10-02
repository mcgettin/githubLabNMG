"""

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

"""

print("Sum of multiples of 3 or 5 under 1000")
input("[press start to begin]")

i=0
total=0
while i < 1000: #stop when we reach multiple bigger than 1000 
    if(i%5==0 or i%3==0): #ie if multiple of 5 or 3
        total+=i #add multiple to cumulative tally
        
    i+=1 #next number (will be used only if a valid multiple)

print("Answer is: ",total) #prints answer

