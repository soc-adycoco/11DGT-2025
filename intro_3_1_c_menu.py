'''
Intro to Python - Chapter 3.1 c
by Adrienne Dycoco
Date: 3/03/2025
Version 1
'''

menu = "What would you like:\n\
1. A complement?\n\
2. An insult?\n\
3. A proverb?\n\
4. An idiom?\n\
9. Quit\n"

answer = int(input(menu))
if answer == 1:
  print("You look lovely today!")
elif answer == 2:
  print("You smell funny.")
elif answer == 3:
  print("Two wrongs don't make a right. But three lefts do...")
elif answer == 4:
  print("The pen is mightier than the sword.")
elif answer == 9:
  print("Goodbye!!!")
