'''

The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?

'''
#gets next natural number
def nextNat(nat,i):
  return nat+i

#finds number of products a natural number has
def natProds(nat):
  prods=2
  for i in range(2,nat/2+1):
    if nat%i==0: prods+=1
  return prods

topProds=1
prods=1
nat=1
i=2

#until a natural number with over 500 products is found, keep checking for natural numbers and counting their products
while topProds < 500:
  nat=nextNat(nat,i)
  prods=natProds(nat)
  if prods > topProds:
    topProds=prods
    print("Number {}: {} products".format(nat,topProds))
  i+=1
  
print ("\nNatural number {} has {} products.\n".format(nat,topProds))