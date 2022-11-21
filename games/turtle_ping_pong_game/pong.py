import random
from turtle import Turtle, Screen

screen = Screen()
MOVE_DISTANCE = 3
RANDOM_Y = random.randint(-260, 260)
P_HEIGHT = 290.0
N_HEIGHT = -280.0
CORNER = 45
P_WIDTH = 30
N_WIDTH = -30
BALL_WIDTH = 1.0
BALL_LENGTH = 1.0
P_PADDLE_COL = 550
N_PADDLE_COL = -550
START_DX = 4
START_DY = -4
NEW_DY = -1

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fast")
        self.shape("circle")
        self.color("white")
        self.shapesize(BALL_WIDTH, BALL_LENGTH)
        self.goto(0, RANDOM_Y)
        self.dx = START_DX
        self.dy = START_DY
        self.move_speed = 0.01

    def move(self):
        self.forward(MOVE_DISTANCE)
        self.setx(self.xcor()+self.dx)
        self.sety(self.ycor()+self.dy)

    def wall_collisions(self):
        if self.ycor() > P_HEIGHT:
            self.sety(P_HEIGHT)
            self.dy *= NEW_DY
        if self.ycor() < N_HEIGHT:
            self.sety(N_HEIGHT)
            self.dy *= NEW_DY

    def returning(self):
        if self.xcor() > P_PADDLE_COL or self.xcor() < N_PADDLE_COL:
            self.hideturtle()
            self.goto(0, RANDOM_Y)
            self.showturtle()