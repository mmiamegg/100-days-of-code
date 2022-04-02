# import random
# from blackjack_art import logo

# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# player_cards = []
# computer_cards = []

# player_score = 0
# computer_score = 0

# blackjack_players = {
#     "Player": player_cards,
#     "Computer": computer_cards
# }

# def deal_cards(deal):
#     while len(deal) < 2:
#         deal.append(random.choice(cards)) 

# # def compute_score():
# #     for card in player_cards:
# #         player_score += int(card)
    
# #     print(f"Your cards: {player_cards}, current score: {player_score}")

# #     print(f"Computer's first card: {computer_cards[0]}")

# deal_cards(blackjack_players["Player"])
# deal_cards(blackjack_players["Computer"])

# # compute_score()

# for card in player_cards:
#     player_score += int(card)
    
# print(f"Your cards: {player_cards}, current score: {player_score}")
# print(f"Computer's first card: {computer_cards[0]}")






















# import random
# #from blackjack_art import logo

# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# should_continue = True

# # player_cards = []
# # computer_cards = []

# # player_score = 0
# # computer_score = 0

# # players = {
# #     "Player": player_cards,
# #     "Computer": computer_cards,
# # }

# # def deal_cards(current_player):
# #     while len(current_player) < 2:
# #         current_player.append(random.choice(cards))

# # def hit(current_player):
# #     new_card = random.choice(cards)
# #     current_player.append(new_card)

# # def total_score(current_player):


# while should_continue:
#     player_cards = []
#     computer_cards = []

#     player_score = 0
#     computer_score = 0

#     # deal cards to player (TRANSFER TO FUNCTION deal_cards() later)
#     while len(player_cards) < 2:
#         player_cards.append(random.choice(cards))
#     # deal cards to computer (TRANSFER TO FUNCTION deal_cards() later)
#     while len(computer_cards) < 2:
#         computer_cards.append(random.choice(cards)) 

#     deal_cards(players["Player"])
#     deal_cards(players["Computer"])

#     # total the score of player cards (TRANSFER TO FUNTION compute_score() later) 
#     for card in player_cards:
#         player_score += card

#     for card in computer_cards:
#         computer_score += card

        
#     print(f"Your cards: {player_cards}, current score: {player_score}")
#     print(f"Computer's first card: {computer_cards[0]}")

#     game_over = False
#     # while player_score < 21:
#     while not game_over:
#         next_move = input("Type 'y' to get another card, type 'n' to pass:").lower()

#         if next_move == 'y':
#             new_card = random.choice(cards)
#             player_cards.append(new_card)
#             player_score += new_card

#             print(f"Your cards: {player_cards}, current score: {player_score}")
#         else:
#             print(f"Your cards: {player_cards}, current score: {player_score}")
#             print(f"Computer's cards: {computer_cards}, current score: {computer_score}")

#             if computer_score < 17:
#                 new_card = random.choice(cards)
#                 computer_cards.append(new_card)
#                 computer_score += new_card
        
#         if player_score > 21:
#             print(f"Your cards: {player_cards}, current score: {player_score}")
#             print(f"Computer's cards: {computer_cards}, current score: {computer_score}")

#             print("You lose.")
#             game_over = True
#         elif player_score == 21:
#             print(f"Your cards: {player_cards}, current score: {player_score}")
#             print(f"Computer's cards: {computer_cards}, current score: {computer_score}")

#             print("Blackjack!")
#             game_over = True
#         else:
#             print(f"Your cards: {player_cards}, current score: {player_score}")

#             print(f"Computer's cards: {computer_cards}, current score: {computer_score}")

#             while computer_score < 17:
#                 new_card = random.choice(cards)
#                 computer_cards.append(new_card)
#                 computer_score += new_card

#                 print(f"Computer's cards: {computer_cards}, current score: {computer_score}")

#             if computer_score > 21:
#                 print("You win!")
#                 game_over = True
#             elif player_score > computer_score:
#                 print("You win!")
#                 game_over = True
#             elif player_score == computer_score:
#                 print("Draw")
#                 game_over = True
#             else:
#                 print("You lose.")
#                 game_over = True
    
#     if input("Continue:") == "n":
#         should_continue = False




# MY SOLUTION FOR DAY 11 CAPSTONE PROJECT
import random
# n

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
should_continue = True

def deal_cards(current_player):
    current_player.append(random.choice(cards))

def compute_score(current_player):
    score = 0
    for card in current_player:
        score += card
    if ace_card_draw and score > 21:
        score -= 10
    return score

def display_results():
    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Computer's cards: {computer_cards}, current score: {computer_score}")

def ace_card_draw(current_player):
    ace_card = False
    for card in current_player:
        if card == 11:
            ace_card = True
    return ace_card

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
    while not game_over:
        next_move = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if next_move == 'y':
            deal_cards(players["Player"])
            player_score = compute_score(players["Player"])
        
        display_results()
        if player_score > 21:
            print("You lose.")
            game_over = True
        elif player_score == 21:
            print("Blackjack!")
            game_over = True
        else:
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