import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
INITIAL_WAIT = 0.075

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
traffic = CarManager()
player = Player()
score = Scoreboard()

game_is_on = True
level = 1
while game_is_on:
    screen.onkey(key='Up', fun=player.move)
    time.sleep(INITIAL_WAIT/level)
    traffic.new_car()
    traffic.move()
    if player.detect_collision(traffic.cars):
        game_is_on = False
        score.game_over()
    if player.level > level:
        traffic.level_up()
        level += 1
        score.increase_score()
    screen.update()

screen.exitonclick()

