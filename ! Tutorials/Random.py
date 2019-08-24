# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 18:22:18 2019

Random module
See also secrets module

"""
import random
#print(random.random())
# generates float between 0 and 1.0

#print(random.seed(5))
# allows returning to same random number later

#print(random.randint(2,100))
# range

x = [random.randint(0, 9) for p in range(0, 10)]
print(x)

#print(random.randrange(2,100,3))
# step; returns an integer

print(random.uniform(2,100))
# returns a float

pets = ['Merle', 'Lily', 'Robin', 'Robbie']
print(random.choice(pets))
print(pets)
random.shuffle(pets)
print(pets)         # changes list


