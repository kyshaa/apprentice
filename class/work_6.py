# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 18:54:14 2021

@author: User
"""

"""Introduction To Numpy"""

# Numpy mean numerical python
# Used for numerical operation and manipulation. 
# Especially in array or matrix

# --------------------------------------------------------------------------------------------------------------------

"""Installation of numpy, scipy and pandas"""

# !pip install -q numpy

def array_properties(a):
    print(f'a =\n{a}')
    print('dim =', a.ndim)
    print('shape =', a.shape)
    print('datatype =', a.dtype)
    print('size =', a.size)
    
# --------------------------------------------------------------------------------------------------------------------

"""Creating array"""

# import package numpy and give it an alias np
# No specific array data type 


import numpy as np

a = np.array([
    [1, 2, 3],
    [4,5,6],
    [7,8,9]])

a_list = [
    [1, 2, 3],
    [4,5,6],
    [7,8,9]]

print(a)
print()
array_properties(a)
# OR
# print("a = \n", a)
# print("dim = ", a.ndim)
# print("shape = ", a.shape)
# print("datatype = ", a.dtype)
# print("size = ", a.size)          - how many element in that array
# print()

print(len(a_list))                  # - calculate number of rows in an array

type(a)
type(a_list)

print(a_list)
print(type(a))
print(type(a_list))


import numpy as np

blist = [31,32,33]
b = np.array(blist)

print(blist)
print(b)
print("dim = ", b.ndim)
print("shape = ", b.shape)
print("datatype = ", b.dtype)
print("size = ", b.size)          # - how many element in that array
print()


import numpy as np

clist = [1, 'Tue', 3, 'Wed']
c = np.array(clist)

print(clist)
print(c)
array_properties(c)
# datatype : <U11 - union of values datatype, contains many thing


# --------------------------------------------------------------------------------------------------------------------

""" Class Activity 1 """

d = np.array([[11, 12, 13]])
array_properties(d)


# Specifying array data type 

import numpy as np

d2 = np.array([[11, 12, 13]], dtype='int64')
array_properties(d2)

e = np.array([[21],[22],[31], [0]], dtype='uint8')
array_properties(e)


# --------------------------------------------------------------------------------------------------------------------

""" Specifying datatype """

import numpy as np

a = np.array(
    [
     [11,12,13]
    ], dtype='float'
)

print(a)
print("dim = ", a.ndim)
print("shape = ", a.shape)
print("datatype = ", a.dtype)
print("size = ", a.size)          # - how many element in that array
print()


# Specifying datatype float32

import numpy as np

a = np.array(
    [
     [11,12,13]
    ], dtype='float32'
)

print(a)
print("dim = ", a.ndim)
print("shape = ", a.shape)
print("datatype = ", a.dtype)
print("size = ", a.size)          # - how many element in that array
print()



# Float value

import numpy as np

a = np.array(
    [
     [11.0,12.0,13.0]
    ]
)

print(a)
print("dim = ", a.ndim)
print("shape = ", a.shape)
print("datatype = ", a.dtype)
print("size = ", a.size)          # - how many element in that array
print()



# --------------------------------------------------------------------------------------------------------------------

""" Class Activity 2 """

f = np.array(
        [
                [21],
                [22],
                [31],
                [0]
        ], dtype="float32"
)

print("f = \n",f)
print("dim = ", f.ndim)
print("shape = ", f.shape)
print("datatype = ", f.dtype)
print("size = ", f.size)          # - how many element in that array
print()


# --------------------------------------------------------------------------------------------------------------------

# Specifying datatype uint8

# uint8 means unsigned integer in 8 bits min = 0 max = 255
# int8 means signed integer in 8 bits min = - 128 max = 127

a = np.array(
        [
                [21],
                [22],
                [31],
                [0]
        ], dtype="uint8"
)

print("a = \n",a)
print("dim = ", a.ndim)
print("shape = ", a.shape)
print("datatype = ", a.dtype)
print("size = ", a.size)          # - how many element in that array
print()

# --------------------------------------------------------------------------------------------------------------------

""" Arange (array range)"""

import numpy as np
seq_a = np.arange(1,10)
array_properties(seq_a)

ar10 = np.arange(10)
array_properties(ar10)
for n in ar10:
    print(n, end=' | ')


# Range used regularly in for loop
for n in range(10):
    print(n)


# Range starts from 1 until 10, 10 must be inclusive so put put 10+1
for n in range(1, 10+1):
    print(n, end=', ')


# Step/ Jump by value in a range (Ex1)
start = 1
stop = 10 + 1
step = 2

for n in range(start, stop, step):
    print(n, end=' | ')


# Step/ Jump by value in a range (Ex2)
start = 1
stop = 10 + 1
step = 2

ar10b = np.arange(start, stop, step)
ar10b = np.uint8(ar10b)                 # convert type of the array
array_properties(ar10b)

for n in ar10b:
    print(n, end=' | ')
    
print()
print()

ar10b = np.float32(ar10b)
array_properties(ar10b)


# --------------------------------------------------------------------------------------------------------------------


""" Class Activity 3 """

# Create an array of integers [0, 5, 15, ..., 100]

import numpy as np

start = 0
stop = 100 + 1
step = 5

arr = np.arange(start, stop, step)
for n in arr:
    print(n, end = ' | ')

array_properties(arr)


# --------------------------------------------------------------------------------------------------------------------


""" Linspace """

# linspace function (line space) - to create an evenly spaced sequence in a specified interval
# create array of floating point value of a specific size


import numpy as np

seq_a2 = np.linspace(1, 10, 15)
array_properties(seq_a2)

# Ex1

start = 0
stop = 10
size = 11   # size must be stop+1

ar10_linsp = np.linspace(start, stop, size)
array_properties(ar10_linsp)


# Ex2

start = 0
stop = 10
size = 10

ar10_linsp = np.linspace(start, stop, size)
array_properties(ar10_linsp)

# Ex1 vs Ex2
# Ex1 akan produce output kemas [ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]
# sbb size dalam Ex adalah 11 tapi number ends at 10, so the number akn intrapolate

# Ex2 akn produce output [ 0.          1.11111111  2.22222222  3.33333333  4.44444444  5.55555556 6.66666667  7.77777778  8.88888889 10.        ] 
# sbb size dlm Ex2 adalah 10 so cukupkan space by desired size, cuma akn cut kat 9 sbb size 10 dan stop 10

#  1  2  3  4  5  6  7  8  9  10
#  0  1  2  3  4  5  6  7  8  9  
#  0  x  x  x  x  x  x  x  x  10

# 0 --> 0
# 1 --> x
# 2 --> x
# 9 --> 10


# so, value output akn hasilkan float .111 or .222 or etc sbb ratio :
x = 10/9 * 1
print (x)

y = 10/9 * 2
print(y)

z = 10/9 * 9
print(z)



# --------------------------------------------------------------------------------------------------------------------

""" Zeros """

# array of zeros


import numpy as np

zer_10a = np.zeros((1, 10))
array_properties(zer_10a)


import numpy as np

zer_10b = np.zeros((1, 10), dtype='float32')
array_properties(zer_10b)


import numpy as np

zer_10c = np.zeros((1, 10), dtype=np.uint8)
array_properties(zer_10c)


import numpy as np

zer_10d = np.zeros((1, 10), dtype="int")
array_properties(zer_10d)


import numpy as np

zeros_arr = np.zeros((2, 4))             
array_properties(zeros_arr)


import numpy as np

###### QUESTION : WHY DTYPE BELOW WRITTEN AS NP.UINT8 ######
# np.zeros((rows, inner rows, inner columns))
zer_5_4_3 = np.zeros((5, 4, 3), dtype=np.uint8)
array_properties(zer_5_4_3)


import numpy as np

# np.zeros((outer rows, inner rows, outer column, inner columns))
zer_4_5_3_2 = np.zeros((4, 5, 3, 2), dtype=np.uint8)
array_properties(zer_4_5_3_2)


# --------------------------------------------------------------------------------------------------------------------

""" Ones """

# create array of ones

import numpy as np

# specify the shape of the array in the 'np.ones' function
ones_arr = np.ones((4, 2))  

array_properties(ones_arr)


# 2-D array

import numpy as np

shape = (1,10)

ones_10 = np.ones(shape)

array_properties(ones_10)


# 1-D array

import numpy as np

shape = (10,)

ones_10 = np.ones(shape)

array_properties(ones_10)




# --------------------------------------------------------------------------------------------------------------------


""" Class Activity 4 """

# Create an array of dim 3 filled with ones.


ones_3dim = np.ones((2,3,4))
array_properties(ones_3dim)

# --------------------------------------------------------------------------------------------------------------------


""" Empty Array"""

# specify its own value

import numpy as np

emp_arr = np.empty((4, 4))

array_properties(emp_arr)


# --------------------------------------------------------------------------------------------------------------------


""" Class Activity 5 """

# Create empty array of 1x10

import numpy as np

emp_1x10 = np.empty((1, 10)) # or ((10,))

array_properties(emp_1x10)

# --------------------------------------------------------------------------------------------------------------------


""" Reshape Array"""


# create array of 1x10 then reshape to 2x5

import numpy as np

ar1x10 = np.arange(1,11)
array_properties(ar1x10)

print()

ar2x5_method1 = ar1x10.reshape((2,5))
array_properties(ar2x5_method1)

# another way is :
    
ar2x5_method2 = np.reshape(ar1x10,(2,5))
array_properties(ar2x5_method2)



# Error because cannot reshape if there are not in the same size 

import numpy as np

ar1s10 = np.linspace(10, 55, 10)
array_properties(ar1s10)

ar3x3_method1 = ar1s10.reshape((3,3))
array_properties(ar3x3_method1)



# reshape knowing only one dimension size

import numpy as np

ar1s10 = np.linspace(10, 55, 10)
array_properties(ar1s10)

# reshape into 5xunknown
ar5x = ar1s10.reshape((5,-1))
array_properties(ar5x)

ar_x5 = ar1s10.reshape((-1,5))
array_properties(ar_x5)


# --------------------------------------------------------------------------------------------------------------------


""" Class Activity 6 """

# Create an array of shape 4x5 and reshape into 2x-1

import numpy as np

ar20 = np.linspace(1,21,20)
array_properties(ar20)

ar4x5 = ar20.reshape((4,5))
array_properties(ar4x5)

ar2x = ar4x5.reshape((2,-1))
array_properties(ar2x )


# --------------------------------------------------------------------------------------------------------------------


""" Class Activity 7 """

# Create an array of 24 element or size
# Reshape into multiples of 3 and 4 in row dimension

import numpy as np

# create a 1 dim array of size 24
arr_1dim = np.arange(1, 25)
array_properties(arr_1dim )

# reshape into array of 3x-1
arr_3x = np.reshape(arr_1dim, (3,-1))
array_properties(arr_3x )

# reshape into array pf 4x-1
arr_4x = np.reshape(arr_1dim, (4,-1))
array_properties(arr_4x)

# --------------------------------------------------------------------------------------------------------------------


""" Class Activity 8 """

# Create an array of unsigned integer 8 bits of size 300 and reshape into (10,10,-1)

arr_uint8 = np.arange(0,300,dtype='uint8')
array_properties(arr_uint8)

print("\nReshape into (10,10,-1)")
arr_uint8 = arr_uint8.reshape(10,10,-1)
print(arr_uint8.shape)
array_properties(arr_uint8)


# --------------------------------------------------------------------------------------------------------------------

import numpy as np

ar300 = np.arange(0,300,dtype='uint8')
print(ar300.shape)

ar10x10x = ar300.reshape((10,10,-1))
print(ar10x10x)

# 10,-1,3
ar10x_x3 = ar300.reshape((10,-1,3))
print("\nReshape into (10,-1,3)")
print(ar10x_x3.shape)

# -1,10,3
ar_x10_x3 = ar300.reshape((-1,10,3))
print("\nReshape into (-1,10,3)")
print(ar_x10_x3.shape)

# -1,-1,3
# will be error because can only specify 1 unknown dimension
# ar_x_x3 = ar300.reshape((-1,-1,3))
# print("\nReshape into (-1,-1,3)")
# print(ar_x_x3.shape)


# --------------------------------------------------------------------------------------------------------------------


""" Random Array"""

# 'rand' will generate random values between 0 - 1
# it accepts the shape of the array to be created

import numpy as np

# random array between 0-1 with shape (4,5)
a1 = np.random.rand(4,5)

array_properties(a1)


# --------------------------------------------------------------------------------------------------------------------


""" Class Activity 9 """

# create an array with shape (3,7) of values between 0-1

import numpy as np

a2 = np.random.rand(3,7)

array_properties(a2)

# --------------------------------------------------------------------------------------------------------------------

""" Randint"""

# create array of integer
# accepts start, stop and shape
# 'randint(start,stop, shape)

import numpy as np

a3 = np.random.randint(0,10, (4,5))

array_properties(a3)


# --------------------------------------------------------------------------------------------------------------------


""" Class Activity 9 """

# create array of unsigned integer of 8 bits with shape (100,100,3) filled with random integer values

import numpy as np

a4 = np.random.randint(1,10, (100,100,3), dtype=np.uint8)

array_properties(a4)

# --------------------------------------------------------------------------------------------------------------------

 """Accessing an array element"""

# index         |  0 |  1 |  2 |  3 |  4 |  5 |  6 |  7 |  8 |  9 | 10 | 11 | 
# value         |  1 |  2 |  3 |  4 |  5 |  6 |  7 |  8 |  9 | 10 | 11 | 12 |
# special index |-12 |-11 |-10 | -9 | -8 | -7 | -6 | -5 | -4 | -3 | -2 | -1 |


# shape 13, akn bagi value up till 12

a0 = np.arange(1,13)
array_properties(a0)

# print a number in an array
print("First : ", a0[0])
print("Second : ", a0[1])
print("Third : ", a0[3])

print("Ninth : ", a0[9-1])
print("Last : ", a0[11])
# OR
print("Last : ", a0[-1])

# print a range of number in an array
# a0[istart:istop]

# stop or istop excluded
print("\nIndex 0 to 4 : ", a0[0:4])

# omit the istart
print("Index 0 to 4 : ", a0[:4])


print('\nindex 3 to 6: ', a0[3:6])


print('\nindex  0 to 10: ', a0[0:10])
print('\nindex  0 to 10: ', a0[:10])

#omit istop equal to last index
print('\nindex 3 to last: ', a0[3:12])
print('\nindex 3 to last: ', a0[3:])

# from istart to second to the last value
# index -1 equal to last index
print("\nindex 3 to second to the last : ", a0[3:-1])

# get odd positions
# a0( istart : istop : istep)
print("\nodd position : ", a0[0::2]) 

# get even positions
# a0( istart : istop : istep)
print("even position : ", a0[1::2]) 


# --------------------------------------------------------------------------------------------------------------------


 """ Use for loop for array """

import numpy as np

N = 12
a1 = np.arange(N+1)

array_properties(a1)
for i in range (N+1):
    print(f"{i} : {a1[i]}")

