# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 18:32:27 2019

@author: HLR

First try at implementing some NT functions

"""
 
def gcd(a,b): 
    if(b==0): 
        return a 
    else: 
        return gcd(b,a%b) 
 
       
#x,y = input("Enter two numbers:>  ").split()
x, y = [int(x) for x in input("Enter two values:>").split()]

x = int(x)
y = int(y)


if gcd(x,y) == 1:
    print("GCD = 1; numbers are relatively prime.")
else:
    print("GCD of these numbers is:> ", gcd(x,y))


##################

# from bckurera:

def calculate_phi(n):
    phi_n = 1
    count = 0
    i = 2
    while (i<n):
        r = gcd_euc(n, i)
        i = i + 1
        if(r==1):
            phi_n = phi_n + 1
    return phi_n

##############
