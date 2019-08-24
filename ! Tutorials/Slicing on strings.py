#  slicing and indexing methods on strings (and others)
#     stop value = first element not returned
#     [ start : len() : step ]           output starts at 0, so (len() - 1)  elements displayed

eg = 'This is a demonstration'
print(eg[::-1])           (negative step)
# output: noitartsnomed a si sihT

eg[:]   returns whole string
eg[::]  returns whole string
eg[:::] is an error   
eg[0:len(eg)]  returns whole string

eg[::]    ==   eg[ 0 : len(eg) : 1 ]

eg[-1] is the last element in eg,
but when used in slicing, 
negative index: [:-n] returns all but the last n elements

eg[:-3]  =  start to -4
eg[-3:]  =  -3 to end

eg[:n] + eg[n:] == eg

eg[4:2]     when first index > second, --> empty string

s = 'Robbie'
t = s[:]
id(s) == id(t)       True

s = abcde
ss = s*5
ss[::5] --> aaaaa     # count from beginning
ss[2::5] --> ccccc

## When you are stepping backward, if the first and second indices are omitted,
## the defaults are reversed in an intuitive way:
## the first index defaults to the end of the string,
## and the second index defaults to the beginning.  

>>> s = '1234512345123451234512345'
>>> s[::-5]                                         54321
'55555'
# (-) sign reverses string; step = 5; count back starting at end, nothing to do with index

###########################

# Can't modify a string, but can build a copy with desired changes.

s = 'Robbie'
ss = s[:2] + 'x' + s[4:]

or use replace:

ss = s.replace('bb', 'x')

