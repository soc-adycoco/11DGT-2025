"""
Times Table (and check input string length)
by Adrienne Dycoco
Date: 3/04/2025
Version 1
"""

#Example: define function to check input string length
def check_length(str, msg):
  while True:
    if len(str) < 1 or len(str) > 25:
      print("Error - length needs to be 1-25 characters. Try again!")
      str = input(msg)
    else:
      print("You entered: ", str)
      return str
      break
    
msg = "What's your name?"
#Get user input
user_name = input(msg)
#Call function to validate string
user_name = check_length(user_name, msg)



#################
#Setup functions
def timestable(table):
  for x in range (, 13):
    print(x, "x", table, "=", x * table)

################
#Setup variables
table = 0

################
#Main
table = int(input("Please enter a times table: "))

timestable(table)
################
