'''
Task 2
by Adrienne Dycoco
Date: 17/02/2025
Version 1
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
