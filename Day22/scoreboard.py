from __init__ import *


class ScoreBoard(Turtle):
    def __init__(self, posx):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(posx, SCREEN_HEIGHT / 2 - 100)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.score}", align='center', font=('Courier', 70, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_score()
