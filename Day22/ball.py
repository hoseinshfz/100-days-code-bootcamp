import random

from __init__ import *


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('blue')
        self.speed('fast')
        self.who_scored = -1
        self.goto(0, 0)
        self.setheading(random.randint(91, 120))
        self.move_speed = INITIAL_BALL_SPEED

    def move(self):
        """ball moves half the move_length and checks if hits the wall"""
        self.forward(MOVE_LENGTH / 2)
        self.check_hit_wall()

    def check_touch_racket(self, players):
        """checks if ball has hits the rackets
        if yes, reflect from the racket and increase the speed"""
        degree = self.heading()
        hit = False
        racket_pos = SCREEN_WIDTH / 2 - RACKET_DISTANCE_FROM_WALL
        if (self.xcor() < -racket_pos + RACKET_WIDTH_SIZE) and (
                self.distance(players[0].racket) < RACKET_LENGTH / 2):
            hit = True
        elif (self.xcor() >= racket_pos - RACKET_WIDTH_SIZE) and (
                self.distance(players[1].racket) < RACKET_LENGTH / 2):
            hit = True

        if hit:
            self.move_speed *= BALL_SPEED_CHANGE_STEP
            degree = 180 - degree
            self.bounce(degree)

    def bounce(self, degree):
        """set the heading to the provided degree"""
        self.setheading(degree)

    def check_hit_wall(self):
        """checks if hits the wall, if Yes, bounce"""
        degree = self.heading()
        if self.ycor() <= -SCREEN_HEIGHT / 2 + MOVE_LENGTH or self.ycor() >= SCREEN_HEIGHT / 2 - MOVE_LENGTH:
            degree *= -1
            self.bounce(degree)

    def check_goal(self):
        """check for the scoring the goal
        return 1 if player 1 scores, and 2 for player 2, and 0 if there was no goal"""
        if self.xcor() <= -SCREEN_WIDTH / 2 + 15:
            self.who_scored = 2
            self.kick_off()
            return 2
        elif self.xcor() >= SCREEN_WIDTH / 2 - 15:
            self.who_scored = 1
            self.kick_off()
            return 1
        else:
            return 0

    def kick_off(self):
        """resets the ball in the middle toward the player who has scored"""
        self.goto(0, 0)
        if self.who_scored == 1:
            self.setheading(random.randint(100, 250))
        else:
            self.setheading(random.randint(-80, 80))
        time.sleep(0.2)
        self.move_speed = INITIAL_BALL_SPEED
        self.move()
