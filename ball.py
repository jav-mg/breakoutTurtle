from turtle import *
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed = 8
        self.shape("square")
        self.color("white")
        self.penup()
        self.xMove = 0
        self.yMove = 3
        self.goto(400,300)

    def move(self):
        if self.speed > 0:
            corX = self.xcor() + self.xMove
            corY = self.ycor() + self.yMove
            self.goto(corX, corY)

    def bounceY(self):
        self.yMove *= -1
        self.xMove += random.uniform(0, 2)
        if self.xMove > self.speed:
            self.xMove = self.speed

        if self.xMove < -self.speed:
            self.xMove = -self.speed

    def bounceX(self):
        self.xMove *= -1

    def reset(self):
        self.goto(0,0)
        self.bounceX()

    def stop(self):
        self.goto(-30,-30)
        self.speed = 0

    def nuevaVelocidad(self):
        self.yMove = random.uniform(0,self.speed)
        if self.yMove < (self.speed/2):
            self.yMove +=1

        self.xMove = self.yMove - self.speed
