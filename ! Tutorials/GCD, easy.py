# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:59:26 2019

@author: HLR

"""

def gcd(a,b): 
    if(b==0): 
        return a 
    else: 
        return gcd(b,a%b) 
 
# should have test to ensure a>b, neither = 0.    