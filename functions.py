"""
Practice - Functions
by Adrienne Dycoco
Date: 25/03/2025
Version 1
"""
###############################

# SET UP FUNCTIONS

# Basic function from w3schools.com
def my_function():
  print("Hello from a function")
  
def number_machine(x):
  x = x * 10 / 2
  print("x = ", x)
  
def dog_years(x):
  x = x * 7
  print("The dog is ", x, "years old")

##############################
  
# SET UP variables & CONSTANTS
user_input = 0

#############################
# Call FUNCTIONS
my_function

user_input = int(input("Enter dog's age 1-28"))
# Call number machine() to user_input
number_machine(user_input)
