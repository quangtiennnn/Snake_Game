from random import randint
from turtle import Turtle
class food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.speed(20)
        self.shapesize(0.5,0.5)
        self.refresh()
    def refresh(self):
        x = randint(-240,240)
        y = randint(-240,240)
        self.goto(x,y)
