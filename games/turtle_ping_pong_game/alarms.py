from turtle import Turtle

class Alarm(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.shape("square")
        self.color("red")

    def create1(self):
        self.showturtle()
        self.goto(420, 294)
        self.shapesize(0.5, 2.5)