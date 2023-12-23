import turtle as t
from turtle import Screen
import random
timmy= t.Turtle()
screen= Screen()

# colour=["red", "purple", "blue", "green", "orange"]
t.colormode(255)

def random_color():
     r= random.randint(0,255)
     g= random.randint(0,255)
     b= random.randint(0,255)
     random_color=(r,g,b)
     return random_color





timmy.speed("fastest")
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        # print(timmy.heading())

        # current_heading=timmy.heading()
        # timmy.setheading(current_heading+10)
        timmy.setheading(timmy.heading()+size_of_gap)

draw_spirograph(2)
screen.exitonclick()