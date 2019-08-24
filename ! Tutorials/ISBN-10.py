# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 11:17:06 2019

@author: https://www.geeksforgeeks.org/program-check-isbn/

The first nine digits of the ISBN number are used to 
represent the Title, Publisher and Group of the book 
and the last digit is used for checking whether ISBN 
is correct or not.

The first 9 digits of it, can take any value between 
0 and 9, but the last digits, sometimes may take value 
equal to 10; this is done by writing it as ‘X’.

To verify an ISBN, calculate 10 times the first digit, 
plus 9 times the second digit, plus 8 times the third 
digit and so on until we add 1 time the last digit. 
If the final number leaves no remainder when divided 
by 11, the code is a valid ISBN.

ISBN-10 to ISBN-13 conversion:
An ISBN-10 is converted to ISBN-13 by prepending "978" 
to the ISBN-10 and recalculating the final checksum 
digit using the ISBN-13 algorithm. The reverse process 
can also be performed, but not for numbers commencing 
with a prefix other than 978, which have no 10-digit 
equivalent.

also see:
https://stackoverflow.com/questions/4047511/checking-if-an-isbn-number-is-correct    

"""
def isValidISBN(isbn): 
  
    # check for length 
    if len(isbn) != 10: 
        return False
      
    # Computing weighted sum of first 9 digits 
    _sum = 0
    for i in range(9): 
        if 0 <= int(isbn[i]) <= 9: 
            _sum += int(isbn[i]) * (10 - i) 
        else: 
            return False
          
    # Checking last digit 
    if(isbn[9] != 'X' and 
       0 <= int(isbn[9]) <= 9): 
        return False
      
    # If last digit is 'X', add  
    # 10 to sum, else add its value. 
    _sum += 10 if isbn[9] == 'X' else int(isbn[9]) 
      
    # Return true if weighted sum of  
    # digits is divisible by 11 
    return (_sum % 11 == 0) 
  
# Driver Code 
isbn = "007462542X"
if isValidISBN(isbn): 
    print('Valid') 
else: 
    print("Invalid") 
      

