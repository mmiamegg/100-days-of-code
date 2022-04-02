# SECTION 3-27
#print("Welcome to the rollercoaster!")
#height = int(input("Whar is your height in cm? "))

#if height >= 120:
#    print("You can ride the rollercoaster!")
#else:
#    print("Sorry, you have to grow taller before you can ride.")


# SECTION 3-28 Challenge
# 🚨 Don't change the code below 👇
#number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#if number % 2 == 0:
    #print("This is an even number.")
#else:
    #print("This is an odd number.")

# SECTION 3-29
# print("Welcome to the rollercoaster!")
# height = int(input("Whar is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         print("Please pay 5.")
#     elif age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")


# SECTION 3-29 CHALLENGE
# 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# bmi = (weight / height ** 2)

# if bmi < 18.5:
#     print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25:
#     print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi < 30:
#     print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi < 35:
#     print(f"Your BMI is {bmi}, you are obese.")
# else:
#     print(f"Your BMI is {bmi}, you are clinically obese.")


# SECTION 3-29 Challenge
# 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")


# SECTION 3-32
# print("Welcome to the rollercoaster!")
# height = int(input("Whar is your height in cm? "))
# bill = 0

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#     elif age <= 18:
#         bill = 7
#     else:
#         bill = 12
    
#     wants_photo = input ("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#         bill += 3

#     print(f"Your final bill is {bill}.")    
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# SECTION 3-33 CHALLENGE
# 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# bill = 0

# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25

# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
    
# if extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is: ${bill}")

# SECTION 3-34
# print("Welcome to the rollercoaster!")
# height = int(input("Whar is your height in cm? "))
# bill = 0

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print("Childe tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $5.")
#     elif age >= 45 and age <= 55:
#         print("Everything is going to br ok. Have a free ride on us!")
#     else:
#         bill = 12
#         print("Adult tickets are $5.")
    
#     wants_photo = input ("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#         bill += 3

#     print(f"Your final bill is {bill}.")    
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# SECTION 3-35 CHALLENGE
# 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = (input("What is your name? \n")).lower()
# name2 = (input("What is their name? \n")).lower()
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
# t = (name1.count("t")) + (name2.count("t"))
# r = (name1.count("r")) + (name2.count("r"))
# u = (name1.count("u")) + (name2.count("u"))
# e = (name1.count("e")) + (name2.count("e"))

# true = str(t + r + u + e)

# l = (name1.count("l")) + (name2.count("l"))
# o = (name1.count("o")) + (name2.count("o"))
# v = (name1.count("v")) + (name2.count("v"))
# e = (name1.count("e")) + (name2.count("e"))

# love = str(l + o + v + e)

# love_score = int(true + love)

# if (love_score < 10) or (love_score > 90):
#     print(f"Your score is {love_score}, you go together like coke and mentos.")
# elif (love_score > 40) and (love_score < 50):
#     print(f"Your score is {love_score}, you are alright together.")
# else:
#     print(f"Your score is {love_score}.")

# SECTION 3-36 Project
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice1 = (input('You\'re at a cross road. Where do you want to go? Type "left" or "right"')).lower()
if (choice1 == "left"):
    choice2 = (input('You came to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ')).lower()

    if choice2 == "wait":
        choice3 = (input('You arrived on the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? ')).lower()
        
        if choice3 == "yellow":
            print("You win!")
        elif choice3 == "red":
            print("You got burned by a fire. Game over.")
        else:
            print("You were hit by a frying pan. Game over.")
    else:
        print("You were attacked by a trout. Game over.")
else:
    print("You fell into a hole. Game over.")