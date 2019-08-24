# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 23:08:30 2019

@author: HLR

"""
string1 = "This is a string."
string2 = "12345654321"
print()
if string1 == string1[::-1]:
    print ("It's palindromic.")
else:
    print(string1[::-1])
    print ("Not palindromic.")

print()

if string2 == string2[::-1]:
    print ("It's palindromic.")
else:
    print ("Not.") 