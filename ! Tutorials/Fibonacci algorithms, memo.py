# Fibonacci
# from https://www.python-course.eu/python3_recursive_functions.php


#The Fibonacci numbers are easy to write as a Python function.
# It's more or less a one to one mapping from the mathematical definition:

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# An iterative solution is also easy to write, though the recursive solution looks
# more like the definition:

def fibi(n):
    old, new = 0, 1
    if n == 0:
        return 0
    for i in range(n-1):
        old, new = new, old + new
    return new

# If you check the functions fib() and fibi(), you will find out that the iterative version fibi()
# is a lot faster than the recursive version fib(). To get an idea of how much this
# "a lot faster" can be, we have written a script, which uses the timeit module,
# to measure the calls. To do this, we save the function definitions for fib and fibi
# in a file fibonacci.py, which we can import in the program (fibonacci_runit.py) below:

from timeit import Timer

t1 = Timer("fib(10)","from fibonacci import fib")

for i in range(1,41):
	s = "fib(" + str(i) + ")"
	t1 = Timer(s,"from fibonacci import fib")
	time1 = t1.timeit(3)
	s = "fibi(" + str(i) + ")"
	t2 = Timer(s,"from fibonacci import fibi")
	time2 = t2.timeit(3)
	print("n=%2d, fib: %8.6f, fibi:  %7.6f, percent: %10.2f" % (i, time1, time2, time1/time2))


#============================


# We can implement a "memory" for our recursive version by using a dictionary
# to save the previously calculated values.

memo = {0:0, 1:1}
def fibm(n):
    if not n in memo:
        memo[n] = fibm(n-1) + fibm(n-2)
    return memo[n]
