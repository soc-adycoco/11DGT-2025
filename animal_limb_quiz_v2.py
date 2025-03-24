"""
Animal Limbs Quiz!
by Zoe Lincoln and Adrienne Dycoco
18/03/25
Version 2 - Multichoice
"""

questions = ("How many limbs does a chicken have?",
"How many limbs does a cat have?", 
"How many limbs does a spider have?",
"How many limbs does a centipede have?",
"How many limbs does a human have?")

options = (("A. 1", "B. 2", "C. 4", "D. 6"),
("A. 8", "B. 10", "C. 2", "D. 4"),
("A. 7", "B. 9", "C. 11", "D. 8"),
("A. 25", "B. 30", "C. 70", "D. 85"),
("A. 4", "B. 17", "C. 35", "D. 2"))

answers = ("B", "D", "D", "C", "A",)
guesses = []
score = 0
question_num = 0

for question in questions:
  print("~~~~~~~~~~~~~~~~~~")
  print(question)
  for option in options[question_num]:
    print(option)
    
  question_num += 1
  

  guess = input("Enter (A, B, C, or D): ").upper()
  guesses.append(guess)
  if guess == answers[question_num]:
    score += 1
    print("Correct! :D")
  else:
    print("Incorrect! :<")
    print({answers[question_num]} " is the correct answer.")
  question_num += 1
