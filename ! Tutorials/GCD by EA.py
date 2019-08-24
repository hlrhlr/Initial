#  GCD using Euclidean Algorithm
#  from https://www.programiz.com/python-programming/examples/hcf


def computeHCF(x, y):

   # This function implements the Euclidean algorithm to find H.C.F. of two numbers
   
   while(y):
       x, y = y, x % y

   return x

print(computeHCF(300, 400))


##This algorithm is based on the fact that H.C.F. of two numbers divides their difference as well.
##
##In this algorithm, we divide the greater by smaller and take the remainder.
##Now, divide the smaller by this remainder. Repeat until the remainder is 0.
##
##For example, if we want to find the H.C.F. of 54 and 24, we divide 54 by 24.
##The remainder is 6. Now, we divide 24 by 6 and the remainder is 0.
##Hence, 6 is the required H.C.F
##
##Here we loop until y becomes zero. The statement x, y = y, x % y does swapping
##of values in Python.  
##
##In each iteration, we place the value of y in x and the remainder (x % y) in y,
##simultaneously. When y becomes zero, we have H.C.F. in x..
