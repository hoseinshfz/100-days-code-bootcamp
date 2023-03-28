from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 90


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(UP)
        self.level = 1

    def move(self):
        """moves the player and if player has passed the finish line, resets its position"""
        if self.ycor() >= FINISH_LINE_Y:
            self.level += 1
            self.goto(STARTING_POSITION)
        else:
            self.forward(MOVE_DISTANCE)

    def detect_collision(self, traffic):
        """detect collision with traffic and terminates the game if it happens"""
        for car in traffic:
            if self.distance(car) < 20:
                print("Game Over")
                return True
        return False
