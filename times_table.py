"""
Times Table
by Adrienne Dycoco
Date: 3/04/2025
Version 1
"""

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
