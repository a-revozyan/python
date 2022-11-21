from turtle import Screen
from pong import Ball
from paddle import Paddle
from drawing import Drawing
from scoreboard import Scoreboard
import time

P_PADDLE_COL = 460
N_PADDLE_COL = -460
ADD_PIXELS = 30
DX = -1
P_MISS_BALL = 540
N_MISS_BALL = -549

screen = Screen()
screen.tracer(0)
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")

p_scoreboard = Scoreboard(loc=50)
l_scoreboard = Scoreboard(loc=-50)
ball1 = Ball()
drawing = Drawing()
r_paddle = Paddle(location=485)
l_paddle = Paddle(location=-490)

drawing.strings()

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

game_on = True
while game_on:
    screen.update()
    time.sleep(ball1.move_speed)
    ball1.move()
    ball1.wall_collisions()
    ball1.returning()

    # collisions with r_paddle
    if (ball1.xcor() >= P_PADDLE_COL) and (ball1.ycor() < r_paddle.ycor() + ADD_PIXELS and
                                           ball1.ycor() > r_paddle.ycor() - ADD_PIXELS):
        ball1.setx(P_PADDLE_COL)
        ball1.dx *= DX
    # collisions with l_paddle
    elif (ball1.xcor() <= N_PADDLE_COL) and (ball1.ycor() < l_paddle.ycor() + ADD_PIXELS and
                                           ball1.ycor() > l_paddle.ycor() - ADD_PIXELS):
        ball1.setx(N_PADDLE_COL)
        ball1.dx *= DX

    # missing the ball
    elif ball1.xcor() > P_MISS_BALL:
        screen.update()
        p_scoreboard.showing()
    elif ball1.xcor() < N_MISS_BALL:
        screen.update()
        l_scoreboard.showing()

    # rival moving
    elif ball1.ycor() > r_paddle.ycor() and ball1.xcor() > 0:
        r_paddle.up()
    elif ball1.ycor() < r_paddle.ycor() and ball1.xcor() > 0:
        r_paddle.down()