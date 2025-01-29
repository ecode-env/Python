from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed('fastest')
        self.refresh()
    def refresh(self):
        random_x = random.randint(-180, 180)
        random_y = random.randint(-180, 180)
        self.goto(random_x, random_y)