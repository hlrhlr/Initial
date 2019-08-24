#  Formatted string literals (f-strings) in Python

a, b = input("Enter two values:> ").split()
print("The numbers are {} and {}.".format (a,b))
print(f"Variable a is  {a}, and Variable b is {b}" )   # f strings


import datetime
today = datetime.datetime.today()
print(f'{today:%B %d, %Y}')





