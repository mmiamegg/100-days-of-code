from random import randint
from higher_lower_art import logo
from higher_lower_art import vs
from higher_lower_data import data

def compare(a, b):   
    print(f"Compare A: {data[a]['name']}, a {data[a]['description']}, from {data[a]['country']}")
    print(vs)
    print(f"Compare B: {data[b]['name']}, a {data[b]['description']}, from {data[b]['country']}")

    correct_answer = higher_follower_count(a,b)
    user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()        
    if user_answer == correct_answer:
        return 1
    else:
        return 0

def higher_follower_count(a,b):
    if data[a]['follower_count'] > data[b]['follower_count']:
        return "a"
    else:
        return "b"

def generate_random_number():
    return randint(0, 49)
    
print(logo)
score = 0
gameover = False
while not gameover:
    if score == 0:
        a = generate_random_number()
        b = generate_random_number()
        if a == b:
            b = generate_random_number()
    else:
        a = b
        b = generate_random_number()
        if a == b:
            b = generate_random_number()
    point = compare(a, b)
    score += point
    if point == 1:
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        gameover = True