from turtle import Turtle

P_HEIGHT = 290.0
N_HEIGHT = -285.0
STEP = 20
PENSIZE = 4.0

class Drawing(Turtle):
    def __init__(self):
        super().__init__()
        self.pensize(PENSIZE)
        self.hideturtle()
        self.speed("fastest")
        self.color("white")

    def strings(self):
        self.penup()
        self.goto(0, N_HEIGHT)
        self.setheading(90)
        while self.ycor() < P_HEIGHT:
            self.pendown()
            self.forward(STEP)
            self.penup()
            self.forward(STEP)
        self.goto(0, -100)
        self.setheading(0)
        self.pendown()
        self.circle(100, 360)









