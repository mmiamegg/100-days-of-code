# SECTION 6-57

# create a function
def my_function():
    print("Hello")
    print("Bye")

my_function()


# SECTION 6-59
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for hurdles in range(6):
    jump()


# SECTION 6-60
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# or while at_goal() != True:
while not at_goal():
    jump()


# SECTION 6-61
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
# while not at_goal():
#     if front_is_clear():
#         move()
#     elif wall_in_front():
#         jump()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

# SECTION 6-62
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def check_right_wall():
#     while not right_is_clear():
#         move()
# def check_front_wall():
#     while front_is_clear():
#         move()
# def jump():
#     turn_left()
#     check_right_wall()
#     turn_right()
#     move()
#     turn_right()
#     check_front_wall()
#     turn_left()   
# while not at_goal():
#     if front_is_clear():
#         move()
#     elif wall_in_front():
#         jump()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()   
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()