import math

# Section 8-79

# def greet():
#     print("Hi!")
#     print("Welcome to day 8.")
#     print("Enjoy the lessons and challenges.")

# greet()

# the PARAMETER is the name of the data that's being passed in
# the ARGUMENT is the actual data that's being passed
# sample for "def greet(name)" --> name in the function is the PARAMETER
# greet("Mia") --> the actual value passed "Mia" is the ARGUMENT
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")

# greet_with_name("Megan")


# Section 8-80
# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")

# # sample of POSITIONAL arguments
# greet_with("Megan", "Melbourne")

# # sample of KEYWORD arguments
# greet_with(location="Melbourne", name="Megan")




# Section 8-81
#Write your code below this line 👇

# def paint_calc(height, width, cover):
#     # number_of_cans = math.ceil((height * width) / cover)
#     area = height * width
#     number_of_cans = math.ceil(area / cover)
#     print(f"You'll need {number_of_cans} cans of paint.")

# #Write your code above this line 👆
# # Define a function called paint_calc() so that the code below works.   

# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)



# Section 8-82
#Write your code below this line 👇

# def prime_checker(number):
    # number_of_divisors = 0
    # checker = int(number)
    # while checker > 0:
    #     if number % checker == 0:
    #         number_of_divisors += 1
    #     checker -= 1

    # is_prime = True

    # for i in range(2,number):
    #     if number % i == 0:
    #         is_prime == False
    # # print(number_of_divisors)

    # # if number_of_divisors <= 2:
    # if is_prime:
    #     print("It's a prime number")
    # else:
    #     print("It's not a prime number")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
# n = int(input("Check this number: "))
# prime_checker(number=n)


# Section 8-83 PROJECT
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

continue_game = True
# def encrypt(plain_text, shift_amount):
#     # print("Encypt")
#     cipher_text = ""

#     for letter in plain_text:
#         # for position in range(alphabet_length):
#         #     if letter == alphabet[position]:
#         #         cipher_text += alphabet[position + shift_amount]
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
        
#         # if new_position > alphabet_length:
#         #     new_position = new_position - alphabet_length - 1

#         new_letter = alphabet[new_position]
#         cipher_text += new_letter

#     print(f"The encoded text is {cipher_text}")

# def decrypt(cipher_text = text, shift_amount = shift):
#     plain_text = ""

#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         plain_text += new_letter

#     print(f"The decoded text is {plain_text}")

# def decrypt():
#     print("Decrypt")

# if direction == "encode":
#     encrypt(plain_text = text, shift_amount = shift)
# elif direction == "decode":
#     decrypt(plain_text = text, shift_amount = shift)


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    # input_direction = ""

    for letter in start_text:
        position = alphabet.index(letter)

        # if cipher_direction == "encode":
        #     new_position = position + shift_amount
        #     input_direction = "encoded"

        # elif cipher_direction == "decode":
        #     new_position = position - shift_amount
        #     input_direction = "decoded"
        
        if cipher_direction == "decode":
            shift_amount *= -1
        
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        end_text += new_letter

    # print(f"The {input_direction} text is {end_text}")
    print(f"The {cipher_direction}d text is {end_text}")


while continue_game:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    alphabet_length = len(alphabet) - 1

    caesar(start_text = text, shift_amount = shift, cipher_direction = direction)

    prompt_continue = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

    if prompt_continue == "no":
        continue_game = False




############################################
############################################
############################################


from cipher_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabet_length = len(alphabet)

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""

    if cipher_direction == "decode":
            shift_amount *= -1 

    for char in start_text:
        # if char.isalpha():
        if char in alphabet:
            position = alphabet.index(char)          
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            end_text += new_letter
        else:
            end_text += char

    print(f"The {cipher_direction}d text is {end_text}")

print(logo)

continue_game = True

while continue_game:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # if shift > alphabet_length:
    #     shift = shift % alphabet_length 

    shift = shift % alphabet_length 

    caesar(start_text = text, shift_amount = shift, cipher_direction = direction)

    prompt_continue = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

    if prompt_continue == "no":
        continue_game = False
        print("Goodbye")