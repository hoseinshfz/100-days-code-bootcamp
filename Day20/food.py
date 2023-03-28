from __init__ import *


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('blue')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        """generates new food in random position after snake eats the food"""
        pos = SCREEN_WIDTH/2 - SNAKE_PIECE_SIZE
        self.goto(random.randint(-pos, pos), random.randint(-pos, pos))
