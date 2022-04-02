import random
# separate module
# import sample

#import from separate module
#print(sample.pi)

# SECTION 4-38
# random_integer = random.randint(1, 10)
# print(random_integer)

# random_float = 5 * random.random()
# print(random_float)


# SECTION 4-40 CHALLENGE
# random_int = random.randint(0,1)

# if random_int == 1:
#     print("Heads")
# else:
#     print("Tails")


# SECTION 4-41
# states_of_america = ["Delaware", "Pennsylvania"]

# print(states_of_america[1])

# states_of_america[1] = "Pencilvania"
# # add one to list
# states_of_america.append("Angeland")
# # add more than one like another list to the existing list
# states_of_america.extend(["Mondstadt", "Liyue"])

# print(states_of_america)

# SECTION 4-42 Challenge
# Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# num_of_names = len(names) - 1
# random_number = random.randint(0, num_of_names)

# person_who_will_pay = names[random_number]

# print(f"{person_who_will_pay} is going to buy the meal today!")

# SECTION 4-43

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]

# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen = [fruits, vegetables]

# print(dirty_dozen)


# SECTION 3-44 CHALLENGE
# 🚨 Don't change the code below 👇
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# column = int(position[0]) -1
# row = int(position[1]) -1
# map[row][column] = "x"


# 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")

# SECTION 3-45 PROJECT
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

if player_choice >= 3 or player_choice < 0:
    print("You typed an invalid number. You lose")
else:
    print(choices[player_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:\n" + choices[computer_choice])


    if player_choice == 0 and computer_choice == 2:
        print("You win")
    elif computer_choice == 0 and player_choice == 2:
        print("You win")
    elif computer_choice > player_choice:
        print("You lose")
    elif computer_choice < player_choice:
        print("You win")
    elif computer_choice == player_choice:
        print("Draw")


