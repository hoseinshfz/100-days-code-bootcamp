from __init__ import *


class Snake:
    def __init__(self):
        self.size = SNAKE_INITIAL_SIZE
        self.body = []
        for i in range(self.size):
            piece = self.piece_maker()
            tup = (0 - i * SNAKE_PIECE_SIZE, 0)
            piece.goto(tup)
            self.body.append(piece)
        self.head = self.body[0]

    @staticmethod
    def piece_maker():
        """Creates a Turtle object for the snake's piece and return it"""
        piece = Turtle('square')
        piece.color('white')
        piece.speed('fastest')
        piece.penup()
        return piece

    def move(self):
        """move the snake's head forward and the body pieces take prior pieces' position,
        then checks for collision with wall or tail"""
        for i in range(len(self.body) - 1, 0, -1):
            xcor = self.body[i - 1].xcor()
            ycor = self.body[i - 1].ycor()
            self.body[i].goto(xcor, ycor)
        self.head.forward(MOVE_LENGTH)
        return self.hit_wall() or self.tail_collision_detector()

    def tail_collision_detector(self):
        """checks the collision between head and body of the snakes"""
        for piece in self.body[1:]:
            if self.head.distance(piece) < SNAKE_PIECE_SIZE / 2:
                return True
        return False

    def eat_food(self):
        """create another piece in position of the last piece after eating a food"""
        new_piece = self.piece_maker()
        xcor = self.body[len(self.body) - 1].xcor()
        ycor = self.body[len(self.body) - 1].ycor()
        tup = (xcor, ycor)
        new_piece.goto(tup)
        self.body.append(new_piece)

    def hit_wall(self):
        """detects collision with walls"""
        xcor = self.head.xcor()
        ycor = self.head.ycor()
        if (xcor >= SCREEN_LENGTH / 2 - 5) or (xcor <= -SCREEN_LENGTH / 2 + 5) or (
                ycor >= SCREEN_WIDTH / 2 - 5) or (ycor <= -SCREEN_WIDTH / 2 + 5):
            return True
        else:
            return False

    def turn_left(self):
        """change snake's head to left if it wasn't toward right"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_up(self):
        """change snake's head to up if it wasn't toward down"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_right(self):
        """change snake's head to right if it wasn't toward left"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def turn_down(self):
        """change snake's head to down if it wasn't toward up"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
