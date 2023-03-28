from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_SIZE = 2
SCREEN_WIDTH = 600
LEFT = 180


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.hideturtle()

    def new_car(self):
        """generates new cars with probability similar to rolling a dice"""
        chance = random.randint(1, 6)
        if chance == 1:
            car = Turtle('square')
            car.color(random.choice(COLORS))
            car.penup()
            car.setheading(LEFT)
            car.shapesize(stretch_wid=1, stretch_len=CAR_SIZE)
            car.speed('fastest')
            random_y_cor = random.randint(-250, 250)
            car.goto(SCREEN_WIDTH/2, random_y_cor)
            self.cars.append(car)

    def move(self):
        """deletes the cars that passed the left side of the screen from the list of cars"""
        to_delete = []
        index = 0
        for car in self.cars:
            if car.xcor() >= -320:
                car.forward(self.move_distance)
                index += 1
            else:
                to_delete.append(index)
        for i in to_delete:
            del self.cars[i]

    def level_up(self):
        """increase the traffic moving speed with each level up"""
        self.move_distance += MOVE_INCREMENT
