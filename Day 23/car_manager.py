import random
from turtle import Turtle

COLORS = ['red', 'orange', 'black', 'green', 'blue', 'purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.cars_list = []
        self.cars_speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        random_num = random.randint(1,5)
        if random_num == 1:
            car = Turtle('square')
            car.penup()
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(random.choice(COLORS))
            y_position = random.randint(-250,250)
            car.goto(300, y_position)
            self.cars_list.append(car)
    def move_cars(self):
        for car in self.cars_list:
            car.backward(self.cars_speed)


    def level_up(self):
        self.cars_speed = MOVE_INCREMENT
