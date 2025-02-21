'''
Task 2
by Adrienne Dycoco
Date: 21/02/2025
Version 2 - IF Conditionals
'''

# Formula
# (0°C × 9/5) + 32 = 32°F
# (0°C × 1.8) + 32 = 32°F
# (10°C × 1.8) + 32 = 18 + 32 
# 10°C = 50°F

# Welcome the user to a temperature conversion app
print("Welcome to a temperature conversion app!")

# Ask the user to enter the temperature in °C
temp_in_C = int(input('Please enter the temperature in °C:'))

# Calculate temp in °F
temp_in_F = temp_in_C*9/5 + 32

# Display the answer with both values, e.g. 10°C = 50°F
print(temp_in_C, "°C =", temp_in_F, "°F")


# Add IF / else if / ELSE conditional statements to evaluate the
# temperature, e.g. That's cold, cool, comfortable or hot.
# add if statements to check temp_in_C
# if less than 5°C - that's cold
if temp_in_C <= 5:
  print("Brr, that's cold!")

# else if between 6 - 17°C - that's cool
elif temp_in_C <= 17:
  print("Ooo, that's cool!")

# else if between 18-24°C - that's comfortable
elif temp_in_C <= 24:
  print("Oh, that's comfortable!")

# else - that's hot
else:
  print("Whew, that's hot!")  
