# Functions


##def multiply(a,b):
##    """Multiplies two numbers"""
##    return a*b
##
##print(multiply(3,8))
##print(multiply.__doc__)

#================================
##
##def Hello(name = 'everybody'):
##    return name
##
##print(Hello())                                  # called with no arguments, returns default
##print(Hello ('bob'))                        # called with an argument, returns it

#=================================

### keyword parameters
##
##def addup(a,b,c=0, d=0):
##    """Adds two, three, or four numbers"""
##    sum = a+b+c+d
##    return sum
##
##print(addup(2,3))
##print(addup(4,6,7))
##print(addup(4))         # error; two obligatory arguments

#==================================

def calculate_mean(first, *values):                                 # or (arg1, *var_tuple)
                                                                                                # *values same as *args    
    return(first + sum(values)) / (1 + len(values))

print(calculate_mean(4,6,8,10))

# *values is a tuple reference, tuple of as many numbers as entered as arguments

#====================================

# if argument is a list, need to unpack it with *

data = [3, 6, 8, 233, 456]

print(calculate_mean(*data))

#=====================================

print('cats')
print('dogs')
print('cats', end=' ')
print('dogs')

print('cats', 'dogs', 'mice')
print('cats', 'dogs', 'mice', sep = ' & ')


#======================================

def many ( *args, **kwargs):
    print (args)
    print (kwargs)

many ( 1,2,3,Name='Bob', Job='cook')

returns a tuple    (1, 2, 3)
and a dictionary {'Name': 'Bob', 'Job': 'cook'}


#=========================================

         




      

      
