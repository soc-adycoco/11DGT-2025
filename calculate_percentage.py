"""
Calculate Percentage
by Adrienne Dycoco
Date: 1/04/2025
Version 1
"""

def multiply(a, b):
  a = int(input("Please enter your score: "))
  b = int(input("Please enter the amount of questions: "))
  percent = a / b * 100
  print("You got {}%!".format(percent))
  
multiply(a, b)



#######################
#Setup functions

def calc_percentage(a, b):
  result = a / b * 100
  return result
  
  
#######################
#Setup variables

score = int(input("Please enter your score: "))
number_questions = int(input("Please enter the amount of questions: "))
  
percentage = calc_percentage(score, number_questions)
print("You got {}%!".format(percentage))
