# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 10:09:55 2021

@author: User
"""

# Data Structure 1 : List []
fruits = ["banana", "cherry", "plum"]
print(fruits)
print(type(fruits))
print(fruits[1])

# negative indexing
print(fruits[-1])
print(fruits[-2])
print(fruits[-3])

# changeable
fruits.append("apple")
print(fruits)

fruits.remove("banana")
print(fruits)

fruits.insert(1, "Apple")
print(fruits)

fruits.clear()
print(fruits)

print(fruits.index("plum"))
print(fruits)

print(len(fruits))

fruits = ["banana", "cherry", "plum", "cherry", "apple", "cherry"] 
print("No of cherry occurence: ", fruits.count("cherry"))
print("No of apple occurenece: ", fruits.count("apple"))

fruits.sort()
print(fruits)


# empty list
L = []


# ------------------------------------------------------------------------------------------------------------------------


# Exercise List

# 1. Define a list of your favourite food
food = ["chicken", "ramyeon", "carbonara", "carbonara", "rose tea"]

# 2. Print the list
print(food)

# 3. print the list from the last item to the first
print(food[-1])
print(food[-2])
print(food[-3])
print(food[-4])
print(food[-5])

# 4. Add "Rice" to your list
food.append( "rice")                    
print(food)

# 5. What is the index of "Rice"
print(food.index("rice"))

# 6. Sort your list
food.sort()                                     # order depends on ASCII code
print(food)

# 7. Give the number of occurence of each food in the list
print("No of carbonara occurence: ", food.count("carbonara"))
print("No of rice occurence: ", food.count("rice"))
print("No of rose tea occurence: ", food.count("rose tea"))
print("No of chicken occurenece: ", food.count("chicken"))


# 8. Clear the list
food.clear()
print(food)


# ------------------------------------------------------------------------------------------------------------------------

# Data Structure 2 : Tuple ()

# tuple : not changeable after being defined
# means we cannot add, insert, remove but duplication is allowed

# Defining tuple use parentheses {}
cars = ("benz", "proton", "BMW", "Tesla")
print(type(cars))
print(cars)

# tuple is indexable = boleh baca index
print(cars[2])       # positive indexing
print(cars[-2])      #  negative indexing

print(cars.index("proton"))


# How to change tuple? 
# Solution: Change tuple to list using Typecasting, x = str(2), edit, then change back to tuple

cars = ("benz", "proton", "BMW", "Tesla")
lcars = list(cars)
print(type(lcars), lcars)

lcars.append("Kia")
lcars.insert(2, "Kancil")
lcars.remove("benz")
print(lcars)


# Then change back the list to tuple

cars = tuple(lcars)
print(cars)

# empty tupple
T = ("benz",)                       # put comma at the end, so that it produced a tuple and not statement of a string
print(type(T))

new_tuple = tuple(("a","b","c"))    # put double parentheses/bracket, so that it produced a tuple and not an error
print(new_tuple)


# ------------------------------------------------------------------------------------------------------------------------

# Exercise Tuple

# 1. Get the name of user siblings from input

lst = [ ] 
n = int(input("Enter number of siblings : ")) 
  
for i in range(0, n):           # range(n)
    ele = input('Name: ')
    lst.append(ele) 
    
print(lst)
     
# flattened_list = flatten(lst)  ---- will not be needed if at the for loop, part ele, you remove square bracket


# 2. Put in tuple

siblings = tuple(lst)

# 3. Print the tuple

print(siblings)


# ------------------------------------------------------------------------------------------------------------------------


# Data Structure 3 : Set {} 

set = {"a", "b", "c", "d"}          # set is unordered, so it has none index
print(set)

# since it is unindexable, so we can access by the item in the list bcuz item are referred by their value
# if have occurence of same value, duplication will be remove in set

test_set = {"a", "b", "c", "d", "a"} 
print(test_set)


# set's ability to change the item : changeable same like list

set.add("f")
print(set)

set.add("a")                        # set is same as before because duplication is not allowed in set
print(set)

set.remove("b")
print(set)

print(set.pop())                          # pop remove and return element
print(set.pop(), set)                     # everytime pop randomly

# discard will remove if element is in set, and wont do anything if its not in the set
set.discard("a")
set.discard("z")

# s.pop() remove the top element of the set
# if pop emty set, it will return an error
set.pop()
print(s)
set.pop()
print(s)

# remove all  item from set
set.clear()


# operation in set
# if remove non existing element from set it will return an error
# s.remove("z")

s1 = {'a', 'b','c','d'}
s2 = {'a','b'}

# s2.union(s1)
# s2.intersection(s1)
s1.difference(s2)

s2.discard('d')
s2.difference(s1)

# check if a set is a superset/subset of another set
s2.issubset(s1)
s1.issuperset(s2)


# ------------------------------------------------------------------------------------------------------------------------

# Tips

x = [1,2,3]
# when we use list = list1 , the y value will also change when we change values in x.
# its not an assignment.

y = x 
print("x:",x)
print("y",y)
x.append(4)
print("x:",x)
print("y",y)

# For data structure, we use list.copy() for assigning it to another list
x = [1,2,3]
y = x.copy() 
print("x:",x)
print("y",y)
x.append(4)
print("x:",x)
print("y",y)

# ------------------------------------------------------------------------------------------------------------------------

#DICTIONARY

# Defining dicitionary
# d = {key : value}

# no duplicate key, if same key used, the later value will replace the earlier value.
cars = {"brand" : "benz", "speed" : 200, "color" : "black"}
print(cars)
# if duplicate key are made the first value are replaced by the new value
cars = {"brand" : "benz","brand" : "ferrari", "speed" : 200, "color" : "black"}
print(cars)

print(type(cars))

# accessing element is by using key
print(cars["brand"])
print(cars["speed"])

# get dictionary keys
k= cars.keys()
print(f"keys of dictionary : {k}")
print(type(k))

# get dictionary values
v = cars.values()
print(f"values of dictionary : {v}")
print(type(v))

# print key pair tuple
i = cars.items()
print(i)

# change a value 
cars["brand"] = "tesla"
print(cars)  

# ading new key value pair to dictionary
cars["model"] = "model x"
print(cars)



# ------------------------------------------------------------------------------------------------------------------------

# Control Structure : Conditions and Loops


# if statement

x = 4
y = 3
if x<y:
    print(x," is lesser than ",y)
elif x==y:
    print(x," is equal to ", y)
else:
    print(x," is bigger than ",y)

print("this prints after if else statement ends")


# value comparison returns True or False

x<y # x is smaller than y
x<=y # x is smaller or equal to y
x>y # x is bigger than y
x>=y # x is bigger or equal than y
x==y # x is equal to y
x!=y # x is not equal y


# ------------------------------------------------------------------------------------------------------------------------

# Control Structure : While Loops

# this loop will print 1 to 6 once.
i =1
while i <=6:
    print(i)
    i +=1

# this loop will print 1 infinitely because the stop condition cant be met 
# i =1
# while i <=6:
#     print(i)


i=0
while i < 6:
    i = i+1
    if i == 3:
        continue
    else:
        print(i)


i=0
while i < 6:
    i = i+1
    if i == 3:
        break
    else:
        print(i)


# ------------------------------------------------------------------------------------------------------------------------

# Control Structure : For Loops

l = {"a","b","c"}
for x in l:
    print(x)

print("\n")
d = {"a":1,"b":2,"c":3}
for x in d:
    # print key and value
    print(x,d[x])

print("\n")

# range(start,stop,step)
# range(stop)
# range(start,stop)
for i in range(7):
    print(i)

print("\n")
for i in range(2,7):
    print(i)

print("\n")
for i in range(2,7,2):
    print(i)