#  Matrix operations without Numpy
# https://www.programiz.com/python-programming/examples/multiply-matrix

##In Python we can implement a matrix as nested list (list inside a list).
##
##We can treat each element as a row of the matrix.
##
##For example X = [[1, 2], [4, 5], [3, 6]] would represent a 3x2 matrix.
##First row can be selected as X[0]
##and the element in first row, first column can be selected as X[0][0].
##
##Multiplication of two matrices X and Y is defined only if the number of
##columns in X is equal to the number of rows Y.
##
##If X is a n x m matrix and Y is a m x l matrix then, XY is defined and has
##the dimension n x l (but YX is not defined). Here are a couple of ways to
##implement matrix multiplication in Python.

############################

# Program to multiply two matrices using nested loops

# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)
##############################
# my script, copied from above:

matrix_a = [[1,2,3,4,5],
                     [6,7,8,9,10]]

matrix_b = [[11,12,13,14,15],
                      [16,17,18,19,20],
                      [16,17,18,19,20],
                      [16,17,18,19,20],
                      [16,17,18,19,20]]

result = [[0,0,0,0,0],
               [0,0,0,0,0]]

for i in range(len(matrix_a)):          # 2     2 rows
    for j in range(len(matrix_b[0])):  # 5    size of first row
        for k in range(len(matrix_b)):   # 5   5 rows
            result[i][j]+= matrix_a[i][k] * matrix_b[k][i]

for r in result:
                   print(r)
                   
 
# working

#############################
# another approach

Matrix Multiplication Using Nested List Comprehension

# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

# result is 3x4
result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

for r in result:
   print(r)

##########################
#  https://www.geeksforgeeks.org/multiplication-two-matrices-single-line-using-numpy-python/
##Using explicit for loops: This is a simple technique to multiply matrices
##but one of the expensive method for larger input data set.In this,
##we use nested for loops to iterate each row and each column.
##If matrix1 is a n x m matrix and matrix2 is a m x l matrix.


# input two matrices of size n x m 
matrix1 = [[12,7,3], 
        [4 ,5,6], 
        [7 ,8,9]] 
matrix2 = [[5,8,1], 
        [6,7,3], 
        [4,5,9]] 
  
res = [[0 for x in range(3)] for y in range(3)]  
  
# explicit for loops 
for i in range(len(matrix1)): 
    for j in range(len(matrix2[0])): 
        for k in range(len(matrix2)): 
  
            # resulted matrix 
            res[i][j] += matrix1[i][k] * matrix2[k][j] 
  
print (res)   

# =============================

# using numpy:


# We need install numpy in order to import it 
import numpy as np 
  
# input two matrices 
mat1 = ([1, 6, 5],[3 ,4, 8],[2, 12, 3]) 
mat2 = ([3, 4, 6],[5, 6, 7],[6,56, 7]) 
  
# This will return dot product 
res = np.dot(mat1,mat2) 
  
# print resulted matrix 
print(res)

##Here we used dot product and in mathematics the dot product is
##an algebraic operation that takes two vectors of equal size and returns a single number.
##The result is calculated by multiplying corresponding entries and adding up those products.
