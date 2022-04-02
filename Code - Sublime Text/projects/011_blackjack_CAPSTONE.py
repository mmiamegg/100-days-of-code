import random
from blackjack_art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
should_continue = True

def deal_cards(current_player):
    current_player.append(random.choice(cards))

def compute_score(current_player):
    score = 0
    for card in current_player:
        if card == 11:
            score += card
            if score > 21:
                score -= 10
        else:
            score += card
    return score

def display_results(move):
    if move == 'y':
        print(f"Your cards: {player_cards}, current score: {player_score}")
    else:
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's cards: {computer_cards}, current score: {computer_score}")

while should_continue:
    player_cards = []
    computer_cards = []

    player_score = 0
    computer_score = 0

    players = {
        "Player": player_cards,
        "Computer": computer_cards,
    }

    while len(player_cards) < 2:
        deal_cards(players["Player"])
        deal_cards(players["Computer"])

    player_score = compute_score(players["Player"])
    computer_score = compute_score(players["Computer"])
        
    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    game_over = False
    if player_score == 21:
        print("Blackjack!")
        game_over = True
    if computer_score == 21:
        print("Blackjack! You lose.")
        game_over = True
    
    while not game_over:
        if player_score < 21:
            next_move = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            
            if next_move == 'y':
                deal_cards(players["Player"])
                player_score = compute_score(players["Player"])            
                display_results(next_move)

                if player_score > 21:
                    print("You lose.")
                    game_over = True
                elif player_score == 21:
                    print("Blackjack!")
                    game_over = True
            elif next_move == 'n':
                display_results(next_move)
                while computer_score < 17:
                    deal_cards(players["Computer"])
                    computer_score = compute_score(players["Computer"])

                    print(f"Computer's cards: {computer_cards}, current score: {computer_score}")

                if computer_score > 21:
                    print("You win!")
                    game_over = True
                elif player_score > computer_score:
                    print("You win!")
                    game_over = True
                elif player_score == computer_score:
                    print("Draw")
                    game_over = True
                else:
                    print("You lose.")
                    game_over = True
    
    if input("Continue: ") == "n":
        should_continue = False