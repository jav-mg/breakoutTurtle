from turtle import *

class Ladrillo(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.reset()
        self.shapesize(1, 2)
        self.color("black")

    def set(self, xpos, ypos, color):
        self.penup()
        self.color(color)
        self.goto(xpos, ypos)

    def eliminar(self):
        self.goto(-30, -30)
        self.penup()
