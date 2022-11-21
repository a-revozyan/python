from turtle import Turtle

class Tim(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.color("black")
        self.showturtle()
        self.shape("turtle")
        self.goto(0, -280)
        self.setheading(90)

    def up(self):
        self.forward(10)

    def right(self):
        self.setheading(0)
        self.forward(10)
        self.setheading(90)

    def left(self):
        self.setheading(180)
        self.forward(10)
        self.setheading(90)

    def down(self):
        self.setheading(270)
        self.forward(10)
        self.setheading(90)

    def returning(self):
        self.goto(0, -280)