# SECTION 9-89

# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that can you easily call over and over again.",
#     "Loop": "The action of doing something over and over again.",
# }

# print(programming_dictionary["Bug"])

# # Adding new items to dictionary
# programming_dictionary["Loop"] = "The action of doing something over and over again."

# print(programming_dictionary)

# # Create an empty dictionary
# empty_dictionary = {}

# # # Wipe an existing dictionary
# # programming_dictionary = {}
# # print(programming_dictionary)

# # Edit an item in a dictionary
# programming_dictionary["Bug"] = "A moth in your computer."

# Loop through a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key]) # to get value


# Section 9-90 EXERCISE
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# #TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}

# #TODO-2: Write your code below to add the grades to student_grades.👇

# # for student in student_scores:
# #     if student_scores[student] >= 91:
# #         student_grades[student] = "Outstanding"
# #     elif student_scores[student] >= 81:
# #         student_grades[student] = "Exceeds Expectations"
# #     elif student_scores[student] >= 71:
# #         student_grades[student] = "Acceptable"
# #     else:
# #         student_grades[student] = "Fail"

# for student in student_scores:
#     score = student_scores[student]

#     if score > 90:
#         student_grades[student] = "Outstanding"
#     elif score > 80:
#         student_grades[student] = "Exceeds Expectations"
#     elif score > 70:
#         student_grades[student] = "Acceptable"
#     else:        
#         student_grades[student] = "Fail"

# # 🚨 Don't change the code below 👇
# print(student_grades)

# for student in student_grades:
#     print(f"{student}: {student_grades[student]}\n")


# Section 9-91
# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }

# cities_visited

# # nest list inside dictionary
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgard"],
# }

# # nest dictionary inside dictionary
# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#     "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgard"], "total_visits": 5},
# }

# # nest dictionary inside list
# travel_log = [
#     {
#         "country": "France",
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12
#     },
#     {
#         "country": "Germany",
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgard"], \
#             "total_visits": 5
#     },
# ]

# # Section 9-92 EXERCISE
# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above

# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇

# def add_new_country(country_visited, times_visited, cities_visited):
#     # travel_log.append(
#     # {
#     #     "country": country_visited,
#     #     "visits": times_visited,
#     #     "cities": cities_visited,
#     # }
#     # )

    
#     # test = {
#     #     "country": country_visited,
#     #     "visits": times_visited,
#     #     "cities": cities_visited,
#     # }

#     # travel_log.append(test)

#     new_country = {}
#     new_country["country"] = country_visited
#     new_country["visits"] = times_visited
#     new_country["cities"] = cities_visited

#     travel_log.append(new_country)


# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

# Section 9-93 PROJECT
# from replit import clear
from auction_art import logo

bids = {}
# other_bidders = True
bidding_finished = False

# def blind_auction_bidders(bidder_name, bid_price):
#     bids[bidder_name] = bid_price

# def find_highest_bidder():
#     highest_bidder = ""
#     highest_bid = 0

#     for bidder in bids:
#         if  bids[bidder] > highest_bid:
#             highest_bid = bids[bidder]
#             highest_bidder = bidder

#     print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

print(logo)
print("Welcome to the secret auction program.")

# while other_bidders:
while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))

    bids[name] = price

    # blind_auction_bidders(name, price)

    # more_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    # if more_bidders == "no":
    #     other_bidders = False

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if should_continue == "no":
        bidding_finished = True

# find_highest_bidder()
find_highest_bidder(bid)