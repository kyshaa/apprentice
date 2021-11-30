# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 16:51:51 2021

@author: User
"""


def array_properties(a):
    print(f'a =\n{a}')
    print('dim =', a.ndim)
    print('shape =', a.shape)
    print('datatype =', a.dtype)
    print('size =', a.size)
    

# --------------------------------------------------------------------------------------------------------------------


"""2D array"""

import numpy as np

a1 = np.arange(1, 17)

a2 = np.resize(a1, (4,4))
array_properties(a2)

# --------------------------------------------------------------------------------------------------------------------

"""Boolean and integer indexing"""

# we have been using integer for indexing all along in a particular format as [start, stop,step]
# however, we can make use of array of integer and boolean (True or False) values as direct indexing value
# normal indexing for obtaing the odd and even index of an array


import numpy as np

a1 = np.arange(9) 
array_properties(a1)

print('Odd index Elements:', a1[1::2])
print('Even index Elements:', a1[::2])

# In other to use integer or boolean index the array of integer 
# and array of boolean must have similar dimension to the original array to be accessed.
# Using array of integer indexing

i_odd = np.array([1,3,5,7])

bool_odd = np.array([False, True,False, True,False, True,False, True,False])

print('Odd index Elements:', a1[1::2])
print('Odd index Elements:', a1[i_odd])
print('Odd index Elements:', a1[bool_odd])


# --------------------------------------------------------------------------------------------------------------------

"""Class Activity 1"""

# 1. Create an array of 1D from 1 to 9
# 2. Print the odd values using normal, integer and boolean indexing.
# 3. Print the even values using normal, integer and boolean indexing.


import numpy as np

a9 = np.arange(1,10)

array_properties(a9)

# odd values using integer
iodd = np.array([0,2,4,6,8])

print('\n-------------Odd Integer-------------')
a_odd = a9[iodd]
array_properties(a_odd)

# even values using integer
ieven = np.array([1,3,5,7])

print('\n-------------Even Integer-------------')
a_even = a9[ieven]
array_properties(a_even)


# get odd value from array of 1 to 9
# using boolean indexing

# create array a, of 1 to 9

# create array of boolean of same shape as array a, with desired index equal to True

bool_odd = np.array([True,False, True,False, True,False, True,False, True])
print('\n------------------Odd Elements-----------------')
print('Normal method    :', a9[0::2])
print('Integer method   :', a9[iodd])
print('Boolean Indexing :', a9[bool_odd])


bool_even = np.array([False, True,False, True,False, True,False, True,False])
print('\n-----------------Even Elements-----------------')
print('Normal method    :', a9[1::2])
print('Integer method   :', a9[ieven])
print('Boolean Indexing :', a9[bool_even])


# --------------------------------------------------------------------------------------------------------------------

"""Class Activity 2"""
  
# 1. Write the index for the even number contain in the array (my_arr) below:
#    28 = [0,1], 22 = [0,5]
#        >> 50 = [1,0], 66=[1,2], 92=[1,1], 98=[1,3], 74=[1,6]
#        >> 44, 60, 98
#        >> 96, 38
#        >> 8, 66, 92, 62
# 2. Write the index for the number divisible by 5 contain in the array (my_arr) below.
#     >> 75 = [0,0]
#     >> 50 = [1,0]
#     >> 85=[2,2], 35=[2,3], 60=[2,4]
#     >> 55=[3,2]


import numpy as np

my_arr = np.random.randint(1, 100, (5,7))
array_properties(my_arr)

"""
since rand int is used, so the array kept changing when run in Spyder, so fixed array are:
    
    a = 
         [[75 28 47 61 69 22 93]
         [50 92 66 98  1 67 74]
         [44 67 85 35 43 60 98]
         [96 38 55 37 93 47 33]
         [37 59 27  8 66 92 62]]
"""
idiv5 = np.array([
    # - 75 = 
    [0,0],
    #    - 50 = 
    [1,0],
    #    - 85=
    [2,2], 
    # 35=
    [2,3], 
    # 60=
    [2,4],
    #    - 55=
    [3,2]
   
])

result = my_arr[idiv5]
array_properties(result)


# find modulus of my_arr
# the values divisible by 5 will be equal to zero

ibooldiv5 = my_arr % 5
array_properties(ibooldiv5)

# compare each values with zero to and assign back to ibooldiv5 for array element to be in boolean datatype
ibooldiv5 = ibooldiv5 == 0
array_properties(ibooldiv5)

# use the new boolean array for indexing
result = my_arr[ibooldiv5]
array_properties(result)


# --------------------------------------------------------------------------------------------------------------------

import numpy as np

a2 = np.arange(1,17).reshape(4,4) 

array_properties(a2)

print('Elements in rows 2 to 3 and columns 2 to 3:\n', a2[1:3,1:3])


i = np.array([[1,1],[2,2]])
j = np.array([[1,2],[1,2]])
print('\nElements in i:\n', a2[i])
print('\nElements in j:\n', a2[:,j])
print('\nElements in rows 2 to 3 and columns 2 to 3:\n', a2[i,j])

print('\n')
a2_c = np.full_like(a2,-100)
array_properties(a2_c)

print('\n')
a2_c[1:3,1:3] = a2[1:3,1:3]
print(a2_c)

print()

a2_bool = a2_c == a2
print(a2_bool)

print('\nElements in rows 2 to 3 and columns 2 to 3:\n', a2[a2_bool])


b1 = np.array([False, True, True, False])
b2 = np.array([False, True, True, False])
print('\n')
print('Elements in b1:\n', a2[b1])
print('\nElements in b2:\n', a2[:,b2])
print('\nElements in b1,b2:\n', a2[b1,b2])


# --------------------------------------------------------------------------------------------------------------------

"""Class Activity 3"""
 
# 1. Create an array of shape (5,6), range of int betweeon 0 and 2000 and
# 2. print the even numbers
# 3. print the odd numbers
# 4. print number divisible by 11.
# 5. Seed of random 12345

# 1. Create an array of shape (5,6), range of int betweeon 0 and 2000 and 
# 5. Seed of random 12345

import numpy as np 

# seed = generate same number all the time
np.random.seed(12345)

a_5x6 = np.random.randint(0, 2000, (5,6))
array_properties(a_5x6)


# 2. print the even numbers
print('\n-----------------------------Even numbers----------------------------')
ibool_even = (a_5x6 % 2) == 0

array_properties(a_5x6[ibool_even])

# 3. print the odd numbers
print('\n------------------------------Odd numbers------------------------------')
ibool_odd = ibool_even == False

array_properties(a_5x6[ibool_odd])

# 4. print number divisible by 11.
divide_by11 = a_5x6 % 11
array_properties(divide_by11)

print('\n')
divide_by11 = divide_by11 == 0
array_properties(divide_by11)

print('\n--------------------------Divisible by 11--------------------------')
array_properties(a_5x6[divide_by11])











