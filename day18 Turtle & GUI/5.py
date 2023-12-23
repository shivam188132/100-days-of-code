import turtle as t
import random
timmy= t.Turtle()
# colour=["red", "purple", "blue", "green", "orange"]
t.colormode(255)

def random_color():
     r= random.randint(0,255)
     g= random.randint(0,255)
     b= random.randint(0,255)
     random_color=(r,g,b)
     return random_color




direction= [0, 90,180,270]
timmy.pensize(15)
timmy.speed("fastest")

for _ in range(100):
    # timmy.color(random.choice(colour))
    timmy.color(random_color())
    
    timmy.forward(30)
    timmy.setheading(random.choice(direction))