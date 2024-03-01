from turtle import *

class Mensaje(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.scorePlayer = 0

    def muestra(self):
        self.clear()
        self.goto(400, 400)
        self.write(f"fin del juego!", align="center", font=("Consolas", 50, "normal"))

    def esconde(self):
        self.clear()
        self.goto(400, 50)
        self.write("")
