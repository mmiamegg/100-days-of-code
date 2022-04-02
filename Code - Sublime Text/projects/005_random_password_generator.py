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
# More readable and uses built in python functions
# instead of manually creating the solution
password_list = []
for char in range (1, nr_letters + 1):
    password_list += random.choice(letters)

for char in range (1, nr_symbols + 1):
    password_list += random.choice(symbols)

for char in range (1, nr_numbers + 1):
    password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(password)