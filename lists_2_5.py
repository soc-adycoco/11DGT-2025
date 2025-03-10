'''
Intro to Python - Chapter 2.5: Lists
by Adrienne Dycoco
Date: 4/03/2025
Version 1
'''

#No comma after the last item
#Each item has an index
numbers = [3, 5, 9, 6]

#Index - 0, 1, 2 and so on
names = ["Aria", "Zoe", "Bella"]
ages = [14, 15, 15]
score = [100, 17, 7]
co2 = []
room_number = []

print(names[2], "is", ages[2])

#Print part of string
name = "Adrienne"
print(name[2])

#Append new values
new_names = ["Adrienne", "Zoe", "Sophie"]
new_ages = [15, 15, 15]
names.append(new_names)
ages.append(new_ages)

print(names)
print(ages)

