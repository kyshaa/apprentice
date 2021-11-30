# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 12:06:21 2021

@author: User
"""

# ---------------------------------------------------------------------------------------------------------------------------------

"""Assignment Function"""

# 1. Write a function to get arguments by keywords and value:
#    initialTemp = 400.0, simulationTime = 35
#    (just print them in the function, try to call function with different number of args)

def my_function(initialTemp = 400.0, simulationTime = 35):
    print (f"The initial temperature is {initialTemp} °C and the simulation time is { simulationTime} s")

# different order will still be outputed the same because keywords is used
my_function()
my_function(170, 20)



# 2. Write a function to calculate S = 1+2+....n 

# a) simple way

input_n = int(input('Please insert an integer value : '))
series_ls = []
      
for i in range (1, input_n+1):
    print (i, sep = " ", end = " ")
    if (i<input_n):
        print("+",sep=" ",end=" ")             # ‘+’ operator is printed only if i
    series_ls.append(i) 
series = sum(series_ls)
print("=",series)
print()


# b) via a recursive function

def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)

input_n = int(input('Please insert an integer value : '))

if input_n < 0:
   print("Enter a positive number")
else:
   print("The sum is",recur_sum(input_n))
   

# 3. Write a function to create Fibonacci sequence(0,1,1,2,3,5....)
#    Tips : the function gets the number of term and produce the term from 0 to n
#    Note : once without recursion, another time with recursion

# Iterative Fibonacci sequence

def fib(n):
    f = []              
    a = 0                               # index 0 of sequence = 0
    b = 1                               # index 1 of seq. = 1
    if n == 0 or n == 1:
        print (n)
    else:
        f.append(a)
        f.append(b)
        while len(f) != n:              # length of f not equals to n
            temp = a + b
            f.append(temp)
            a = b
            b = temp

    print (f)
    
nterms = int(input("Please insert number of term : "))    
fib(nterms)

    

# Recursive Fibonacci sequence

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = int(input("Please insert number of term : "))

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))


# ---------------------------------------------------------------------------------------------------------------------------------

"""Assignment Lambda Function"""

# 1. Write down a function to produce this statement:
#    f(x,y,z) = 2x^2 + 2y +2z use lambda function

def lambda_f(x, y, z):
    return lambda f : f*pow(x, 2) + f * y + z

# f_doubler now is a function of a : (x=2, y=3, z=4)
f_doubler = lambda_f(2, 3, 4)       
print(f_doubler(11))                # value of f = 11


# ---------------------------------------------------------------------------------------------------------------------------------

"""Assignment Datetime Module"""

# Find out other function to format data and time of now and try to use.


from datetime import datetime
 
# Calling now() function
today = datetime.now()
 
print(f"Today's date and time is {today}")


# ---------------------------------------------------------------------------------------------------------------------------------

"""Assignment Math module"""
# find out more functions in math module and try to use them in your code

# Function 1 : Getting Pi value
import math
math.pi
print(f"Pi value is {math.pi}\n ",)

# Function 2 : e value
import math
math.e
print(f"e value is {math.e}\n ",)

# Function 3 : Math radians and degrees
import math
rads = math.radians(30)
print(f"Radian value for 30 is {rads:.4f}\n ",)

deg = math.degrees(math.pi/6)
print(f"Degree value for pi/6 is {deg:.4f}\n ",)

# Function 4 : Sin, Cos, Tan Calculation
import math
x = 0.5235987755982988                  # angle of 30 degrees (0.5235987755982988 radians):
ms = math.sin(x)
mc = math.cos(x)
mt = math.tan(x)
print(f"sin(x) : {ms:.2f}\ncos(x) : {mc:.2f}\ntan(x) : {mt:.2f}")

# Function 5 : log
import math
f_input = float(input("Please enter a number to calculate log : \n"))
log = math.log(f_input)
print(f"Log : {log:.4f}")

# specified base of log
import math
log10 = math.log10(f_input)
print(f"Log10: {log10:.4f}\n")

# Function 6 : Exponent
import math
expo = math.exp(10)
print(f"exponent for 10 : {expo:.4f}")

# exponent operation
import math
expo_op = math.e**10
print(f"exponent power of 10 : {expo_op:.4f}")


# Function 6 : Power
import math
math.pow(2, 4)              
print(f"2**4 : {math.pow(2, 4)}")

# Function 7 : Ceil and Floor
# ceil() function approximates the given number to the smallest integer, greater than or equal to the given floating point number
# floor() function returns the largest integer less than or equal to the given number.

import math
c = math.ceil(4.5867)
f = math.floor(4.5678)
print(f"ceil  : {c}\nfloor : {f}")

# ---------------------------------------------------------------------------------------------------------------------------------

"""Assignment Own Module"""

# 1. Create a module with your name and import functions of the previous assignment to it
# try to use them in another file


from kishapackage import calculation_0

m = calculation_0.add(2, 3)
print("2 + 3 = {m}")

n = calculation_0.multiply(10, 3)
print("10 x 3 = {n}")

p = calculation_0.expo(17, 2)
print("17^2 = {p}")


# ---------------------------------------------------------------------------------------------------------------------------------

"""Assignment Package"""

# check if camelcase package is installed
# if not, install
# then use it to change string into camel case


# camelcase : capitalize each word 
import camelcase

c = camelcase.CamelCase()
    
txt = "guten tag! ich bin kisha. wie gehts"

# write text with camelcase
print(c.hump(txt))

# for initialization and packaging
print(dir(camelcase))


# ---------------------------------------------------------------------------------------------------------------------------------

"""Assignment Module & Package"""

# 1. create a module with your name
# 2. write a function that counts from 1 to n in the module
# 3. create a package which contains this module
# 4. use the package in a program

import kisha

kisha.count(6)

from kishapackage import kisha


# ---------------------------------------------------------------------------------------------------------------------------------

""" Assignment : File Handling"""

# 1. create file with your name and .txt extension

import os

f = open ("studentFile.txt", "w")
f.write("No\tStudent name\tGrade")
f.writelines(["\n1\tInamul\t\t100","\n2\tKisha\t\t100"])
f.close()  


# 2. the file lookslike:
    
    # No Student name  grade
    # 1  inamul        100
    # 2  kisha         100

# 3. read file line by line and print it
f1 = open("studentFile.txt", "r")
for l in f1:
    print(l)
    

# 4. close file
f1.close()


# ---------------------------------------------------------------------------------------------------------------------------------

""" Assignment : File Handling"""

# create a package with these modules:
    # 1. A module (FileHandling) that has function for creating, writing and reading the file.
    #    The file name will be sent by an arguments
    # 2. A module (destroy) : get the file name and delete the files
    # 3. use the package and all the modules in your code

from kishapackage import FileHandling

# f_name = "traineeFile.txt"
f1 = open("traineeFile.txt", "r")
for l in f1:
    print(l)
f1.close()


from kishapackage import destroy

f_name = "traineeFile.txt"
if destroy(f_name):
    print("File Removed!")






