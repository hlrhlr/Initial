# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 18:47:25 2019

@author: HLR   works.

"""

import random
  
def Rand(start, end, num): 
    results = [] 
  
    for j in range(num): 
        results.append(random.randint(start, end)) 
  
    return results
  
# Driver Code 
num = 100
start = 1
end = 200
results = Rand(start, end, num) 
sresults=str(results)            # must be string
rns = open("randoms.txt", "w")
rns.write(sresults)

rns.close()