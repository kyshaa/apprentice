# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 11:11:49 2021

@author: User
"""

# slicing a list

a = [3, 5, 6, 7, 8, "nine", 7, 23, 45, 67, 89]
print (a[0])
print (a[3:])       # start from 3rd index
print (a[:])
print (a[1:4])


# slicing 2D list

a = [1, 3, 5, 7]
b = [4, 5, 6, 9]
c = [a, b]
print (c)
print (c[0])
print (c[1][3:])    # starts from index 3 onwards
print (c[1][:4])    # end at index 4


# check to see if an item is in a list

L1 = [1, 3, 5]
print(3 in L1)

if 3 in L1:
    print("3 is in the list")
    
if 7 not in L1:
    print("7 is NOT the list")
    
else:
    print("No")
    

# repetition - repeat a list

L1 = [1, 3, 4]
L2 = L1*4
print(L2)


# Concatenate a list = combine elements into 1 list

L1 = [1, 3, 5]
L2 = [4, 5, 7] 
L3 = L1 + L2
print (L3)


# list manipulation

name = ["Nu' man", "Afiq", "James", "alkisah"]
print(name[1])
print(name[3])

# list manipulation 2

score_table = [["Nu' man", "Afiq", "James", "alkisah", "Musa"], [80, 75, 89, 92, 68]]
name_numan = score_table[0][0]
print(name_numan)

name_numan_s = score_table[1][0]
print(name_numan_s)

name_james = score_table[0][2]
james_score = score_table[1][2]
print(name_james, james_score)

# empty list
x = []

# 1 dimension list
b = [1,2,3,4,5,6,7,8,9]
print(len(b))

# list with mixed datatype
d = [1, 1.0, 1+3j, 'two', True]
print(type(d))
print(len(d))


# append function = add number to the list

num = [1, 5, 6, 9]
new_n = 89
num.append(new_n)
print(num)


# extend value num yg kat atas tu, masukkan value c pula

c = [23, 45, 46]
num.extend(c)
print(num)


# assign string to variable

a = """Guten tag!
    Ich bin Kisha.
    Sehr angenehm.
    Wie geht's'?"""
    
    
# splice string    

b = "Hello, World"
print(b[:5])        # execute from index 0 to index 4

b = "Hello, World"
print(b[2:])


# loop through the string 

for x in "banana":
    print(x)
    
for x in "banana":
    if x == 'b':
        print(x)


# string length

a = "Hello, World"
b = len(a)
print("len is {}".format(b))
print(f"len is {b}")


# check string - use keyword "in"

txt = "Ich liebe dich"
print("dich" in txt)

if "dich" in txt:
    print("pass")


# check string - use keyword "not in"

txt = "Ich liebe dich"
print("dich" not in txt)

if "dich" not in txt:
    print("pass")
    
    
# string formatting - Error: sbb datatype formatting campur str and int

age = 36
txt = "Ich bin Kisha. Mein Alter ist " + age
print(txt)


# string formatting - Success sbb datatype formatting only str

age = 36
txt = "Ich bin Kisha. Mein Alter ist {}"
print(txt.format(age))

# exercise datatype formatting

quantity = 3
itemno = 567
price = 49.95
myorder = "I wanna pay {2} dollars for {0} pieces of item {1}"
print(myorder.format(quantity, itemno, price))


# Eg1 : string = escape character

txt = 'Ich bin Kisha'
print(txt)

txt = "Mir geht's gut"
print(txt)

txt = "Guten\nTag!"
print(txt)


# Eg2: string = escape character

txt = 'Hello\tWorld'
print(txt)

txt = "\x48\x65\x6c\x6c\x6f"
print(txt)

txt = "\110\145\154\154\157"
print(txt)


# string modulo (%), space 10 spaces before write "test"

print ('%d'%(42,))
print ('{:>10}'.format('test'))


# Generic form of format string : fill alignment

import math

from math import pi
print(pi)
print('{0:0<20}'.format(pi))    # add from the right
print('{0:0>20}'.format(pi))    # add from the left
print('{0:0^20}'.format(pi))
print('{0:*<20}'.format(pi))


# Generic form of format string : sign 

import math
from math import pi

print('{0:+}'.format(pi))
print('{0:+}'.format(-1.0 * pi))
print('{0:-}'.format(pi))
print('{0: }'.format(pi))
print('{0:}'.format(-1.0 * pi))


# Generic form of format string : m, minimum total size of formatted string

import math
from math import pi

print('{0:10}'.format(pi))
print('{0:20}'.format(pi))
print('{0:30}'.format(pi))
print ('\n')


# Generic form of format string : c

import math
from math import pi

print('{0:.10}'.format(1000000 * pi))
print('{0:,.10}'.format(1000000 * pi))


# Generic form of format string : p, precision
# p kena ada dot (.)

import math
from math import pi

print('{0:.1}'.format(pi))
print('{0:,.2}'.format(pi))
print('{0:,.5}'.format(pi))



# Generic form of format string : t, way to present data type

import math
from math import pi

print('{0:.5e}'.format(pi))
print('{0:.5g}'.format(pi))
print('{0:.5f}'.format(pi))

print('{0:.5%}'.format(pi))

print('{0:.5e}'.format(100000 * pi))
print('{0:.5g}'.format(100000 * pi))
print('{0:.5f}'.format(100000 * pi))


# Exercise formatted string

s = 'Python'

print('{0:}'.format(s))
print('{0:>20}'.format(s))
print('{0:!>20}'.format(s))
print('The formatted string is : {0:!<20}'.format(s))


# Exercise formatted string

import textwrap
sample_text = '''
Python is a widely used high-level, general purpose, interpreted,
dynamic programming language. Its design philosophy emphasizes
code readability and its syntax allows programmers to express
concepts in fewer lines of code than possible in languages such
as C++ or Java.
    '''
    
print()
print(textwrap.fill(sample_text, width=50))
print()