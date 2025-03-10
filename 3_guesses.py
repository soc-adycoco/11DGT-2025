'''
3 Guesses - Good Programming Habits
by Adrienne Dycoco
Date: 10/03/2025
Version 1
'''

# import time
# import random

# Greet the user
name = input("Enter your name: ")
name = name.title()
print("Hello",name)
# time.sleep(1) 
print()

# Ask the user if they want to play a game
answer = input("Do you want to play a game? (y/n) ")
answer = answer.lower()
answer = answer[0]
print()

# If yes, then setup gameplay - pick number ranges
if answer == "y":
    rand1 = random.randint(0,1000)
    rand2 = random.randint(0,1000)
    if rand1 < rand2: 
        low = rand1
        high = rand2
    else:
        low = rand2
        high = rand1
        
        # Explanatory game tutorial
    print("I have picked two random numbers between 0 and 1000")
    print("You have 3 guesses to enter a number between those two random numbers.")
    print("They can be any two random numbers for instance...")
    print("465 - 890, 1 - 290 or 994 - 999...Who knows???")
    print()
    
    # Proceed to gameplay
    # If they guess correct
    guess = 1
    winner = False
    while guess < 4 and winner == False:
        answer = int(input("Enter your guess: "))
        guess = guess + 1
        if answer >= low and answer <= high:
            print(name,"... YOU HAVE WON!!!")
            print()
            print("The random numbers were",low,"and",high)
            winner = True
            guess = 4 
            
            # If they guess wrong
        else:
            print("That is not in the range")
            print()
            
            # If the user lost
    if winner == False:
        print("You have used all your guesses and did not enter a number in range.")
        print("The random numbers were",low,"and",high)
    print()
    print("Thank you for playing, I hope I'll see you again soon.")
    
    # If the user doesn't wish to play the game
else:
    print("That is a shame,",name,"- if you change your mind you know where I am.")
    
    # Farewell to the player
print()
print("Bye")
