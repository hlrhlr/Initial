# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 16:24:22 2019

@author: HLR, after web tutorials


"""

try:
    do something
except ErrorValue as err:
    print(err)
    
finally:            # optional
    do something else
    close file, etc

#=============================================

if whatever > 100:
    raise Exception ("whatever must be < 100")

#=============================================
    
    
ErrorValues include:
    IOError
    ImportError
    ValueError
    EOFError
    TypeError
     ... and others    