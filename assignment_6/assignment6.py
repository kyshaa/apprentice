# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 18:54:46 2021

@author: User
"""

""" Assignment Numpy """

# 1. Create an array of shape (10,10) with uint8 random values.
# 2. Print the shape, size and dimension. 
# 3. Compute the values of the third row to the last row.
# 4. Compute the average of the columns.


import numpy as np

np.random.seed(42)
arr = np.random.randint(0,256, (10,10), dtype='uint8')

print("\n------------------ Array Info ------------------\n")
print(f'Shape: {arr.shape}')
print('Size : {arr.size}')
print('Dimension: {arr.ndim}')
print('Datatype: {arr.dtype}')

arr3_last = arr[3:]

# Contains 7 element because only 7 rows remaining 
print('\nSum of EACH row from 3rd row to last row:', np.sum(arr3_last, axis=1))
print('Sum of ALL row from 3rd row to last row:', np.sum(arr3_last))

# Contains 10 element for each columns
print('\nAverage of EACH column: ', arr.mean(axis=0))
print('Average of ALL columns: ', arr.mean())






























