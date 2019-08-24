# from https://www.geeksforgeeks.org/python-count-occurrences-of-a-character-in-string/


# Python3 code to demonstrate  
# occurrence frequency using  
# naive method  
  
# initializing string  
test_str = "GeeksforGeeks"
  
# using naive method to get count  
# counting e  
count = 0
  
for i in test_str: 
    if i == 'e': 
        count = count + 1
  
# printing result  
print ("Count of e in GeeksforGeeks is : "
                            +  str(count))

================


# Python3 code to demonstrate  
# occurrence frequency using  
# count() 
  
# initializing string  
test_str = "GeeksforGeeks"
  
# using count() to get count  
# counting e  
counter = test_str.count('e') 
  
# printing result  
print ("Count of e in GeeksforGeeks is : "
                           +  str(counter)) 


====================


# Python3 code to demonstrate  
# occurrence frequency using  
# re + findall() 
import re 
  
# initializing string  
test_str = "GeeksforGeeks"
  
# using re + findall() to get count  
# counting e  
count = len(re.findall("e", test_str)) 
  
# printing result  
print ("Count of e in GeeksforGeeks is : "
                            +  str(count)) 

===========================
# from https://www.geeksforgeeks.org/count-occurrences-of-a-word-in-string/

More string exercises here

# Python program to count the number of occurrence  
# of a word in the given string given string 
  
def countOccurences(str, word): 
      
    # split the string by spaces in a 
    a = str.split(" ") 
  
    # search for pattern in a 
    count = 0
    for i in range(0, len(a)): 
          
        # if match found increase count  
        if (word == a[i]): 
           count = count + 1
             
    return count        
  
# Driver code 
str ="GeeksforGeeks A computer science portal for geeks  "
word ="portal"
print(countOccurences(str, word)) 

========================
see also:
    
    Count occurrences of a string that can be constructed from another given string
    Count of occurrences of a "1(0+)1" pattern in a string
    Count occurrences of a sub-string with one variable character
    Count occurrences of a character in a repeated string
    Python | Count occurrences of a character in string
    Count occurrences of a substring recursively
    Python | Count occurrences of an element in a Tuple
    Python | Count occurrences of an element in a list
    Most frequent word in first String which is not present in second String
    String containing first letter of every word in a given string with spaces
    Replace all occurrences of pi with 3.14 in a given string
    Replace all occurrences of a string with space
    Remove all occurrences of a character in a string
    Rearrange a binary string as alternate x and y occurrences
    Replace all occurrences of string AB with C without using extra space













