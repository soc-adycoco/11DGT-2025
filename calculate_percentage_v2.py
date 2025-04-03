"""
Calculate Percentage - V2
by Adrienne Dycoco
Date: 1/04/2025
Version 2
"""

#######################
#Setup functions

def calc_percentage(a, b):
  result = a / b * 100
  return result
  
#######################
#Setup variables
percentage = 0

#Put this in a loop
asking = False
while asking == False:
  try:
    score = int(input("Please enter your score: "))
    number_questions = int(input("Please enter the number of questions: "))
    
    percentage = calc_percentage(score, number_questions)
    asking = True
    print("You got {}%!".format(percentage))
  
  except ValueError:
    print("Invalid input - please enter a number!")
  
  except ZeroDivisionError:
    print("Invalid input - you can't divide by zero!")
  
