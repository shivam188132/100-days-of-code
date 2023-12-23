from turtle import Turtle,Screen
import random
new_turtle= Turtle()
screen= Screen()
is_race_on=False

screen.setup(width=500, height= 500)
user_bet=screen.textinput(title="make your bet" , prompt= "which turtle is going to win the race? Enter the color: ")
The_color=["red", "yellow", "blue", "green", "black", "pink"]

all_turtles=[]
# creating 6 turtles:
for _ in range(len(The_color)):
    new_turtle= Turtle(shape="turtle")
    new_turtle.color(The_color[_])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-180+50*_)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        #230 is 250 half width of turtle
        if turtle.xcor()>220:
            is_race_on=False
            winning_color= turtle.pencolor()
            if winning_color== user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)














screen.exitonclick()