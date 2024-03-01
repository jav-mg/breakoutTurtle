import turtle
from turtle import *
from ladrillo import *
from ball import *
from paddle import *
from score import *
from mensaje import *
import random
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
turtle.setworldcoordinates(0, turtle.window_height(), turtle.window_width(), 0)
screen.title("Breakout")
screen.tracer(0)                # This function is used to turn turtle animation on or off and set a delay for update drawings.
screen.listen()                 # escucha keypress
# -----------------------------------------------------------------

POSINICIAL_X = 40
POSINICIAL_y = 90
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
TOTAL = 45
ladrillos = []
gameOn = True

#---------------------------
#procedimnientos y funciones

def reinicia():
    ladrillos.clear()
    posX = POSINICIAL_X
    posY = POSINICIAL_y
    indi = 0
    # agrega ladrillos en tres filas
    for _ in range(TOTAL):
        if indi == 15:
            posX = POSINICIAL_X
            posY += 30
            indi = 0

        ld = Ladrillo()
        ld.set(posX, posY, random.choice(COLORS))
        ladrillos.append(ld)

        posX += 50
        indi += 1
