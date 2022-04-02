# SECTION 5-48
# fruits = ["Apple", "Peach", "Pear"]

# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")

# SECTION 5-49 CHALLENGE
# 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()

# number_of_inputs = 0
# sum_of_heights = 0

# for item in student_heights:
#   number_of_inputs += 1
#   sum_of_heights += int(item)

# for height in student_heights:
#     sum_of_heights += int(height)

# for student in student_heights:
#     number_of_inputs += 1

# average_height = round(sum_of_heights / number_of_inputs)
# print(average_height)

# SECTION 5-50 CHALLENGE
# student_scores = input("Input a list of student scores ").split()
 
# highest_score = 0

# for score in student_scores:
#     int_score = int(score)
#     if int_score > highest_score:
#         highest_score = int_score

# print(f"The highest score in the class is: {highest_score}")

# SECTION 5-51
# for number in range(1, 10):
#     print(number)

# for number in range(1, 10, 3):
#     print(number)

# SECTION 5-52 CHALLENGE
# total = 0
# for number in range(1, 101):
#     if (number % 2) == 0:
#         total += number
# print(total)

# total = 0
# for number in range(2, 101, 2):
#     total += number
# print(total)


# SECTION 5-53 CHALLENGE
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 5 == 0:
#         print("Buzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     else:
#         print(number)

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '+']

def password_generator(input_letters, input_symbols, input_numbers):
    password_list = []
    for char in range (1, input_letters + 1):
        password_list += random.choice(letters)

    for char in range (1, input_symbols + 1):
        password_list += random.choice(symbols)

    for char in range (1, input_numbers + 1):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    print(password)

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password? "))
nr_numbers = int(input(f"How many numbers would you like? "))
nr_symbols = int(input(f"How many symbols would you like? "))


# MY SOLUTION FOR 5-54 PROJECT
# password_values = []
# password = ""

# for n in range(1, nr_letters + 1):
#     rand_int = random.randint(0, (len(letters)-1))
#     password_values.append(letters[rand_int])

# for n in range(1, nr_numbers + 1):
#     rand_int = random.randint(0, (len(numbers)-1))
#     password_values.append(numbers[rand_int])

# for n in range(1, nr_symbols + 1):
#     rand_int = random.randint(0, (len(symbols)-1))
#     password_values.append(symbols[rand_int])

# for n in range(1, len(password_values) + 1):
#     rand_int = random.randint(0, (len(password_values)-1))
#     password += password_values[rand_int]
#     password_values.pop(rand_int)

# print(password)


# TUTORIAL SOLUTION
# password_list = []
# for char in range (1, nr_letters + 1):
#     password_list += random.choice(letters)

# for char in range (1, nr_symbols + 1):
#     password_list += random.choice(symbols)

# for char in range (1, nr_numbers + 1):
#     password_list += random.choice(numbers)

# # print(password_list)
# random.shuffle(password_list)
# # print(password_list)

# password = ""
# for char in password_list:
#     password += char

# print(password)

for n in range(57):
    password_generator(nr_letters, nr_symbols, nr_numbers)