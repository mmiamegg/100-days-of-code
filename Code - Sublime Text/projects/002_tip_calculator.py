# SECTION 2-24 Project
print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))
tip_amount = int(input("What percentage tip would you like to give? 10, 12, 0r 15? "))
people = int(input("How many people to split the bill? "))

tip_percentage = 1 + (tip_amount / 100)

bill_with_tip = bill * tip_percentage
bill_per_person = round(bill_with_tip / people, 2)
total_bill = "{:.2f}".format(bill_per_person)

message = f"Each person should pay: ${total_bill}"
print(message)