from __init__ import *


def draw_filed_line():
    """draws the middle line"""
    field = Turtle()
    field.hideturtle()
    field.penup()
    field.goto(0, SCREEN_WIDTH / 2)
    field.setheading(DOWN)
    field.pencolor('white')
    for i in range(int(SCREEN_WIDTH / MOVE_LENGTH)):
        field.pendown()
        field.forward(MOVE_LENGTH/2)
        field.penup()
        field.forward(MOVE_LENGTH/2)


