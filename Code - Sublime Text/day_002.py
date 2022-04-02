#SECTION 2-18
#num_char = len(input("What is your name?"))

#check type (type checking) of variable
#print(type(num_char))

#type casting (number in this example) to string
#new_num_char = str(num_char)

#print("Your name has " + num_char + " characters.")

#typecast int to float (can also convert string or other primitive data type to float)
#a = float(123)


# SECTION 2-19 Exercise
# 🚨 Don't change the code below 👇
#two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

#digit_one = int(two_digit_number[0])
#digit_two = int(two_digit_number[1])

#two_digit_number = digit_one + digit_two

#print(two_digit_number)


# SECTION 2-21 Challenge
# 🚨 Don't change the code below 👇
#height = input("enter your height in m: ")
#weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#height_as_float = float(height) ** 2
#weight_as_float = float(weight)

#bmi = weight_as_float / height_as_float
#bmi_as_int = int(bmi)

#print(bmi_as_int)


# SECTION 2-22
#print(round(8 / 3, 2))
#score = 0
#height = 1.8
#isWinning = True
# can be += or -= or *= or /=
#score += 1
#print(score)

#f-String
#print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")



# SECTION 2-23 Challenge
# 🚨 Don't change the code below 👇
#age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#max_age = 90
#days_a_year = 365
#weeks_a_year = 52
#months_a_year = 12

#age_as_int = int(age)

#years_left = 90 - age_as_int
#days_left = years_left * 365
#weeks_left = years_left * 52
#months_left = years_left * 12

#message = f"You have {days_left} days, {weeks_left} weeks and {months_left} months left."
#print(message)



# SECTION 2-24 Project
print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))
tip_amount = int(input("What percentage tip would you like to give? 10, 12, 0r 15? "))
people = int(input("How many people to split the bill? "))

tip_percentage = 1 + (tip_amount / 100)

bill_with_tip = bill * tip_percentage
bill_per_person = round(bill_with_tip / people, 2)
total_bill = "{:.2f}".format(bill_per_person)

message = f"Each person should pay: ${total_bill}"
print(message)