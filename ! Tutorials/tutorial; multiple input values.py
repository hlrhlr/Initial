# tutorial: input multiple data from user

#   USING split():

x, y, z = input("Enter three values, space between:> ").split()
# may need to int(string)
print('x is ', x)
print('y is ', y)


a, b = input("Enter two values:> ").split()
print("The numbers are {} and {}.".format (a,b))
print(f"Variable a is  {a}, and Variable b is {b}" )   # f strings


listOfValues = list(map(int,input("Enter a series of values:> ").split()))   # map
print(listOfValues)
# input must be numeric


#   USING LIST COMPREHENSIONS:

x, y = [int(x) for x in input ("Enter two values:> ").split()] 
print(x)
print(y) 
# note: don't define x, y separately; 'for' loop fills variables
# or use alternate output line (format)


# Multiple inputs to a list:

listOfValues = [int(s) for s in input("Enter multiple values:> ").split()]
print(listOfValues)





