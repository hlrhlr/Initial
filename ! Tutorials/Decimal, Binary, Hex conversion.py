# Convert Decimal to Binary, Octal and Hexadecimal

# from https://www.programiz.com/python-programming/
#                  examples/conversion-binary-octal-hexadecimal 

dec = int(input("Enter a number to be translated:> "))
 
print()
print("The decimal value of",dec,"is:")
print(bin(dec),"in binary.")
print(oct(dec),"in octal.")
print(hex(dec),"in hexadecimal.")


# convert back to decimal:
#   print(int(binarynumber, 2)
#   print(int(octalnumber, 8)
#   print(int(hexnumber, 16)
