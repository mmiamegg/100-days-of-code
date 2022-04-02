import random
# import hangman_art
#import hangman_words

from hangman_words import word_list
from hangman_art import stages, logo
#from hangman_art import logo


end_of_game = False
#word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

print(logo)

print(f'Pssst, the solution is {chosen_word}.')

display = []
for letter in range(word_length):
    display += "_"

# blanks = 0
# for letter in display:
#     if letter == "_":
#         blanks += 1

# while blanks > 0:
#     guess = input("Guess a letter: ").lower()

#     for position in range(word_length):

#         letter = chosen_word[position]
#         if letter == guess:
#             display[position] = letter
            
#     blanks = 0

#     for letter in display:
#         if letter == "_":
#             blanks += 1

#     print(display)
#     print(blanks)
# ==================================

# while not end_of_game and not lives == 0:
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")
    # else:{{          
    for position in range(word_length):
        letter = chosen_word[position]
          
        if letter == guess:
            display[position] = letter
      
    if guess not in chosen_word:
        # print(f"you guessed {letter}, that's not in the word. You lose a life.")
        print(f"you guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
    # }}
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win")    
    
    # if lives == 0:
    #     print("You lose")

    print(stages[lives])




# ==================================
# OLD CODE
# import random

# # commented items are my solutions. uncommented items are course solutions

# word_list = ["aardvark", "baboon", "camel"]
# # random_number = random.randint(0, len(word_list) - 1)
# # word = word_list[random_number]

# chosen_word = random.choice(word_list)
# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# display = []
# word_length = len(chosen_word)

# # for letter in chosen_word:
# for letter in range(word_length):
#     #display.append("_")
#     display += "_"

# print(display)

# # guess = input("Guess a letter: ")
# guess = input("Guess a letter: ").lower()

# #letter_position = 0

# # for letter in chosen_word:
# for position in range(word_length):
#     #if guess == letter:
#     #if letter == guess:
#         #print("Right")
#         #display[letter_position] = guess
#     #else:
#         #print("Wrong")
#     #letter_position += 1
#     letter = chosen_word[position]
#     if letter == guess:
#         display[position] = letter
# print(display)