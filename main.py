import random
import turtle
from turtle import Turtle, Screen
turtle.colormode(255)
color_list = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203)]

tim = Turtle()
tim.shape("circle")
tim.pensize(100)



def random_color():
    color = (random.choice(color_list))
    return color


number_of_dots = 100
tim.penup()
tim.setx(-370)
tim.setheading(-90)
tim.penup()
tim.forward(200)
tim.setheading(0)

for dot in range(1, number_of_dots):
    random_color()
    tim.pendown()
    tim.dot(25,random_color())
    tim.penup()
    tim.forward(80)
    if dot % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(800)
        tim.setheading(0)







screen = Screen()
screen.exitonclick()







