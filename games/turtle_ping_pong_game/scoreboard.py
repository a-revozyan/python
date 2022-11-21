from turtle import Turtle
ALIGN = "center"
MOVE = False
FONT = ('Algerian', 48, 'normal')
COR_X = 230
SCORE = 1

class Scoreboard(Turtle):
    def __init__(self, loc):
        super().__init__()
        self.penup()
        self.speed("fast")
        self.color("white")
        self.score = SCORE
        self.hideturtle()
        self.goto(loc, COR_X)

    def showing(self):
        self.clear()
        self.write(f"{self.score}", move=MOVE, align=ALIGN, font=FONT)
        self.score += SCORE