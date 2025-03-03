'''
Lesson 2.3
by Adrienne Dycoco
Date: 25/02/2025
Version 1
'''

#print(x) will print 4.0
#x = float(4)
#print(x)

#If the user types 3 into the input, the height variable will equal 3.0.  If the user types 1.7 that will be stored. Either can be used in the calculation below.
#height = float(input("How tall are you in metres?"))
#print("Half your height is {} metres".format(height / 2))


#Make a small app to share our pocket money with everyone in class

#Ask pocket money
pocket_money = int(input("How much pocket money do you have?: "))

#Ask the number of people
number_people = int(input("How many people are there?: "))

#Calculate the shared amount as dollars
shared_amount = pocket_money / number_people

#Display the shared amount
print("Each person will get: ${}" .format(shared_amount))
