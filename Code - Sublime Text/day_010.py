# Section 10-97

# def my_function():
#     result = 3 * 2
#     return result

# def my_function():
#     return 3 * 2

# output = my_function()

# Functions with Outputs

# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = f_name.title()

#     return f"{formated_f_name} {formated_l_name}"

# formated_string = format_name("mia", "megan")
# print(formated_string)

# Section 10-98
# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "You didn't provide valid inputs."
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()

#     return f"Result: {formated_f_name} {formated_l_name}"

# print(format_name(input("What is your first name? "), input("What is your last name? ")))

# Section 10-99 PROJECT
# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# def days_in_month(input_year, input_month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
#     # if input_month == 2:
#     #     if is_leap(input_year):
#     #         return 29
#     #     else:
#     #         return month_days[input_month-1]
#     # else:
#     #     return month_days[input_month-1]

#     if is_leap(input_year) and month == 2:
#         return 29
#     else:
#         return month_days[input_month-1] 

  
# #🚨 Do NOT change any of the code below 
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

# Section 10-100
# def format_name(f_name, l_name):
#     """Take a first and last name and format it
#     to return the title case version of the name."""
#     if f_name == "" or l_name == "":
#         return "You didn't provide valid inputs."
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()

#     return f"Result: {formated_f_name} {formated_l_name}"

# print(format_name(input("What is your first name? "), input("What is your last name? ")))

# format_name(f_name, l_name)


# Section 10-101 PROJECT
from calculator_art import logo

# add
def add(n1, n2):
    return n1 + n2

# subtract
def subtract(n1, n2):
    return n1 - n2

# multiply
def multiply(n1, n2):
    return n1 * n2

# divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# finished = False
# continue_calculating = "n"
# answer = 0

# while not finished:
#     if continue_calculating == 'n':
#         num1 = int(input("What's the first number?: "))
#         for symbol in operations:
#             print(symbol)
#     else:
#         num1 = answer

#     operation_symbol = input("Pick an operation: ")
#     num2 = int(input("What's the next number?: "))
#     calculation_function = operations[operation_symbol]
#     answer = calculation_function(num1, num2)

#     print(f"{num1} {operation_symbol} {num2} = {answer}")

#     continue_calculating = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ").lower()

#     if continue_calculating == 'n':
#         finished = True

def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ").lower() == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()