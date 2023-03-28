from turtle import Turtle
FONT = ('Arial', 12, 'normal')


class StatesNameWriter(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def write_state(self, state, pos):
        self.goto(pos)
        self.write(f"{state}", align='center', font=FONT)

