# Matrix Transposition
# from : https://www.programiz.com/python-programming/examples/transpose-matrix


# Program to transpose a matrix using nested loop

X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)

   ########################

# Program to transpose a matrix using list comprehension 

X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]

for r in result:
   print(r)
# ++++++++++++++++++++++++++++++++++

# from https://www.geeksforgeeks.org/transpose-matrix-single-line-python/

##Using Nested List Comprehension: Nested list comprehension are used to iterate
##through each element in the matrix.In the given example ,we iterate through each
##element of matrix (m) in column major manner and assign the result to rez matrix
##which is the transpose of m.
## 
m = [[1,2],[3,4],[5,6]] 
for row in m : 
    print(row) 
rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))] 
print("\n") 
for row in rez: 
    print(row)

    =======================

##Using zip: Zip returns an iterator of tuples, where the i-th tuple contains the i-th element
##from each of the argument sequences or iterables. In this example we unzip our array
##using * and then zip it to get the transpose.
## 
matrix=[(1,2,3),(4,5,6),(7,8,9),(10,11,12)] 
for row in matrix: 
    print(row) 
print("\n") 
t_matrix = zip(*matrix) 
for row in t_matrix: 
    print(row) 
 ==========================

## Using numpy: NumPy is a general-purpose array-processing package designed
## to efficiently manipulate large multi-dimensional arrays.
## The transpose method returns a transposed view of the passed multi-dimensional matrix.
 
# You need to install numpy in order to import it 
# Numpy transpose returns similar result when  
# applied on 1D matrix

import numpy  
matrix=[[1,2,3],[4,5,6]] 
print(matrix) 
print("\n") 
print(numpy.transpose(matrix))

#===============================

##Transpose a matrix in Single line in Python
##https://www.geeksforgeeks.org/transpose-matrix-single-line-python/
##
##Using Nested List Comprehension: Nested list comprehension are used to iterate
##through each element in the matrix.In the given example ,we iterate through each
##element of matrix (m) in column
##major manner and assign the result to rez matrix which is the transpose of m.

#  ... more methods here also ... 

m = [[1,2],[3,4],[5,6]] 
for row in m : 
    print(row) 
rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))] 
print("\n") 
for row in rez: 
    print(row) 









    
