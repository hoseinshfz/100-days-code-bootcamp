from __init__ import *
from utilities import *
from player_racket import PlayerRacket
from ball import Ball
from scoreboard import ScoreBoard

my_screen = Screen()
my_screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
my_screen.bgcolor('black')
my_screen.title('Pong')
my_screen.tracer(0)
my_screen.listen()
ball = Ball()
draw_filed_line()


def exit_func():
    global end
    print("Ciao!")
    end = True


# Initializing the scoreboards for two players
score_board = []
for i in range(2):
    player = ScoreBoard(-50 + i * 100)
    score_board.append(player)

# Initializing the rackets of the players
players = []
for i in range(1, 3):
    player = PlayerRacket(i)
    players.append(player)

end = False
count = 0
while not end:
    my_screen.onkey(key='Up', fun=players[1].go_up)
    my_screen.onkey(key='Down', fun=players[1].go_down)
    my_screen.onkey(key='w', fun=players[0].go_up)
    my_screen.onkey(key='s', fun=players[0].go_down)
    my_screen.onkey(key='space', fun=exit_func)
    ball.move()
    ball.check_touch_racket(players)
    who_scored = ball.check_goal() - 1
    if who_scored >= 0:
        score_board[who_scored].increase_score()
        for player in players:
            player.reset()

    time.sleep(ball.move_speed)
    count += 1
    if count == GAME_END_TIMER:
        print("Time's Up!!")
        end = True

    my_screen.update()

my_screen.exitonclick()
