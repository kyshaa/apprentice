# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 15:44:20 2021

@author: User

"""

"""
Object-Oriented Programming (OOP)
- Objects : name
- Class : human
- Methods : run, kick, jump
- Attributes : height, weight, hobbies
"""


## [1] class definition (create a model)

class clsName:
    x = 0
    
# define an instance (object) from class
obName = clsName()

# pointing to the memory
print(obName) #this is a reference (memory address) to the object

# access to properties of an object
print ("x property of obname object is: ", obName.x)
obName.x += 1
print ("x property of obname object is: ", obName.x)

# example 2 
ob2 = clsName()
print ("x property of ob2 object is: ", ob2.x)



## [2] __init__ method : to initialize an object of the class
# because most classes are define by a complicated data structure
# definition of a class = don't do anything bcuz classes just a model

class Person:
    def __init__(self, n, a):          # name , age are Properties in a class
        self.name = n                   # self = is a pointer to the instance that call the function/ parameter pointed to the object in class
        self.age = a

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# if a new instance is added, the value is updated
p1.name = "Billy"
print(p1.name)

p2 = Person("Ali", 20)
print(p2.name, " ", p2.age)



## [3] define a method of objects:

class Person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet (self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.greet()      # no need to set parameter in the bracket sbb pointer of self has pointed to the instances of the class


## [4] Name of self-parameter not always "self"

class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age
        
    def myfunc(abc):
        print("Hello my name is " + abc.name)
        
p1 = Person("John", 36)
p1.myfunc()


# modify object properties
p1.age = 40

# delete object
del p1.age
del p1
  

# use "pass" to use the empty class
class students:
    pass

obStd = students()



# inheritance

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):
        print(self.firstname, self.lastname)
        
# use the Person class to create an object and then execute the printname method

x = Person("John", "Doe")
x.printname()

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self,fname,lname)
        
y = Student("Mike", "Olsen")

# printname inherit function from its parents that is "Person", thats y boleh pakai even different class
y.printname()

y.firstname = "Tobias"
y.printname()



class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):
        print(self.firstname, self.lastname)
        
# use the Person class to create an object and then execute the printname method

x = Person("John", "Doe")
x.printname()

class Student(Person):
    def __init__(self, fname, lname, gradyear):
        super().__init__(fname,lname)
        self.graduationyear = gradyear
    
    def printInfo(self):
        super().printname()
        print(self.graduationyear)
        
x = Student("Mike", "Olsen", 2019)
x.printInfo()








































