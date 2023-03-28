from __init__ import *
import time
from snake import Snake
from scoreboard import ScoreBoard
from food import Food

my_screen = Screen()
my_screen.setup(SCREEN_LENGTH, SCREEN_WIDTH)
my_screen.bgcolor('black')
my_screen.tracer(0)
snake = Snake()
my_screen.listen()
food = Food()
score_board = ScoreBoard()


def exit_func():
    """set the end_game condition to True"""
    global end_game
    print("Ciao!")
    end_game = True


end_game = False
while not end_game:
    my_screen.onkey(key='Up', fun=snake.turn_up)
    my_screen.onkey(key='Down', fun=snake.turn_down)
    my_screen.onkey(key='Left', fun=snake.turn_left)
    my_screen.onkey(key='Right', fun=snake.turn_right)
    my_screen.onkey(key='space', fun=exit_func)
    end_game = snake.move()

    if end_game:
        score_board.game_over()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.eat_food()
        score_board.increase_score()
    time.sleep(0.1)
    my_screen.update()

my_screen.exitonclick()
