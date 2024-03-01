from config import *

def salir():
    global gameOn
    gameOn = False

# ----------------------------
#controla cierre de la ventana con ESC
screen.onkey(salir, "Escape")

# ----------------------------
reinicia()

ball = Ball() # agrega bola rebotadora
paddle = Paddle() # agrega raqueta
marcador = Marcador() # agrega raqueta
marcador.actualiza()
mensaje = Mensaje()

screen.onkeypress(paddle.go_right, "Right")
screen.onkeyrelease(paddle.stop, "Right")

screen.onkeypress(paddle.go_left, "Left")
screen.onkeyrelease(paddle.stop, "Left")

while gameOn:
    time.sleep(0.01)            # sleep
    ball.move()                 # mueve bola
    paddle.move()               # mueve raqueta
    screen.update()             # actualiza ventana

    # colision bordes
    if ball.ycor() > turtle.window_height():
        ball.stop()
        mensaje.muestra()

    if ball.xcor() > turtle.window_width() or ball.xcor() < 0:
        ball.bounceX()

    if ball.ycor() < 0:
        ball.bounceY()

    #colision paddle
    if ball.distance(paddle) < 50 and ball.ycor() > 530:
        ball.bounceY()

    # colision tortuga ladrillo
    for lad in ladrillos:
        if lad.distance(ball) < 20:
            lad.eliminar()
            ladrillos.remove(lad)
            ball.bounceY()
            marcador.scorePlayer += 1
            marcador.actualiza()

    if len(ladrillos) <= 0:
        reinicia()

#------------------
#screen.exitonclick()