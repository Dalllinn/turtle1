import turtle
from turtle import Turtle, Screen
from random import choice, randint

tu = Turtle()
new_screen = Screen()
turtle.colormode(255)
tu.speed("fastest")


def random_color():
    g = randint(0, 255)
    b = randint(0, 255)
    r = randint(0, 255)
    my_tuple = (r, g, b)
    return my_tuple


def draw(how_many_gap):
    for a in range(int(360 / how_many_gap)):
        tu.color(random_color())
        tu.circle(100)
        tu.setheading(tu.heading() + how_many_gap)


draw(5)

new_screen.exitonclick()