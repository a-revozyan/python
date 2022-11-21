from turtle import Turtle
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
MOVE = 10
SHAPE_WIDTH = 2.0
SHAPE_LENGTH = 6.0
P_YCOR = 235
N_YCOR = -230

class Paddle(Turtle):
    def __init__(self, location):
        super().__init__()
        self.penup()
        self.goto(location, 0)
        self.shapesize(SHAPE_WIDTH, SHAPE_LENGTH)
        self.setheading(UP)
        self.speed("fastest")
        self.shape("square")
        self.color("white")

    def up(self):
        self.setheading(UP)
        self.forward(MOVE)
        if self.ycor() > P_YCOR:
            self.setheading(DOWN)
            self.forward(MOVE)

    def down(self):
        self.setheading(DOWN)
        self.forward(MOVE)
        if self.ycor() < N_YCOR:
            self.setheading(UP)
            self.forward(MOVE)
