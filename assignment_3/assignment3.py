"""
Created on Wed Oct 20 20:25:01 2021

@author: User

Assignment 3 : Data Structure

"""

#---------------------------------------------------------------------------------------------------------------------------------
# PART A : SET OPERATIONS
#---------------------------------------------------------------------------------------------------------------------------------

#1. define a set for all courses in your major (4)
courses = {'Informatics', 'Medical Electronics', 'Instrumentation', 'Biochemistry'}
print("\nThe major courses are : ", *courses, sep = "\n ")                # sep = separated by

#2. define a set of courses you passed
c_passed = {'Biotelemetry', 'Dynamics'}
print("\nThe courses passed are : ", *c_passed, sep = "\n ")                # sep = separated by

#3. find out which courses you have not passed yet
c_failed = {'Calculus', 'Electromagnetic'}
print("\nThe courses failed are : ", *c_failed, sep = "\n ")                # sep = separated by

#4. define a set of all courses you take (whatever you have now, passed, failed)
c_now = {'Biomaterial'}
all_c = courses.union(courses, c_passed, c_failed, c_now)
print('\nAll courses taken are : ', *all_c, sep = "\n ")

#5. find out the courses you take previously and not passed yet
t_und_f = all_c.difference(courses, c_passed)
print("\nThe taken courses & not passed yet are : ", *t_und_f, sep = "\n ")  # sep = separated by


#---------------------------------------------------------------------------------------------------------------------------------
# PART B : DICTIONARY
#---------------------------------------------------------------------------------------------------------------------------------

# 1. Define a malay/english dict for numbers 0 to 5

dictionary = {'sifar' : 'zero','satu' : 'one', 'dua' : 'two', 'tiga' : 'three', 'empat' : 'four', 'lima' : 'five'}
print("\nNumber in Malay are : \n", dictionary)


# 2. Take out the Malay words you defined in your dictionary

malay = dictionary.keys()
print(f"\n{malay}")

# 3. Define a set of numbers from zero to ten

set_numbers = {'zero' : 'sifar','one' : 'satu', 'two' : 'dua', 'three' : 'tiga', 'four' : 'empat', 'five' : 'lima', 'six' : '', 'seven' :'', 'eight' : '', 'nine' : '', 'ten' : ''}


# 4. Find out which numbers are not defined in your dictionary

if set_numbers.get(True):
    print('True')
else :
    print('\nUndefined keys detected !')


# 5. Ask from user input to add them to the dictionary

key_dict = list(set_numbers.keys())
value_def = list(set_numbers.values())

for i in range (len(value_def)):
    if value_def[i]=='':
        add_def = input(f"Define {key_dict[i]} in malay : ")
        set_numbers[key_dict[i]] = add_def

print("\nThe malay/english numbers dictionary are:\n", set_numbers)


#---------------------------------------------------------------------------------------------------------------------------------
# PART C : LOOPS
#---------------------------------------------------------------------------------------------------------------------------------

#1. get an integer value from user (n). Calculate this series: S = 1+2+...+n

input_n = int(input('Please insert an integer value : '))


#2. print the S result
#3. example:  n=4, S=10 (1+2+3+4=10) 
#             n=0, S=0 
#             n=1, S=1

series_ls = []

#4. (a) for loop
# for loop enables i to range between 1 and n (as n+1 is not included)
# for each iteration, the value of i is printed
      
for i in range (1, input_n+1):
    print (i, sep = " ", end = " ")
    
    if (i<input_n):
        print("+",sep=" ",end=" ")             # ‘+’ operator is printed only if i

    series_ls.append(i) 
print("=",sum(series_ls))
print()

series_ls.clear()


#4. (b) while loop

while input_n >= 0 :
    series_ls.append(input_n)
    series = sum (series_ls)
    input_n -=1                                 # equals to subtraction
print("Series (while loop): ", series)   
print("Series (for loop): ", series)  

#---------------------------------------------------------------------------------------------------------------------------------
