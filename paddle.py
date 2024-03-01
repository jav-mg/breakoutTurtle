from turtle import *

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.speedMax = 4
        self.speed = 0
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(400, 550)

    def go_left(self):
        self.speed = -self.speedMax

    def go_right(self):
        self.speed = self.speedMax

    def stop(self):
        self.speed = 0

    def move(self):
        self.goto(self.xcor() + self.speed, self.ycor())
