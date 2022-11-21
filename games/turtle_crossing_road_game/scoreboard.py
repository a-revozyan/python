from turtle import Turtle

ALIGN = "left"
MOVE = False
FONT = ('Algerian', 24, 'normal')
LOCATION = -280, 250

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        self.penup()
        self.name = ""
        self.hideturtle()
        self.goto(LOCATION)
        self.write(f"LEVEL: {self.score}", move=MOVE, align=ALIGN, font=FONT)

    def adding(self):
        self.clear()
        self.score += 1
        self.write(f"LEVEL: {self.score}", move=MOVE, align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=MOVE, align=ALIGN, font=FONT)