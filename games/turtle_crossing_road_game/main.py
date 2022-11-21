from turtle import Screen
from tim import Tim
from cars import Car
from scoreboard import Scoreboard
import time



car = Car()
tim = Tim()
screen = Screen()
scoreboard = Scoreboard()

screen.tracer(0)
screen.setup(width=600, height=600)
screen.title("CROSSING")

screen.listen()
screen.onkeypress(tim.up, "Up")
screen.onkeypress(tim.left, "Left")
screen.onkeypress(tim.right, "Right")
screen.onkeypress(tim.down, "Down")

game_on = True
while game_on:
    time.sleep(0.01)
    screen.update()
    car.create_cars()
    car.move()
    for x in car.cars:
        if tim.distance(x) < 20:
            scoreboard.game_over()
            game_on = False
            screen.exitonclick()
    if tim.ycor() > 280:
        scoreboard.adding()
        tim.returning()

screen.exitonclick()














screen.exitonclick()

