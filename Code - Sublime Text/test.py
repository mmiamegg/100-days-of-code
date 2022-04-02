##############
#  PROBLEM 1 #
##############
# from random import randint

# def digital_root(n):
#     digits = str(n)
#     length = len(digits)
#     sum = 0
#     while length > 1:
#         sum = 0
#         for number in digits:
#             sum += int(number)
#         digits = str(sum)
#         length = len(digits)
#     return sum

##############
#  PROBLEM 2 #
##############
# def duplicate_count(text):
#     text = text.lower()
#     length = len(text)
#     duplicates = 0
#     for letter in text:
#         count = 0
#         for position in range (0, length):
#             if letter == text[position]:
#                 count += 1
#             # print(f"{letter} compare to {text[position]}")
#         if count > 1:
#             duplicates += 1
#             new_text = ""
#             for position in range(0, length):
#                if text[position] != letter:
#                    new_text += text[position]
#             text = new_text
#             print(new_text)
#             length = len(text)
#     return duplicates

##############
#  PROBLEM 3 #
##############
# def get_sum(a,b):
#     sum = 0
#     if a > b:
#         c = a
#         a = b
#         b = c    
#     if a == b:
#         return a
#     else:
#         while a != (b + 1):
#             sum += a
#             a += 1
#             # print(a)
#     return sum

# print(get_sum(2, -1))

##############
#  PROBLEM 3 #
##############
# def get_sum(a,b):
#     sum = 0
#     if a > b:
#         c = a
#         a = b
#         b = c    
#     if a == b:
#         return a
#     else:
#         while a != (b + 1):
#             sum += a
#             a += 1
#             # print(a)
#     return sum

# # print(get_sum(2, -1))



##############
#  PROBLEM 4 #
##############
# def row_sum_odd_numbers(n):
#     sum = 0
#     list_odd_numbers = row_odd_numbers(n)
#     for number in list_odd_numbers:
#         sum += number
#     return sum

# def row_odd_numbers(n):
#     row = 0
#     count = 1
#     number = 1
#     while row < n:
#         list_odd_numbers = []
#         row += 1
#         for odd_number in range(0, count):
#             list_odd_numbers.append(number)
#             number += 2
#         count += 1
#     return list_odd_numbers
        
# row_sum_odd_numbers(13)



##############
#  PROBLEM 5 #
##############
# def move_zeros(array):
#     numbers = []
#     zeroes = 1
#     for number in array:
#         if number != 0:
#            numbers.append(number)
#         else:
#             zeroes += 1   
#     for zero in range(0,zeroes):
#         numbers.append(0)
#     array = numbers
#     return array

# print(move_zeros([1, 0, 1, 2, 0, 1, 3]))



# def create_phone_number(n):
#     phone_number = "("    
#     for number in range(0,3):
#         phone_number += str(n[number])
#     phone_number += ") "
#     for number in range(3,6):
#         phone_number += str(n[number])
#     phone_number += "-"
#     for number in range(6,10):
#         phone_number += str(n[number])
#     return phone_number

# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])




# def valid_parentheses(string):
#     count = 0
#     parentheses = ""
#     for character in string:
#         if character == "(":
#             count +=1
#             parentheses += "("
#         elif character == ")":
#             count -= 1
#             parentheses += ")"
#     print(parentheses)
#     if count == 0:
#         test = parentheses
#         length = len(test)
#         while length > 2:                             
#             test = test.replace("()", "")
#             length = len(test)
#         if test == ")(":
#             return False
#         else:
#             return True   
#     else:
#         return False
        
#     print(test)
     
# valid_parentheses("(())((()())())")




def duplicate_encode(word):
    word = word.lower()
    length = len(word)
    word_convert = ""
    for letter in range (0, length):
        count = 0        
        for position in range (0, length):
            if word[letter] == word[position]:
                count += 1
            print(f"{word[letter]} compare to {word[position]}")
        print(f"number times of letter {word[letter]}: {count}")
        if count > 1:
            word_convert += "("
        else:
            word_convert += ")"
    return word_convert

duplicate_encode("woord")