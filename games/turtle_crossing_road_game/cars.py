from turtle import Turtle
import random

CAR_SPEED = 0.5
Y_RANGE_N = -250
Y_RANGE_P = 250
X_LOCATION = 280
COLORS = ['red', 'orange', 'yellow', 'green', 'blue',
          'purple', 'pink', 'brown', 'gold', 'cyan',
          'dimgray', 'LimeGreen', 'DarkKhaki', 'Khaki']

class Car():
    def __init__(self):
        self.cars = []

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle()
            car.penup()
            car.shape("square")
            car.shapesize(1, 1.8)
            car.showturtle()
            car.color(random.choice(COLORS))
            car.goto(X_LOCATION, random.randint(Y_RANGE_N, Y_RANGE_P))
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.backward(CAR_SPEED)
