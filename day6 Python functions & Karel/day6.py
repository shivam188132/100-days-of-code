"""def my_function():
    print("hello")
    print("world")

my_function()

#2
def turn_around():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
#robot square    
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()
turn_left()

#6

def turn_around():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
for movement in range(1,7):
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

    #or

def turn_around():
    turn_left()
    turn_left()
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
for movement in range(6):
    jump()

#7
def turn_around():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    while not right_is_clear():
        move()
    if right_is_clear():
        turn_right()
        move()
        turn_right()
        while not wall_in_front():
            move()
        turn_left()    
while not at_goal():
    if wall_in_front():
        jump()
    else :"""



