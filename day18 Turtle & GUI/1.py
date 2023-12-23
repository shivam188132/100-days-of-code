from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

'''timmy.shape("timmy")
timmy.color("red")
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)'''

# or

'''for _ in range(4):
    timmy.forward(100)
    timmy.right(90)
screen.exitonclick()

import heroes
print(heroes.gen())'''


timmy.home()
timmy.dot()
timmy.fd(50); timmy.dot(20, "blue"); timmy.fd(50)
timmy.position()

timmy.heading()