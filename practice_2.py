"""
Python Quiz Practice 2
by Adrienne Dycoco
Date: 21/03/2025
Version 1
"""

#Setup varibles: number 1 and number 2
num_1 = 0
num_2 = 0

#Store 2 entered numbers as variables
num_1 = int(input("Please enter a number from 1-100: "))
num_2 = int(input("Please enter another number from 1-100: "))

#Give feedback
print("You entered the numbers {} and {}".format(num_1, num_2))

#Calculate which is bigger or if they're equal
#Display result to the user
if num_1 < 1 or num_1 > 100:
  print("One or more of your numbers aren't between 1-100!")
  
elif num_2 < 1 or num_2 > 100:
  print("One or more of your numbers aren't between 1-100!")

elif num_1 > num_2:
  print("Your first number {} is larger than your second number {}!".format(num_1, num_2))
  
elif num_1 < num_2:
  print("Your second number {} is larger than your first number {}!".format(num_2, num_1))
  
elif num_1 == num_2:
  print("Your numbers {} and {} are equal!".format(num_1, num_2))
  
else:
  print("Please enter a valid number!")
