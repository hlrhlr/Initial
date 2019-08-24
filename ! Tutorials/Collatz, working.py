#  Collatz attempt

## Start with any positive integer n. Then each term is obtained from the previous term
## as follows:
##     if the previous term is even, the next term is one half the previous term.
## If the previous term is odd, the next term is 3 times the previous term plus 1.
## The conjecture is that no matter what value of n, the sequence will always reach 1.

counter = 0
n = int(input("Enter a number, any number:>  "))

def collatz (n):

    if n > 1:
        global counter
        if n % 2 == 0:
            n = n/2
            counter = counter + 1
            print("Even path n = ", (n))
            collatz(n)
        else:
            n = (3*n +1)
            counter = counter + 1
            print("Odd path n = ", (n))
            collatz(n)  
       
    #return n

print (collatz(n))  # prints 'None' but no output if this print is omitted
print("The Collatz algorithm, starting with ", (n), ",  took ", (counter),  " iterations.")

        
        
# !!! working ?

 
 
