# string methods practice

eg = "Quod erat demonstrandum"

print(eg.replace(' ', ''))
print(eg.replace(' ', '$'))

##letterbin = []
##for s in eg:
##    letterbin.append(s)
##print(letterbin)                # list of strings


together = ''                   # reassemble original string; better way follows
for s in eg:
    together = together + s
print(together)
########################
eg = "Quod erat demonstrandum"

letterbin = []
for s in eg:
    letterbin.append(s)     
print(letterbin)

# this generates a list of one-letter strings

# reassemble to a string

output=''           # a bin
print(output.join(letterbin))                                                                                 # Join              

#######################



#######################
print(eg.upper())
print(eg.title())
print(eg.casefold())        # lower case
print(eg.swapcase())     # lower to upper, vice versa
print(eg.capitalize())       # first letter only to upper case
print("The letter 'Q' is at index: ", eg.index('Q'))

##########################

list_of_strings = ['a', 'b', 'c', 'd', 'e']                                                     #  Join List --> String

reunited = (' ').join(list_of_strings)

print(reunited)         # ---> a b c d e

##############################

eg2 = 'My dogs are called Merle, Lily, and Robin'

print(eg2.split(','))          # creates a list, separated at ','                  #  Split String --> List

################################

# Built-in String Functions

str()
len()
chr(123) #   integer --> character; both also work for unicode
ord('#')   #  character --> integer

print('whatever', end = '?') 



               
      

      
