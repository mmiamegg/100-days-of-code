from cipher_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabet_length = len(alphabet)

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""

    if cipher_direction == "decode":
            shift_amount *= -1 

    for char in start_text:
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

    shift = shift % alphabet_length 

    caesar(start_text = text, shift_amount = shift, cipher_direction = direction)

    prompt_continue = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

    if prompt_continue == "no":
        continue_game = False
        print("Goodbye")