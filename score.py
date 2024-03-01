from turtle import *

class Marcador(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.scorePlayer = 0
        self.actualiza()

    def actualiza(self):
        self.clear()
        self.goto(400, 50)
        self.write(f"{self.scorePlayer}", align="center", font=("Consolas", 30, "normal"))
