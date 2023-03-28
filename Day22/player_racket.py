from __init__ import *


class PlayerRacket(Turtle):
    def __init__(self, player):
        super().__init__()
        self.player_id = player
        self.racket = Turtle('square')
        self.racket.color('white')
        self.racket.penup()
        self.racket.speed('fastest')
        self.racket.shapesize(stretch_wid=1, stretch_len=RACKET_SIZE)
        self.reset()
        self.racket.setheading(UP)

    def go_up(self):
        """racket moves upward"""
        self.racket.setheading(UP)
        self.racket.forward(MOVE_LENGTH)

    def go_down(self):
        """racket moves downward"""
        self.racket.setheading(DOWN)
        self.racket.forward(MOVE_LENGTH)

    def reset(self):
        """resets the positions of the rackets"""
        xcor = -SCREEN_WIDTH / 2 + RACKET_DISTANCE_FROM_WALL
        if self.player_id == 2:
            xcor *= -1
        self.racket.goto(x=xcor, y=0)
