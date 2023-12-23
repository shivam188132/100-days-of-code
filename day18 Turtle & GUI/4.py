from turtle import Turtle
import random
timmy= Turtle()
colour=["red", "purple", "blue", "green", "orange"]
direction= [0, 90,180,270]
timmy.pensize(15)
timmy.speed("fastest")

for _ in range(100):
    timmy.color(random.choice(colour))
    timmy.forward(30)
    timmy.setheading(random.choice(direction))