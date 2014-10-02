"""

A palindromic number reads the same both ways.
The largest palindrome made from the product of
two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.

"""

#function to chck for palindromes
def bigPalin(small,big):
    num1=big
    num2=big
    maxi=0

    while num1 >= small: 
        while num2 >= small:
            if(str(num1*num2)==str(num1*num2)[::-1]): #if is same number forward and backward
                if(maxi< num1*num2): #if current maximum is less than palindrom result
                    maxi=num1*num2
                    print(maxi)
            num2-=1
        num1-=1
        num2=big
    return maxi

pal=bigPalin(100,999) #min + max for 3-digits
if(pal != 0): print("Maximum Palindrome:",pal)
else: print("No palindrome for digit range")

