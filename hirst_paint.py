# import colorgram
#
# color_list = []
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     tuple_ = (r, g, b)
#     color_list.append(tuple_)
#
# print(color_list)

import turtle as t
import random


tu = t.Turtle()
tu.penup()
tu.hideturtle()
app_screen = t.Screen()
t.colormode(255)
tu.setheading(225)
tu.forward(300)
tu.setheading(00)
tu.speed("fastest")

dots_count = 101


def random_color():
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    r = random.randint(0, 255)
    my_tuple = (r, g, b)
    return my_tuple


for dots in range(1, dots_count):
    tu.dot(20, random_color())
    tu.forward(50)
    if dots % 10 == 0:
        tu.setheading(90)
        tu.forward(50)
        tu.setheading(180)
        tu.forward(500)
        tu.setheading(0)









app_screen.exitonclick()