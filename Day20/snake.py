from turtle import Turtle

class Snake:
    def __init__(self):
        self.size = SNAKE_INITIAL_SIZE
        self.piece_xy = []
        self.body = []
        for i in range(self.size):
            # piece = Turtle('square')
            # piece.color('white')
            # piece.speed('fastest')
            # piece.penup()
            piece = self.piece_maker()
            tup = (0 - i*20, 0)
            #self.piece_xy.append(tup)
            piece.goto(tup)
            self.body.append(piece)
        self.head = self.body[0]

    def piece_maker(self):
        piece = Turtle('square')
        piece.color('white')
        piece.speed('fastest')
        piece.penup()
        return piece

    def move(self):
        for i in range(len(self.body)-1, 0, -1):
            xcor = self.body[i-1].xcor()
            ycor = self.body[i-1].ycor()
            self.body[i].goto(xcor, ycor)
        self.head.forward(MOVE_LENGTH)

    def tail_collision_detector(self):
        xcor = self.head.xcor()
        ycor = self.head.ycor()
        #print(f"{xcor}, {ycor}")
        for piece in self.body[1:]:
            #print("#")
            #print(f"###\n{piece.xcor()}, {piece.ycor()}")
            #if (xcor >= piece.xcor() - 5  and xcor <= piece.xcor() + 5) and (
            #        ycor >= piece.ycor() - 5 and ycor <= piece.ycor() + 5):
            if self.head.distance(piece) < 10:
                print(f"{xcor}, {ycor}")
                print(f"###\n{piece.xcor()}, {piece.ycor()}")
                return True
            #else:
            #    return False
        return False

    def eat_food(self):
        new_piece = self.piece_maker()
        xcor = self.body[len(self.body)-1].xcor()
        ycor = self.body[len(self.body) - 1].ycor()
        tup = (xcor, ycor)
        new_piece.goto(tup)
        self.body.append(new_piece)

    def hit_wall(self):
        xcor = self.head.xcor()
        ycor = self.head.ycor()
        if (xcor >= SCREEN_LENGTH/2 or xcor <= -SCREEN_LENGTH/2) or (
                ycor >= SCREEN_WIDTH/2 or ycor <= -SCREEN_WIDTH/2):
            return True
        else:
            return False

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        #print("L")

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        #print("U")

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        #print("R")

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        #print("D")
