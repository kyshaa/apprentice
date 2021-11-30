def array_properties(a):
    print(f'a =\n{a}')
    print('dim =', a.ndim)
    print('shape =', a.shape)
    print('datatype =', a.dtype)
    print('size =', a.size)
    
# --------------------------------------------------------------------------------------------------------------------

""" Assignment : Index splitting """

# 1. Create an array of shape (100,100,3) of unsigned integer 8 bits filled with random values between 0 to 256.
# 2. Find the values that are less than 30, 50, 100, 250.
# 3. Split the array into 4 parts vertically and horizontally
# 4. Copy array from Question 1 and change the values that are les than 110 to 0 and others to 255
# 5. Hint: Use random seed of 12345


# 1. Create an array of shape (100,100,3) of unsigned integer 8 bits filled with random values between 0 to 256
# 5. Hint: Use random seed of 12345

import numpy as np

np.random.seed(12345)
a = np.random.randint(0, 256, (100, 100, 3), dtype = 'uint8')
array_properties(a)



# 2. Find the values that are less than 30, 50, 100, 250.

# To print full array in output, change threshold=np.inf. Default is threshold=1000 
np.set_printoptions(threshold=1000)

a30 = a < 30
print('\nValues that less than 30:\n', a[a30])

a50 = a < 50
print('\nValues that less than 50:\n', a[a50])

a100 = a < 100
print('\nValues that less than 100:\n', a[a100])

a250 = a < 250
print('\nValues that less than 250:\n', a[a250])



# 3. Split the array into 4 parts vertically horizontally

# .hsplit and .vsplit : return list containing the splitted array as the list's element

a4_horizontal = np.hsplit(a,4)
print('\nParts in array element horizontaly splitted array:',len(a4_horizontal))
print('\nArray element in horizontaly splitted array:\n',a4_horizontal)

print('\n----------------------------------------------------------------------------------------------------------------------------')
a4_vertical = np.vsplit(a,4)
print('\nParts in array element vertically splitted array:',len(a4_vertical))
print('\nArray element in vertically splitted array:\n',a4_vertical)



# 4. Copy array from Question 1 and change the values that are less than 110 to 0 and others to 255

b = a.copy()

# np.where (condition, x, y) : to replace values that meet condition with x and those that do not with y.
b_new = np.where(b < 110, 0, 255) 

print('\nNew Array : \n', b_new)

















































