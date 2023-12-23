from turtle import Turtle
import random
timmy=Turtle()
colour=["red", "purple", "blue", "green", "orange"]

timmy.shape("turtle")
# n=int(input("enter the number of side that you want: "))
def draw_figure(n):
    angle=360/n
    for _ in range(n):
        timmy.forward(100)
        timmy.right(angle)
        

for op in range(3,11):
    timmy.color(random.choice(colour))
    draw_figure(op)
        
 