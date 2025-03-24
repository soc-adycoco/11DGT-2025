"""
Animal Limbs Quiz!
by Zoe Lincoln and Adrienne Dycoco
11/03/25
Version 1
"""

# Greet user and ask if they want to play
name = input("What's your name?").title()
print("Hello, {}!".format(name))
confirm = input("Would you like to play a game? (yes/no)")
confirm = confirm.lower().strip()

# If yes - explain and proceed to gameplay
if confirm == "yes":
  print("Yay! Here's how to play:")
  print("The name of an animal will appear on your screen.")
  print("Enter a number to guess how many limbs it has.")
  print("You'll start with 100 points.")
  print("You will lose 20 points per wrong guess.")
  print("That's all. Have fun! :D")

# Starts with 100 points
  points = 100

# Ask 5 questions: chicken, cat, spider, centipede, human
# Question 1:
  answer_1 = int(input("How many limbs does a chicken have?"))
  if answer_1 == 2:
    print("Correct! :D")
  # Lose 20 points if wrong
  else:
    print("Womp womp... You lost 20 points. Better luck next time! D:")
    points -= 20

# Question 2:
  answer_2 = int(input("How many limbs does a cat have?"))
  if answer_2 == 4:
    print("Correct! :D")
  # Lose 20 points if wrong
  else:
    print("Womp womp... You lost 20 points. Better luck next time! D:")
    points -= 20
    
# Question 3:
  answer_3 = int(input("How many limbs does a spider have?"))
  if answer_3 == 8:
    print("Correct! :D")
  # Lose 20 points if wrong
  else:
    print("Womp womp... You lost 20 points. Better luck next time! D:")
    points -= 20
    
# Question 4:
  answer_4 = int(input("About how many limbs does a centipede have?"))
  if answer_4 == 70:
    print("Correct! :D")
  # Lose 20 points if wrong
  else:
    print("Womp womp... You lost 20 points. Better luck next time! D:")
    points -= 20
    
# Question 5:
  answer_5 = int(input("How many limbs does a human have?"))
  if answer_5 == 4:
    print("Correct! :D")
  # Lose 20 points if wrong
  else:
    print("Womp womp... You lost 20 points. Better luck next time! D:")
    points -= 20

# Final results
  print("You made it to the end! Let's see your final score:")
  if points == 100:
    print("Points: {}".format(points))
    print("Well done! You're an animal limb master! :DDD")
  elif points == 80:
    print("Points: {}".format(points))
    print("Pretty good! Almost got it C:")
  elif points == 60:
    print("Points: {}".format(points))
    print("Not bad - could use a bit of studying! :)")
  elif points == 40:
    print("Points: {}".format(points))
    print("Better than nothing! :>")
  elif points == 20:
    print("Points: {}".format(points))
    print("Hey, at least you got one! :]")
  elif points == 0:
    print("Points: {}".format(points))
    print("Yikes... need a little help, buddy. :<")

# If user doesn't wish to play - farewell the player :C
else:
  print("Aww, that's a shame. Bye then! :J")
