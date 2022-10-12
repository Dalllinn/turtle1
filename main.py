import turtle
from turtle import Turtle, Screen
from random import choice,randint
#  from tkinter import ttk,colorchooser

tu = Turtle()
new_screen = Screen()
turtle.colormode(255)
#  tu.color("green")
#  tu.shape("turtle")


# def turtle_square():
#     for a in range(15):
#         tu.forward(10)
#         tu.penup()
#         tu.forward(10)
#         tu.pendown()
#
#
# turtle_square()


#
tu_directions = [0, 90, 180, 270]
tu.pensize(15)
tu.speed("fastest")


def random_color():
    g = randint(0, 255)
    b = randint(0, 255)
    r = randint(0, 255)
    my_tuple = (r, g, b)
    return my_tuple


for a in range(220):
    tu.color(random_color())
    tu.forward(40)
    tu.setheading(choice(tu_directions))


# def shape(num_of_sides):
#     angle = 360 / num_of_sides
#     for b in range(num_of_sides):
#         tu.forward(100)
#         tu.right(angle)
#
#
# for a in range(3, 11):
#     tu.pencolor(choice(color_list))
#     shape(a)

new_screen.exitonclick()
