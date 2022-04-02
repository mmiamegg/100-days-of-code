MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01,
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0
insufficient_resources = []
turn_off = False


def customer_order():
    """Ask user for drink and perform next command"""
    global turn_off
    # Take the order or command of the user
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # Check if the user made an order or typed 'report'
    if order == "report":
        # If user typed 'report', go to print_report function
        print_report()
    elif order == "off":
        turn_off = True
    else:
        # If user typed a drink, go to oder function
        make_drink(order)


def make_drink(drink):
    """Take the order of the user to process the transaction"""
    # Get the ingredients of the chosen drink from the MENU
    global profit
    selection = MENU[drink]["ingredients"]
    drink_cost = MENU[drink]["cost"]
    # Check if resources are enough
    enough_resources = check_resources(selection)

    if enough_resources:
        # Check if payment amount and if payment is enough
        total_coins = compute_coins(drink_cost)

        if total_coins >= drink_cost:
            for ingredient in selection:
                resources[ingredient] -= selection[ingredient]

            profit += drink_cost
            change = total_coins - drink_cost
            format_change = "{:.2f}".format(change)
            if change > 0:
                print(f"Here is ${format_change} dollars in change.")
                print(f"Here is your {drink}. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")
    else:
        for ingredient in insufficient_resources:
            print(f"Sorry there is not enough {ingredient}")


def compute_coins(drink_cost):
    total_coins = 0
    print("Please insert coins.")
    for coin in coins:
        count_coins = float(input("How many " + coin + "?: "))
        total_coins += float(count_coins * coins[coin])
    return total_coins


def print_report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    format_profit = "{:.2f}".format(profit)
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${format_profit}")


def check_resources(selection):
    global insufficient_resources
    # A checker for insufficient ingredients
    is_enough = True
    # Check if all ingredients have enough resources
    for ingredient in selection:
        if resources[ingredient] < selection[ingredient]:
            is_enough = False
            insufficient_resources.append(ingredient)
    return is_enough


while not turn_off:
    customer_order()