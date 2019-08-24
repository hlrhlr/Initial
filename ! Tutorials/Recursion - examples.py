#  from   https://www.journaldev.com/23647/python-reverse-string

#################################################

# string reversal

eg = 'This is a demonstration'

def reverse_recursion(s):
    if len(s) == 0:
        return s
    else:
        return reverse_recursion(s[1:]) + s[0]

print(reverse_recursion(eg))

##############################################

# GCD

This version of code utilizes Euclid's Algorithm for finding GCD.

def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)


    ###########################################

# GCD

def gcd(a,b):
    return a if not b else gcd(b, a%b)

#################################################

# GCD

def gcd(x,y):
    while y != 0:
        (x,y) = (y, x%y)
    return x   


################################################

# Factorials

def fact(x):
    if x == 0:
        return 1
    return x * fact (x -1)

