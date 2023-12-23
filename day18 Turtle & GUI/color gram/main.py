import turtle as turtle_module
import random

no_of_dots=101

turtle_module.colormode(255)

tim=turtle_module.Turtle()
color_list = [(230, 233, 238), (239, 231, 235), (228, 236, 231), (196, 162, 104), (66, 91, 124),
              (140, 169, 190), (134, 92, 54), (218, 205, 124), (127, 30, 54), (28, 38, 62), (147, 64, 86), (75, 17, 35),
              (183, 142, 158), (134, 180, 144), (159, 154, 56), (49, 56, 96), (177, 99, 110), (52, 32, 20),
              (71, 126, 103), (104, 119, 162), (85, 147, 157), (172, 206, 170), (91, 149, 107), (220, 175, 187),
              (186, 101, 81), (166, 200, 211), (77, 72, 41), (132, 37, 28), (178, 189, 211)]

tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(400)
tim.setheading(0)



for dot_count in range(1, no_of_dots):
    
    tim.dot(20, random.choice(color_list))
    tim.forward(40)

    if dot_count %10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(400)
        tim.setheading(0)





















screen=turtle_module.Screen()
screen.exitonclick()