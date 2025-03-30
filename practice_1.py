"""
Python Quiz Practice 1
by Adrienne Dycoco
Date: 20/03/2025
Version 1
"""

grade = int(input("Please enter the score you got on a test: "))
print("You entered: ", grade)

#If grade is greater than or equal to 90:
#   Print “A”
if grade >= 90:
  print("A")

#Else if grade is greater than or equal to 80:
#   Print “B”
elif grade >= 80:
  print("B")

#Else if grade is greater than or equal to 70:
#   Print “C”
elif grade >= 70:
  print("C")

#Else if grade is greater than or equal to 60:
#   Print “D”
elif grade >= 60:
  print("D")

#Else if grade is greater than or equal to 50:
#   Print “F”
elif grade >= 50:
  print("F")

else:
  print("Enter a valid number!")
