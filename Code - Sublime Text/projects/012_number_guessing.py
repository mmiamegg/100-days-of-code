# import random

# def number_guessing_game():
#     random_number = random.randint(1, 100)

#     print("Welcome to the Number Guessing Game!")
#     print("I'm thinking of a number beteween 1 and 100.")
#     difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

#     if difficulty_level == 'easy':
#         attempts = 10
#     else:
#         attempts = 5

#     print(f"You have {attempts} attempts remaining to guess the number.")

#     guessed_correctly = False
#     while attempts > 0 and not guessed_correctly:
#         guess = int(input("Make a guess: "))
#         if guess != random_number:
#             attempts -= 1
#             if attempts == 0:  
#                 print("You have run out of attempts. Game Over.")
#                 guessed_correctly = True           
#             elif guess > random_number:
#                 print("Too high.")
#             else:
#                 print("Too low.")
            
#             if attempts != 0: 
#                 print(f"You have {attempts} attempts remaining to guess the number.")
#                 print("Guess again.")
#         else:
#             print("You guessed right. You win!")
#             guessed_correctly = True
    
#     play = input("Play again? 'y' if yes, 'n' if no. ").lower()
#     if play == 'y':
#         number_guessing_game()

# number_guessing_game()


###############################################
# comment of my solution against video solution
###############################################
# - Did not use functions
# - Did not break down my code into smaller, more readable code


###############################################
# important take from solution
###############################################
# - Break down requirements to smaller chunks
# - Use comments to list down each requirement


from random import randint
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0

def check_answer(guess, answer, turns):
    """checks answer against guess. Return the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number beteween 1 and 100.")
    answer = randint(1, 100)

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")
game()