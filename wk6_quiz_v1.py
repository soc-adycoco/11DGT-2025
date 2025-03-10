'''
Week 6 Quiz
by Adrienne Dycoco
Date: 6/03/2025
Version 1
'''
# Setup variables
msg = "What is the word for (please type in romaji!): "
score = 0

# Setup lists - index: 0, 1, 2
print()
questions = ["one", "two", "three"]
answers = ["ichi", "ni", "san"]

print("""Konnichiwa! \nWelcome to the Japanese quiz!""")

# Ask Q's
i = 0
while i < len(questions):
  user_answer = input(msg, questions[i])
  i += 1

# Check is ans == answer[1]

# Calc score
