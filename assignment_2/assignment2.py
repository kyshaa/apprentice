# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 17:03:45 2021

@author: Alkisah Mubin

Assignment 2

"""

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
1. Collect the name, year of birth and salary of a user. Then output the following:
    - "Good day {name}!, your year of birth is {year of birth} and your age in the year 2030 will be {Age}. From your salary of {salary}, the computed tax of 12.3 % is {tax} " 
"""

print()
print("Please enter your details")

name = input("Name : ")
yob = int(input("Year of birth: "))    
age = 2030 - yob
salary = int(input("Salary (RM) : "))
tax = (0.123) * salary

print(f'Good day {name}!, your year of birth is {yob} and your age in the year 2030 will be {age}. From your salary of RM {salary}, the computed tax of 12.3 % is RM {tax:.2f}')


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
2. Collect a list of names and scores and find the average of the score
"""

from nltk import flatten

lst = [ ] 
n = int(input("Enter number of people : ")) 
  
for i in range(0, n): 
    ele = [input('Name: '), int(input('Score :'))] 
    lst.append(ele) 
      
print(lst)                                                           

# list flattening to remove square bracket
flattened_list = flatten(lst)
print(flattened_list)                                               

# separate int and str datatype in flattened list
myIntList = [x for x in flattened_list if isinstance(x, int)]
print(myIntList)                                                     

myStrList = [x for x in flattened_list if isinstance(x, str)]
print(myStrList)                                                     

print("\n")
a = sum(myIntList)
b = len(myStrList)
avg_score = a / b
print(f'The average score for {b} people is {avg_score:.2f}')


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
3. Use python to write application letter for a job to Perantis, apply text wrap with line width of 50
"""

import textwrap
print()
print("Dear Perantis Iskandar")
print()

letter = '''
\tI am writing to express my interest in AI programmer position at Educity Iskandar. I have been passionate in this field since I have accomplished my final year project with a greatest motivation 
during the bachelor study at Universiti Teknologi Malaysia. I believe that Educity Iskandar will not only be the best home for me to utilize my expertise but also will give me a wing to expand the 
skills and knowledge in AI.I look forward to hearing from you. I can be reached through the email and contact number stated in the resume. 
'''

    
print()
print(textwrap.fill(letter, width=50))
print()
