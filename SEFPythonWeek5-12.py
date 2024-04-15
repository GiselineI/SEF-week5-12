
# WEEK 6
# exercise 1
# 1. create 3 favourite things about you using multiline string

favouriteThings = 'Music'\
                  ' Noodles'\
                  ' Games'

print(f"My Favourite things are {favouriteThings}")

#2. using variables in string print - student fill details. (firstname, lastname, address)

firstName = "Giseline"
lastName = 'Itil'
address = '81 notrealaddress ave.'

print(f"My full name is {firstName} {lastName} and my address is {address}")

#Excercise 2
# 1. create a list of agile software. insert the values, delete one item from the list. use slicing and display the list of sofware's

#insert the values of cheesecake
cheeseCake = ['Newyork','Strawberry','Cherry','Chocolate', 'Japanese]']
print(cheeseCake)
#deleting the fourth item in the list
del cheeseCake[3]
print(cheeseCake)
#slicing the list 
print(cheeseCake[:2])
print(cheeseCake[2:])

#Excercise 3 
#1. start with the list by printing three course's ame like comp

#input value of courses
courseNumber = ['comp 100', 'comp 120', 'comp 213']

#print each course with their own personalize message
print(f"You are enrolled {courseNumber[0]}, you will be learning about programming 101 ")
print(f"You are enrolled {courseNumber[1]}, you will be learning about Software Engineering Fundament")
print(f"You are enrolled {courseNumber[2]}, you will be learning Wen Interface Design")

#add a new course
courseNumber.append('Math 175')

print("a new course will be given to you based on your other courses")
print(f"you are now also enrolled in {courseNumber[3]}, you will be learning Functions and Number Systems")

# Week 8 

# Exercise 1 
# 1. Use the following dictionary and answer the questions

favorite_languages = {
    'jen': 'HTML',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'C#',
    }
print(favorite_languages)

# Change value C# to Python 
favorite_languages['phil'] = 'Python'
print(favorite_languages)

#Add an item
favorite_languages['Giseline'] = 'C#'
print(favorite_languages)

#remove item
favorite_languages.pop('sarah')

#list all values 
print(favorite_languages)

#Exercise 2 
#1. create a python dictionary called student. Include student name, age, subject, semester, grade and lab keys. Include the value for each key accordingly. Display keys separately and values separately in the print statement.
student = {
    'name': 'Giseline',
    'age': 19,
    'subject': 'Software Engeneering Fundeament',
    'semester': 1,
    'grade': 34,
    'lab key': 'idk what this is',
}
print(student)

#create variable tp hold dictionary 
v = student.values()
k = student.keys()

#print the keys then print the values
print(f"the keys are: {k}")
print(f"the values are: {v}")

#Week 9
#Exercise 1 
# 1. 
# Get user input


outside_temperature = int(input('ENTER THE TEMPERATURE OUTSIDE: '))
print(outside_temperature)
    
#Compare if the input is hot or cold
   
if (outside_temperature <= 98):
    print("IT IS COLD")
else:
    print("IT IS HOT") 
    

# Exericse 2
agile_value = ['Individuals and Interactions', 'Working Software', 'Customer Collaborations', 'Responding to Change']
print(agile_value)
for keys in range(len(agile_value)):
    {
        print(f"Agile value {keys+0}: {agile_value[keys]}")
    }

# Week 10 maybe 
#1. Create a function called team_collaboration() . pass two team collaboration software names as the arguments. 
def team_collaboration(software):
    {   
    
    print(f"I use {software} software for team collaboration")
    }

team_collaboration("Microsoft Team")
team_collaboration("Notion")

# Exercise 2 
# 1. Create a function called project() that store project_id globally and locally . Call the function and display both the id's . 
project_id = 369

def project():
    
    project_id = 533 
    return project_id
    

print(f"My global project id is: {project_id}")
print(f"My internal project id is: {project()}")


# WEEK 11
# Exercise 1
#1. Import the correct library and print a calendar for your project. Print October month calendar of this year 

import calendar
x =  calendar.TextCalendar(calendar.SUNDAY)
displayCalendar = x.formatmonth(2024, 5)
print(displayCalendar)

#Exercise 2 
#1. Use 5 Functions in Python Math Module  and print the results 


# import math and creating value(number), which will be used for every math function 
import math
number = 81

#find the circumference and format it with three decimal points
print(f'The circumference is: {math.pi*number*number:.3f}.')

#find the square root of the number
print(f'square root: {math.sqrt(number)}')

#find the greated common divisor of the number
print(f"Greatest Common Divisor: {math.gcd(number)}")

#display the power of the number 
print(f"Power of {number} is : {math.pow(number, 2)}")

#find the remainder of the number
print(f"Remainder of {number} and 5 is : {math.remainder(number, 5)}")

#Exercise 3
#1 . Write a command to create a new directory usign OS Library
# part 1. create a new directory

#calling os funstions and creating newdir name
import os 
newDir = 'Music folder'

# print the name of the directory
print(newDir)

# Through an if statement a new directory is created and then check if it does exsts
if not os.path.exists(newDir):
    os.mkdir(newDir)
    #directory doesnt exist 
    print(f"this directory {newDir} does not exist")
else: 
    #directory exist
    print(f" {newDir} was succesfully created and exists")

# Part 2. remove the file

os.rmdir(newDir)

if not os.path.exists(newDir):
    #directory doesnt exist 
    print(f"this directory {newDir} does not exist")
else: 
    #directory exist
    print(f" {newDir} was succesfully created and exists")



