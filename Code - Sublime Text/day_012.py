# Section 12-114

# # scope
# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")



# #local scope

# def drink_potion():
#    potion_strength = 2
#    print(potion_strength)

# drink_potion()
# print(potion_strength)

###########################################
###########################################
# # global scope ENCOUNTERED ERROR SCENARIO
# player_health = 10

# def drink_potion():
#    potion_strength = 2
#    for test in range(0, potion_strength):
#        player_health += potion_strength
   
# drink_potion()
# print(player_health)
###########################################
###########################################

# global scope
# player_health = 10

# def drink_potion():
#    potion_strength = 2
#    print(player_health)
   
# drink_potion()
# print(player_health)


# # NESTED FUNCTION
# player_health = 10

# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(player_health)
    
#     drink_potion()

# print(player_health)


# Section 12-115
#######################################
# python does not have block scope
# making a variable within an if/while
# statement still makes it available
# globally
#
# however, if the if/while statement
# is inside a function, it becomes
# only available within that function
#######################################



# # Section 12-116
# # modify global scope
# enemies = 1

# def increase_enemies():
#     global enemies
#     enemies += 1
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")


# Section 12-117
# Global Constants
# No need to modify and identify by naming variable
# With all upper case letters

# PI = 3.14159
# URL = "http://www.google.com"
# TWITTER_HANDLE = "@yu_angela"



# Section 12 PROJECT
import random

random_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number beteween 1 and 100.")
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty_level == 'easy':
    attempts = 10
else:
    attempts = 5

print(f"You have {attempts} attempts remaining to guess the number.")

guessed_correctly = False
while attempts > 0 and not guessed_correctly:
    guess = int(input("Make a guess: "))
    if guess != random_number:
        attempts -= 1
        if guess > random_number:
            print("Too high.")
        else:
            print("Too low.")
        print("Guess again.")
        print(f"You have {attempts} attempts remaining to guess the number.")
    else:
        print("You guessed right. You win!")
        guessed_correctly = True