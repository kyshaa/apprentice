# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 23:03:18 2021

@author: User
"""

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


"""Assignment 1 : Object-oriented Programming"""

# To define a class for students
# The class contains these properties: 1. name 2. matricNo 3. set of course taken
# The class also contains some methods:
    # 1. __init__ method takes the initial properties from the user to be filled
    # 2. print method to print all the information of the student in a good format
# After class definition, make 3 objects from the class and fill them with your information and two of your friend 
# and print their properties using the print function of the clas


class stdnts:
    def __init__(self, n, m, c):
        self.name = n                   # self = is a pointer to the instance that call the function/ parameter pointed to the object in class
        self.matric = m
        self.course = c
        
    def printing(self):
        print(" ", self.name, " | Matric No.: ", self.matric, " | Course: ", self.course, "\n")

       
print("\nClass of 2021\n")

student_1 = stdnts("1. Mesut Ozil", "A21MB0001", "Fluid Engineering")
student_1.printing()

student_2 = stdnts("2. Paul Pogba", "A21MB0123", "Dynamics")
student_2.printing()

student_3 = stdnts("3. Luke Shaw", "A21MB0562", "Calculus")
student_3.printing()

student_4 = stdnts("4. Marcus Rashford", "A21MB0752", "Physics")
student_4.printing()

student_5 = stdnts("5. Mason Mount", "A21MB0633", "Biosignals")
student_5.printing()


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


"""Assignment 2 : Inheritance"""

##### This class must be inherited from the student class
# 1 - Create a model for (BSCstudent) bachelor student (it inherit properties of student class) but it has extra properties 
#     like major, average, set of pass and failed subjects that keeps the name of courses and also the score
#     Methods : AVG calculate the average from the scores of objects taken.

# 2 - RequiredCourses(get the set of courses in the major): The method shows which courses of the major is not taken yet by the students.
# 3 - printInfo() : print all the info of the student.

class Students:
    def __init__(self):
        self.name = input("Name : ")
        self.matric = input ("Matric No.: ")
        self.course = list(i for i in input("Insert subjects: ").strip().split())
        
    def display(self):
        print("\n----------Student Details----------\n")
        print("Name : ", self.name)
        print("Matric No. : ", self.matric)
        print("Subjects : {}".format(', '.join(self.course)))
        
class BSCstudent(Students):
    def __init__(self):
        super().__init__()
        self.PassedFailed()
        self.RequiredCourses()
        self.AVG()
        
    def PassedFailed(self):
        subject_dict = dict.fromkeys(self.course, None)
        subject_score = [float(input(f'{i} score: ')) for i in subject_dict]
        
        self.passed = {i:j for i, j in zip(subject_dict,subject_score) if j>=45}
        self.failed = {i:j for i, j in zip(subject_dict,subject_score) if j<45}
        
    def AVG(self):
        self.score_sum = sum([float(i) for i in self.passed.values()] + [float(i) for i in self.failed.values()])
        self.score_avg = self.score_sum/(len(self.passed.values()) + len(self.failed.values()))
        
    def RequiredCourses(self):
        self.major = input("Major course : ")
        self.subjects = [i for i in input('Insert subjects: ').strip().split()]
    
    def printInfo(self):
        super().display()
        print("\n----------Bachelor Information----------\n")
        print("Major course : ", self.major)
       
        print("Passed subjects : ")
        for x in self.passed:
            print(f'{x}: {self.passed[x]}')

        print("Failed subjects : ")
        for x in self.failed:
            print(f'{x}: {self.failed[x]}')
            
        print(f"Average score : {self.score_avg:.2f}")
        print("Major upcoming subjects : ", ", ".join(self.subjects))
        
S1 = BSCstudent()
S1.printInfo()












