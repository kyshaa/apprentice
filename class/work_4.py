# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 09:24:48 2021

@author: User
"""


# TIPS:
    
# do not create unnecessary variable
# to save memory
# make an understandable variable

"""
Function

- is a block of code which only runs when called
- can pass data, known as parameters into function
- function can return data as result

"""

# 1.0 : to define a function, function definition

def my_function():
    print("Hello from a function")
    
# after define, can just called it to used
my_function()



# 2.1 : arguments & parameters

def my_function(fname):
    print(fname + ",Welcome")
    
# argument sent to the function
my_function("kisha")


# 2.2 : arguments & parameters

def my_function(firstName, lastName):
    print(firstName + " " + lastName)
    
# argument sent to the function
# my_function("kisha")    # Error 

# number of arguments must same with definition
my_function("song", "jihyo") 


# 2.3 : arbitary arguments

def my_function(*kids):         # kids now is a tuple
    if len(kids) == 0:
        print("There is no children in the family")
    else:
        print("The youngest child is " + kids[len(kids)-1])     # last item in tuple

my_function()
my_function("Song", "Kwang")
my_function("Song", "Kwang", "Jihyo", "Kook")
        


# 3.0 Keyword arguments : to help with unordered argument sending
#     to know which argument send to which parameter

def my_function(child3, child2, child1):
    print ("The youngest child is " + child3)

# different order will still be outputed the same because keywords is used
my_function(child1 = "Song", child2 = "Ji", child3 = "Hyo")
my_function(child3 = "Hyo", child2 = "Ji", child1 = "Song")



# 4.0 Arbitary keyword arguments, 

def my_function(**name):
    if len(name) == 0:
        print ("No arg is sent")
    else:
        for x in name.keys():
            print(x, ":", name[x])

my_function(firstName = "Song", middlename = "Ji", lastName = "Hyo")
my_function(firstName = "Song", lastName = "Hyo")
my_function()



# 5.0 Default value for Parameters : if a value does not send by args, default is used

def my_function(country = "Malaysia"):
    print("I'm from "+ country)
    
my_function("Iran")
my_function("India")
my_function()
my_function("Nigeria")



# 6.0 Pass different datatype to the function : collection types

def my_function(food):
    for x in food:
        print(x)
        
fruits = ["apple", "banana", "cherry"]

my_function(fruits)


# 6.1 Changing to parameter with list type make changes to args

def my_function(food):
    food.reverse()      #change the list
    
fruits = ["apple", "banana", "cherry"]

my_function(fruits)
print(fruits)



# 7.0 Return value

def dup_function(x):
    return 5 * x

print(dup_function(3))
print(dup_function(5))
print(dup_function(9))



# 8.0 Pass Statement
def my_function():
    pass                    # function doesn't do anything and just pass sbb takde function 
    
    

# 9.0 Recursive Function

def func(n):
    if n ==1:
        return 1
    else:
        return n*func(n-1)
    
print("Factorial of 7 is:",func(7))
#4! = 1*2*3*4

 
# ---------------------------------------------------------------------------------------------------------------------------------
# Assignment

#1. Write a function to get arguments by keywords and value:
#   initialTemp = 400.0, simulationTime = 35
#   (just print them in the function, try to call function with different number of args)

def my_function(initialTemp = 400.0, simulationTime = 35):
    print (f"The initial temperature is {initialTemp} °C and the simulation time is { simulationTime} s")

# different order will still be outputed the same because keywords is used
my_function()
my_function(170, 20)


# ---------------------------------------------------------------------------------------------------------------------------------

# Assignment

# 2. Write a function to calculate S = 1+s+....n 
#     a) simple way
#     b) via a recursive function

# 3. Write a function tocreate Fibonacci sequence(0,1,1,2,3,5....)
#    Tip : the function gets the number of term and produce the term bla bla bla
#    Note : once without recursion, another time with recursion


# ---------------------------------------------------------------------------------------------------------------------------------

"""
Lambda Function
- small anonymous function
- can take any number of args, but can only have one expression
- syntax : lambda args : expression
"""

## [1]
x = lambda a:a+10
print(x(5))

## [2] More arguments
x = lambda a, b, c : a + b + c
print(x(5,6,2))

## [3] use lambda in functions
def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)       # mydoubler now is a function of a : 2*a
print(mydoubler(11))
mytripler = myfunc(3)       # mytripler = 3a
print(mytripler(11))

# ---------------------------------------------------------------------------------------------------------------------------------

# Assignment Lambda Function

# Write down a function to produce this statement:
#    f(x,y,z) = 2x^2 + 2y +2z use lambda function

# ---------------------------------------------------------------------------------------------------------------------------------

# 1. Modules a file containing a set of function you want to include in your application

import myFirstModule  # save file as myFirstModule
# define function in a module

# def greeting(name):
#     print("Hello, "+ name)

name = input("What is your name?")
myFirstModule.greeting(name)

myFirstModule.greeting("Mr. Ali")

myFirstModule.goodbye(name)



# 2. using variables of a module

print(myFirstModule.person1["age"])


# rename amodule for easier coding
import myFirstModule as mx

a = mx.person1["age"]
print(a)
mx.greeting("Ms. Nura")


# 3. dir function - to find the existing functions in a module
print(dir(myFirstModule))

# 4. Import chosen part from a module

from myFirstModule import person1

print(person1["age"])

from  myFirstModule import greeting
greeting("song")


"""Note: when importing using from keyword, do not use
the module name when referring to elements in module.
ex: person1("age"), not myfirstmodule.person1("age")"""


# 5. Built-in mpdule

import datetime
x = datetime.datetime.now()
print(x)


# ---------------------------------------------------------------------------------------------------------------------------------

# Assignment Datetime module

# find out other function to format data and time of now and try to use.


# ---------------------------------------------------------------------------------------------------------------------------------


import math
x = math.sqrt(64)
print(x)

# ---------------------------------------------------------------------------------------------------------------------------------

# Assignment Math module
# find out more functions in math module and try to use them in your code


# ---------------------------------------------------------------------------------------------------------------------------------

# Assignment Own Module

# 1. Create a module with your name and import functions of the previous assignment to it
# try to use them in another file

# ---------------------------------------------------------------------------------------------------------------------------------


"""
Package
- is a folder containing one/ more module files
- PIP Python Package Installer:
    > check PIP version:
    > in CMD: C\Users.....\ Scripts>pip install camelcase
- install package by PIP:
    > pip install camelcase
- use a package 
- uninstall package
    > 
"""
# camelcase : capitalize each word 

import camelcase

c = camelcase.CamelCase()
    
txt = "hello world"

# write text with camelcase
print(c.hump(txt))

# for initialization and packaging
print(dir(camelcase))


# define package


# ---------------------------------------------------------------------------------------------------------------------------------

"""
File Handling

- open  a file:
- the mode


"""
import os

# f is file handler

f = open ("myFirstFile.txt", "w")
f.write("Hello, this is my first line")
f.writelines(["\nsecond","\nthird"])
f.close()  
 
f1 = open("myFirstFile.txt", "r")
print(f1.read(5))    # baca sampai character kelima je, yg lain truncated
print(f1.read(5))

print(f1.readline())


for 1 in f1:
    print(1)
    
f.close()


# Delete files

import os
os.remove("myFirstFile.txt")


# check existence 
import os
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("not exists")
















