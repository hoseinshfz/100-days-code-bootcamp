from __init__ import *


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(SCOREBOARD_LOCATION)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        """clear and writes new score"""
        self.clear()
        self.write(f"Score: {self.score}", align='center', font=('Arial', 18, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        """Writes Game over message in the middle of the screen"""
        self.goto(0, 0)
        self.pencolor('red')
        self.write(f"Game Over! Your Score: {self.score}.", align='center', font=('Arial', 24, 'normal'))
